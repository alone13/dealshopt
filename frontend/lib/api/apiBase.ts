/// <reference path="../../typings/izischool.d.ts"/>

import * as request from "request-promise";
import { Request } from "request";
import * as url from "url";
import * as querystring from "querystring";

import { HttpStatusCodes } from "../framework/statusCodes";

export enum ApiRequestMethod {
    GET,
    POST,
    PUT,
    DELETE
}


export interface RequestParameters<T> {
    method: ApiRequestMethod;
    body?: T;
    query?: { [key: string]: any } | null;
    url: string;
    headers?: { [key: string]: string };
}

export interface ApiListResponse<T> {
    count: number;
    current: string;
    prev: string;
    next: string;
    results: T[];
}

export interface ApiListResponseLite<T> {
    results: T[];
}

export interface PagedApiRequest {
    sort?: string|string[];
    limit?: number;
    offset?: number;
}

export interface HttpResponseBase {
    statusCode: number;
    headers: { [name: string]: string };
    request: {
        uri: url.Url;
        method: string;
        headers: { [name: string]: string };
    };
}

export interface Response<T> extends HttpResponseBase {
    body: T | null;
}

export interface CleanupFunction<T> {
    (data: T): T;
}

export abstract class ApiBase {
    constructor(urlRoot: string, requestId: string) {
        this.urlRoot = urlRoot;
        this.requestId = requestId;
    }

    protected urlRoot: string;
    protected requestId: string;

    protected post<TBody, TReturn>(url: string, body?: TBody, query?: { [key: string]: any } | null, cleanup?: CleanupFunction<TBody>): Promise<Response<TReturn>> {
        return this.request<TBody, TReturn>(
            {
                method: ApiRequestMethod.POST,
                query: query,
                body: body,
                url: url
            },
            cleanup
        );
    }
    protected get<TReturn>(url: string, query?: { [key: string]: any }): Promise<Response<TReturn>> {
        return this.request<any, TReturn>({
            method: ApiRequestMethod.GET,
            query: query,
            url: url
        });
    }
    protected delete<TBody, TReturn>(url: string, body?: TBody, query?: { [key: string]: any }, cleanup?: CleanupFunction<TBody>): Promise<Response<TReturn>> {
        return this.request<TBody, TReturn>(
            {
                method: ApiRequestMethod.DELETE,
                query: query,
                body: body,
                url: url
            },
            cleanup
        );
    }

    protected put<TBody, TReturn>(url: string, body?: TBody, query?: { [key: string]: any } | null, cleanup?: CleanupFunction<TBody>): Promise<Response<TReturn>> {
        return this.request<TBody, TReturn>(
            {
                method: ApiRequestMethod.PUT,
                query: query,
                body: body,
                url: url
            },
            cleanup
        );
    }

    protected async request<TBody, TReturn>(parameters: RequestParameters<TBody>, cleanup?: CleanupFunction<TBody>): Promise<Response<TReturn>> {
        if (!parameters.url) {
            throw new Error("url parameter is required");
        }

        if (!parameters.url.endsWith("/")) {
            throw new Error("Url must be terminated with /");
        }

        let requestUrl = url.resolve(this.urlRoot, parameters.url);
        let dataPromise: Promise<Request> | Request | null = null;
        let headers = {
            "X-Request-ID": this.requestId
        };

        if (parameters.query) {
            for (let key in parameters.query) {
                if (!parameters.query.hasOwnProperty(key)) {
                    continue;
                }
                let value = parameters.query[key];
                if (value instanceof Array) {
                    parameters.query[key] = value.join(",");
                }
            }
        }

        switch (parameters.method) {
            case ApiRequestMethod.GET:
                dataPromise = request.get(requestUrl, {
                    resolveWithFullResponse: true,
                    qs: parameters.query,
                    json: true,
                    headers: headers
                });
                break;
            case ApiRequestMethod.POST:
                dataPromise = request.post(requestUrl, {
                    resolveWithFullResponse: true,
                    qs: parameters.query,
                    json: true,
                    body: parameters.body,
                    headers: headers
                });
                break;
            case ApiRequestMethod.PUT:
                dataPromise = request.put(requestUrl, {
                    resolveWithFullResponse: true,
                    qs: parameters.query,
                    json: true,
                    body: parameters.body,
                    headers: headers
                });
                break;
            case ApiRequestMethod.DELETE:
                dataPromise = request.del(requestUrl, {
                    resolveWithFullResponse: true,
                    qs: parameters.query,
                    json: true,
                    body: parameters.body,
                    headers: headers
                });
                break;
            default:
                throw new Error(`Method ${parameters.method} is unsupported`);
        }

        let realStackTrace = new Error("ApiError. See InnerError for details");
        let timestart: number[] | undefined = undefined;
        try {
            timestart = process.hrtime();
            let data = await dataPromise;
            let httpResponse = <Response<TReturn>>data.toJSON();
            return httpResponse;
        } catch (error) {
            if (error.statusCode && (error.statusCode === HttpStatusCodes.NotFound
                || error.statusCode === HttpStatusCodes.Unauthorized)) {
                let httpResponse = <Response<TReturn>>error.response.toJSON();
                httpResponse.body = null;
                return httpResponse;
            }

            try {
                let data = parameters.body;
                if (data && cleanup) {
                    data = cleanup(data);
                }


            } catch (cleanupError) {
                console.log(cleanupError);
            }

            let err: any = new Error();
            err.stack = realStackTrace.stack;

            let innerErr: any = new Error();
            innerErr.message = error.message;
            innerErr.stack = error.stack;
            innerErr["error"] = error.error;
            innerErr["statusCode"] = error.statusCode;

            err.innerError = innerErr;
            throw err;
        }
    }

    /**
     * Stolen from http://stackoverflow.com/a/24648941
     */
    private cloneObject<T>(o: any): T {
        const gdcc = "__getDeepCircularCopy__";
        if (o !== Object(o)) {
            return o; // primitive value
        }

        let set = gdcc in o;
        let cache = o[gdcc];
        let result: any;

        if (set && typeof cache === "function") {
            return cache();
        }
        // else
        o[gdcc] = function(): any { return result; }; // overwrite
        if (o instanceof Array) {
            result = [];
            for (let i = 0; i < o.length; i++) {
                result[i] = this.cloneObject(o[i]);
            }
        } else {
            result = {};
            for (let prop in o) {
                if (prop !== gdcc) {
                    result[prop] = this.cloneObject(o[prop]);
                } else if (set) {
                    result[prop] = this.cloneObject(cache);
                }
            }
        }
        if (set) {
            o[gdcc] = cache; // reset
        } else {
            delete o[gdcc]; // unset again
        }
        return result;
    }
}
