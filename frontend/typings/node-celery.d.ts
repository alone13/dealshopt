/// <reference path="./node/node.d.ts"/>

declare module "node-celery" {
    export interface ICeleryClient {
        call(taskName: string, params: { [key: string]: any }[], options?: any, callback?: Function): void;
    }

    export function createClient(opts?: {
        CELERY_BROKER_URL: string;
        CELERY_RESULT_BACKEND: string;
    }): any;
}
