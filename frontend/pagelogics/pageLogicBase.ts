/// <reference path="../typings/izischool.d.ts"/>

export interface CollectionRequest {
    limit?: number;
    offset?: number;
}

export interface Sort {
    sort?: string;
}

export abstract class PageLogicBase {
}
