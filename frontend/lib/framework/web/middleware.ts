/// <reference path="../../../typings/izischool.d.ts"/>

import * as express from "express";
import * as decorators from "../decorators";
import * as bluebird from "bluebird";
import * as uuid from "node-uuid";

import { HttpStatusCodes } from "../statusCodes";
import { Dependency } from "../ioc/dependency";

interface VisitorIdOptions {
    maxAge: number;
}

export function visitorId(options: VisitorIdOptions): express.RequestHandler {
    return (req: express.Request, res: express.Response, next: express.NextFunction): any => {
        if (!req.cookies.visitorId || !/^[0-9a-fA-F\-]{36}$/.test(req.cookies.visitorId)) {
            const visitorId = uuid.v4();
            req.cookies.visitorId = visitorId;
            res.cookie("visitorId", visitorId, { maxAge : options.maxAge });
        }
        return next();
    };
}

@Dependency.register()
export class Middleware {
    static proxy(target: Object, key: string, descriptor: TypedPropertyDescriptor<any>): void {
        const metaFunction = decorators.makeMeta(descriptor.value);
        metaFunction.meta.isProxy = true;
    }

    static before(middlewareResolver: decorators.MiddlewareResolver): MethodDecorator {
        return (target: Object, propertyKey: string, descriptor: TypedPropertyDescriptor<any>) => {
            const metaFunction = decorators.makeMeta(descriptor.value);
            metaFunction.meta.middleware.before.push(middlewareResolver);
        };
    }

    static after(middlewareResolver: decorators.MiddlewareResolver): MethodDecorator {
        return (target: Object, propertyKey: string, descriptor: TypedPropertyDescriptor<any>) => {
            const metaFunction = decorators.makeMeta(descriptor.value);
            metaFunction.meta.middleware.after.push(middlewareResolver);
        };
    }
}
