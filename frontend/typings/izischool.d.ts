/// <reference path="tsd.d.ts" />
/// <reference path="./supertest/supertest.d.ts"/>
/// <reference path="./convict.d.ts"/>
/// <reference path="./multer.d.ts"/>
/// <reference path="./asyncExtensions.d.ts"/>
/// <reference path="./mmmagic.d.ts"/>
/// <reference path="./sharp.d.ts"/>

interface Array<T> {
    filter<U extends T>(pred: (a: T) => a is U): U[];
}

declare module "nunjucks" {
    import * as express from "express";

    export module runtime {
        export class SafeString {
            constructor(data: string);
        }
    }

    export interface IOptions {
        autoescape?: boolean;
        throwOnUndefined?: boolean;
        trimBlocks?: boolean;
        lstripBlocks?: boolean;
        watch?: boolean;
        noCache?: boolean;
        web?: {
            useCache?: boolean,
            async?: boolean
        };
        express?: express.Express;
    }

    export interface IEnvironment {
        filters: {
            escape: Function;
        };
        render(name: string, context?: any): string;
        render(name: string, context: any, callback: Function): void;
        renderString(name: string, context?: any, callback?: Function): string|void;
        addGlobal(name: string, value: any): IEnvironment;
        getGlobal(name: string): any;
        addExtension(name: string, value: any): void;
        addFilter(name: string, func: Function): IEnvironment;
    }

    export interface ITemplate {
        render(context: any, callback?: Function): string|void;
    }

    export function configure(path?: string, opts?: IOptions): IEnvironment;
    export function compile(src: string, env: IEnvironment, path: string, eagerCompile: boolean): ITemplate
    export function render(name: string, context?: any, callback?: Function): string|void;
    export function renderString(str: string, context?: any, callback?: Function): string|void;
    export function installJinjaCompat(): void;
}

declare module "nunjucks-date-filter" {
    export function setDefaultFormat(format: string): any;
    export function install(env: any, customName: string): void;
}

declare module "intravenous" {
    export interface IRegisterFn {
        (name: string, object: Function|Object, lifecycle?: string): void;
    }

    export interface IGetFn {
        (name: string): any;
    }

    export interface IContainer {
        register: IRegisterFn;
        get: IGetFn;
        create(): IContainer;
        dispose(): void;
    }

    export interface IFactory<T> {
        get(): T;
        use(dependencyName: string, overrideValue: any): IFactory<T>;
    }

    export function create(): IContainer;
}

declare module Express {
    export interface Response {
        view<T>(model?: T): void;
        namedView<T>(name: string, model?: T): void;

        notFound(message?: string): void;
    }

    export interface Request {
        sessionID?: string;
        multerErrors: {
            [key: string]: string;
        };
        isMobile(): boolean;
        isMobileOrTablet(): boolean;
        isAjax(): boolean;
        controllerName: string;
        actionName: string;
    }
}
