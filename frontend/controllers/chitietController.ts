/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IChiTietPageLogic } from "../pagelogics/chitietPageLogic";

export class ChiTietController extends Controller {
    static $inject: string[] = ["ChiTietPageLogic"];

    private chitietPageLogic: IChiTietPageLogic;

    constructor(
        chitietPageLogic: IChiTietPageLogic,
    ) {
        super();
        this.chitietPageLogic = chitietPageLogic;
    }

    @Method.get("/chitiet/")
    public async chitiet(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        console.log("vv");
        return res.namedView(req.isMobile() ? "chitiet_sp" : "chitiet", {
            title: "Chi Tiết"
        });
    }
}
