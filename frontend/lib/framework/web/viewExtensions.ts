/// <reference path="../../../typings/izischool.d.ts"/>

import * as intravenous from "intravenous";
import * as express from "express";
import * as nunjucks from "nunjucks";

const X_REQUEST_ID_HEADER_NAME = "x-request-id";

export class AwaitExtension {
    tags: string[] = ["await"];

    public parse(parser: any, nodes: any, lexer: any): any {
        const tok = parser.nextToken();
        const args = parser.parseSignature(null, true);
        parser.advanceAfterBlockEnd(tok.value);

        return new nodes.CallExtensionAsync(this, "run", args, []);
    }

    public run(context: any, asyncResult: any, callback: Function): void {
        try {
            if (asyncResult.then) {
                (<Promise<any>>asyncResult).then(
                    result => {
                        try {
                            callback(null, result);
                        } catch (error) {
                            console.log(error.stack); /* DO NOT REMOVE */
                            callback(error.stack);
                        }
                    },
                    err => {
                        callback(err.stack);
                    }
                );
            } else {
                callback(null, asyncResult);
            }
        } catch (error) {
            callback(error);
        }
    }
}

export class PartialViewExtension {
    tags: string[] = ["partial"];

    constructor(container: intravenous.IContainer, env: nunjucks.IEnvironment) {
        this.container = container;
        this.env = env;
    }
    private container: intravenous.IContainer;
    private env: nunjucks.IEnvironment;

    public parse(parser: any, nodes: any, lexer: any): any {
        const tok = parser.nextToken();
        const args = parser.parseSignature(null, true);
        parser.advanceAfterBlockEnd(tok.value);

        return new nodes.CallExtensionAsync(this, "run", args, []);
    }

    public run(context: any, request: express.Request, response: express.Response, controller: string, action: string, partialModelOrCallback: Object|Function, callback: Function): void {
        if (!request || !response) {
            throw new Error("Please pass request and response to the view");
        }
        let partialModel: Object | null = null;
        if (typeof partialModelOrCallback === "function") {
            callback = <Function>partialModelOrCallback;
        } else {
            partialModel = <Object>partialModelOrCallback;
        }

        const ctrl = this.container.get(`${controller}Controller`);
        const handler = ctrl[action].bind(ctrl);

        let promise: Promise<string> | null = null;
        try {
            promise = <Promise<string>>handler(request, response, this.env, partialModel);
        } catch (error) {
            callback(error);
            return;
        }

        if (!promise.then) {
            throw new RangeError(`Partial view must return promise! ${controller}Controller.${action}`);
        }

        promise.then(content => {
            const result = new nunjucks.runtime.SafeString(content);
            try {
                callback(null, result);
            } catch (error) {
                this.logError(request, error, partialModel);
                callback(error);
            }
        }).catch(error => {
            try {
                this.logError(request, error, partialModel);
            } finally {
                callback(error);
            }
        });
    }

    private logError(request: express.Request, error: any, partialModel: Object | null): void {
        const scope = this.container.create();
        let requestId = "unknown";
        if (request) {
            requestId = request.headers[X_REQUEST_ID_HEADER_NAME] || "unknown";
        }
        scope.register("RequestId", requestId);
    }
}
