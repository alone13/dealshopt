/// <reference path="../../typings/izischool.d.ts"/>


import * as express from "express";

import { Methods } from "./web/controller";

export interface IMetaFunction extends Function {
    meta: MetaObject;
}

export interface MiddlewareResolver {
    (): express.RequestHandler | express.ErrorRequestHandler;
}

export class MetaObject {
    methods: IMetaRouteDescriptor[];
    middleware: {
        before: MiddlewareResolver[]
        after: MiddlewareResolver[]
    };
    isProxy: boolean;

    constructor() {
        this.methods = [];
        this.isProxy = false;
        this.middleware = {
            before: [],
            after: []
        };
    }
}

export interface IMetaRouteDescriptor {
    method: Methods;
    path: string;
    requiredAccessFlags?: string[];
}

export function makeMeta(func: Function): IMetaFunction {
    const metaFunc = <IMetaFunction>func;
    if (!metaFunc.meta) {
        metaFunc.meta = new MetaObject();
    }
    return metaFunc;
}
