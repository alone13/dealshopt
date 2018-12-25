/// <reference path="../../../typings/izischool.d.ts"/>

import * as express from "express";
import * as decorators from "../decorators";
import * as intravenous from "intravenous";
import * as forms from "forms";
import * as bluebird from "bluebird";
import * as debugModule from "debug";

import { HttpStatusCodes } from "../statusCodes";
import { ParameterResolverMiddleware } from "./parameterResolver";

const X_REQUEST_ID_HEADER_NAME = "x-request-id";

export enum Methods {
    Get, Post, All
}

export class Method {
    static get(path: string, requiredAccessFlags?: string[]): MethodDecorator {
        return Method.addMetod(Methods.Get, path, requiredAccessFlags);
    }
    static post(path: string, requiredAccessFlags?: string[]): MethodDecorator {
        return Method.addMetod(Methods.Post, path, requiredAccessFlags);
    }

    private static addMetod(method: Methods, path: string, requiredAccessFlags?: string[]): MethodDecorator {
        return (target: Object, key: string, descriptor: TypedPropertyDescriptor<any>) => {
            const metaFunction = decorators.makeMeta(descriptor.value);
            metaFunction.meta.methods.push({
                method: method,
                path: path,
                requiredAccessFlags: requiredAccessFlags
            });
        };
    }
}

const METHOD_MAP = {};
METHOD_MAP[Methods.Get] = "get";
METHOD_MAP[Methods.Post] = "post";
METHOD_MAP[Methods.All] = "all";

export interface FormHandleResult<T> {
    error: boolean;
    success: boolean;
    form: forms.IBoundForm<T>;
    data: T;
}


const debug = debugModule("izischool-framework:controller");

export class Controller {
    public router: express.Router;

    protected className: string;
    protected controllerName: string;

    constructor() {
        this.className = Object.getPrototypeOf(this).constructor.name;
        this.controllerName = this.className.replace(/Controller/, "");
        /* magic: Need to camelify this string */
        this.controllerName = this.controllerName.substring(0, 1).toLowerCase() + this.controllerName.substring(1);
        debug(`Created ${this.className}`);
    }

    protected handleForm<T>(req: express.Request, form: forms.IForm<T>, isOptional?: boolean): Promise<FormHandleResult<T>> {
        return new Promise<FormHandleResult<T>>((resolve, reject) => {
            const callbacks: forms.ICallbacks<T> = {
                success: (f): void => {
                    resolve({
                        error: false,
                        success: true,
                        form: f,
                        data: f.data || <T>{}
                    });
                },
                error: (f): void => {
                    resolve({
                        error: true,
                        success: false,
                        form: f,
                        data: f.data
                    });
                }
            };
            callbacks.empty = isOptional
                ? callbacks.success
                : callbacks.error;

            form.handle(req, callbacks);
        });
    }

