/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";
import * as intravenous from "intravenous";

import { Controller } from "../lib/framework/web/controller";
import { HttpStatusCodes } from "../shared/statusCodes";

const CSURF_BAD_CSRF_TOKEN_CODE = "EBADCSRFTOKEN";

export class ErrorController extends Controller {
    constructor() {
        super();

    }

    public noUrlMatched(req: express.Request, res: express.Response, next: express.NextFunction): void {
        this.error404(req, res, next);
    }

    public error(err: any, req: express.Request, res: express.Response, next: express.NextFunction): void {
        let httpErrorCode = err.statusCode || NaN;
        let isErrorCodeFromApi = false;
        if (isNaN(httpErrorCode) && err.innerError) {
            httpErrorCode = err.innerError.statusCode || NaN;
            isErrorCodeFromApi = !isNaN(httpErrorCode);
        }
        if (isNaN(httpErrorCode)) {
            return this.error500(err, req, res, next);
        }
        if (httpErrorCode === HttpStatusCodes.NotFound) {
            return this.error404(req, res, next);
        }
        if (httpErrorCode === HttpStatusCodes.BadGateway) {
            return res.send(HttpStatusCodes.BadGateway).end();
        }
        if (err.code === CSURF_BAD_CSRF_TOKEN_CODE) {
            return this.csrfFailed(req, res, next);
        }
        if (httpErrorCode === HttpStatusCodes.BadRequest && !isErrorCodeFromApi) {
            return this.error400(err, req, res, next);
        }

        return this.error500(err, req, res, next);
    }

    public error500(err: any, req: express.Request, res: express.Response, next: express.NextFunction): void {
        res.status(HttpStatusCodes.InternalServerError);

        this.logError(req, err);

        const viewName = req.app.get("env") === "development" ? "error/500_stack.jinja2" : "error/500.jinja2";

        res.render(viewName, {
            requestId: req.headers["x-request-id"] || "unknown",
            error: err,
            prettyDump: (d: any): string => JSON.stringify(d, null, 2),
            formatStackTrace: this.formatStackTrace
        });
    }

    public error404(req: express.Request, res: express.Response, next: express.NextFunction): void {
        res.status(HttpStatusCodes.NotFound);
        res.render("error/404.jinja2");
    }

    public error400(err: any, req: express.Request, res: express.Response, next: express.NextFunction): void {
        res.status(HttpStatusCodes.BadRequest);

        this.logError(req, err);

        res.render("error/400.jinja2");
    }

    public csrfFailed(req: express.Request, res: express.Response, next: express.NextFunction): void {
        res.status(HttpStatusCodes.Forbidden);
        res.render("error/csrf.jinja2", {
            originalUrl: req.originalUrl
        });
    }

    private logError(req: express.Request, error: Error): void {
        let a = 1;
    }

    private formatStackTrace(stackTrace: string): string {
        return stackTrace
            .replace(/</g, "&lt;").replace(/>/g, "&gt;")
            .replace(/(&lt;anonymous&gt);/g, "<span class='anonymous-function'>$1</span>")
            .replace(/\n/g, "<br />")
            .replace(/([a-zA-Z0-9]+)\.(js|ts)/g, "<span class='filename'>$1</span>.$2")
            .replace(/(\d+):(\d+)/g, "<span class='line'>$1</span>:<span class='column'>$2</span>")
            .replace(/at ([a-zA-Z0-9]+)\.([a-zA-Z0-9$]+)/g, "at <span class='class-name'>$1</span>.<span class='function-name'>$2</span>")
            .replace(new RegExp(process.cwd(), "g"), "~");
    }
}
