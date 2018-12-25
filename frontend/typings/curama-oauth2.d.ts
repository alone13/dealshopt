/// <reference path="./passport/passport.d.ts"/>

declare module "passport-oauth2-client-password" {

    import * as passport from "passport";
    import * as express from "express";

    interface IVerifyOptions {
        message: string;
    }

    interface VerifyFunctionWithRequest {
        (req: express.Request, username: string, password: string, done: (error: any, user?: any, options?: IVerifyOptions) => void): void;
    }

    interface VerifyFunction {
        (clientId: string, clientSecret: string, done: (error: any, user?: any, options?: IVerifyOptions) => void): void;
    }

    class Strategy implements passport.Strategy {
        constructor(verify: VerifyFunction);

        name: string;
        authenticate: (req: express.Request, options?: Object) => void;
    }
}

declare module "oauth2orize" {
    import * as express from "express";

    export function createServer(): Server;

    export class exchange {
        static password(issue: Function): express.RequestHandler;
        static password(options: any, issue: Function): express.RequestHandler;
    }

    export class Server {
        exchange(type: string, fn: Function): Server;
        exchange(fn: Function): Server;


        token(): express.RequestHandler;
        errorHandler(): express.RequestHandler;
    }
}