    /**
     * Registers controller methods as cations if they have @Method decorator.
     * @param {intravenous.IContainer} container Container to resolve dependencies from
     * @param {express.Router}         router    Router to register actions with
     */
    public _registerController(container: intravenous.IContainer, router: express.Router): void {
        this.router = router;

        debug(`Registering ${this.className}`);

        for (const f of this.enumerateMethods(this)) {
            if (!this[f].meta) {
                continue;
            }

            const mf = <decorators.IMetaFunction>this[f];
            for (const method of mf.meta.methods) {
                const routerMethod: Function = this.router[METHOD_MAP[method.method]].bind(this.router);

                // const actionMiddleware = (mf.meta.isProxy ? mf() : mf).bind(controller);

                const middlewareChain: (express.RequestHandler | express.ErrorRequestHandler)[] = [];
                if (method.path.startsWith("!")) {
                    const originalPath = method.path;
                    method.path = "/:url(*)";
                    const parameterResolverMiddleware = <ParameterResolverMiddleware>container.get("ParameterResolverMiddleware");
                    middlewareChain.push(parameterResolverMiddleware.create(originalPath.substr(1)));
                }

                middlewareChain.push(...this.resolveMiddlewares(mf.meta.middleware.before));

                const actionDispatcher = async (req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> => {
                    const scope = container.create();
                    scope.register("RequestId", req.headers[X_REQUEST_ID_HEADER_NAME] || "unknown");
                    scope.register("ClientId", function(): any {
                        this.get = function(): any {
                            if (req.isAuthenticated()) {
                                return req.user.clientId;
                            }
                            return "unknown";
                        };
                    });
                    const controllerInstance = scope.get(this.className);
                    scope.dispose();
                    debug(`Created instance of ${this.className}`);
                    if (!controllerInstance) {
                        // O.o
                    }

                    const actionMiddleware = <express.RequestHandler>(mf.meta.isProxy ? mf() : mf).bind(controllerInstance);

                    try {
                        this.extendRequestAndResponse(req, res, next, actionMiddleware);
                        debug(`request resolved to ${req.controllerName}.${req.actionName}`);
                        const result = actionMiddleware(req, res, next);
                        if (result["then"]) {
                            /* tslint:disable:no-unused-expression We need the side effect, not the return value*/
                            await result;
                            /* tslint:enable */
                            // next();
                        }
                    } catch (error) {
                        next(error);
                    }
                };
                middlewareChain.push(actionDispatcher);

                middlewareChain.push(...this.resolveMiddlewares(mf.meta.middleware.after));

                const args = [method.path, middlewareChain];
                routerMethod.apply(this.router, args);
            }
        }
    }

    /* tslint:disable:no-unused-variable This function is used indirectly from `middlewareWrapper` in `register method` */
    private extendRequestAndResponse(req: express.Request, res: express.Response, next: express.NextFunction, currentMethod: Function): void {
    /* tslint: enable */
        const methodName = currentMethod.name.replace("bound ", "");

        const viewMethod = (model?: Object): void => {
            const typeofModel = typeof model;

            const viewName: string = `${this.controllerName}/${methodName}.jinja2`;
            let viewModel: Object | null = null;

            if (typeofModel === "object" && !!model) {
                viewModel = model;
            } else {
                viewModel = {};
            }

            viewModel["req"] = req;
            viewModel["res"] = res;

            try {
                res.render(viewName, viewModel);
            } catch (error) {
                next(error);
            }
        };

        const namedViewMethod = (name: string, model?: Object): void => {
            const typeofName = typeof name;
            const typeofModel = typeof model;

            let viewName: string = name;
            let viewModel: Object | null = null;

            if (viewName.indexOf("/") === -1) {
                viewName = `${this.controllerName}/${viewName}.jinja2`;
            }

            if (typeofModel === "object" && !!model) {
                viewModel = model;
            } else {
                viewModel = {};
            }

            viewModel["req"] = req;
            viewModel["res"] = res;

            try {
                res.render(viewName, viewModel);
            } catch (error) {
                next(error);
            }
        };

        const notFoundMethod = (message?: string): void => {
            const error: any = new Error();
            error.statusCode = HttpStatusCodes.NotFound;
            next(error);
        };

        res.view = viewMethod;
        res.namedView = namedViewMethod;
        res.notFound = notFoundMethod;

        const mobileRegex = /(iPhone|Android)/;
        const isMobile = (): boolean => {
            const ua = req.headers["user-agent"];
            return mobileRegex.test(ua);
        };

        const mobileOrTabletRegex = /(iPhone|iPad|Android)/;
        const isMobileOrTablet = (): boolean => {
            const ua = req.headers["user-agent"];
            return mobileOrTabletRegex.test(ua);
        };

        const isAjax = (): boolean => {
            return req.xhr || (!!req.headers["accept"] && req.headers["accept"].indexOf("json") !== -1);
        };

        req.isMobile = isMobile;
        req.isMobileOrTablet = isMobileOrTablet;
        req.isAjax = isAjax;
        req.controllerName = this.controllerName;
        req.actionName = methodName;
    }

    private resolveMiddlewares(middlewareResolvers: decorators.MiddlewareResolver[]): (express.RequestHandler | express.ErrorRequestHandler)[] {
        const result: (express.RequestHandler | express.ErrorRequestHandler)[] = [];
        for (const res of middlewareResolvers) {
            result.push(res());
        }
        return result;
    }

    private enumerateMethods(obj: Object): string[] {
        const result: string[] = [];
        for (const name of Object.getOwnPropertyNames(Object.getPrototypeOf(obj))) {
            const method = obj[name];
            if (!(method instanceof Function) || name === "constructor") {
                continue;
            }
            result.push(name);
        }
        return result;
    }
}
