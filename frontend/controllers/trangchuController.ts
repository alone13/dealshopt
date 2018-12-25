/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ITrangChuPageLogic } from "../pagelogics/trangchuPageLogic";
import { ISanPhamPageLogic } from "../pagelogics/sanphamPageLogic";

export class TrangChuController extends Controller {
    static $inject: string[] = ["TrangChuPageLogic", "SanPhamPageLogic"];

    private trangchuPageLogic: ITrangChuPageLogic;
    private sanphamPageLogic: ISanPhamPageLogic;

    constructor(
        trangchuPageLogic: ITrangChuPageLogic,
        sanphamPageLogic: ISanPhamPageLogic
    ) {
        super();
        this.trangchuPageLogic = trangchuPageLogic;
        this.sanphamPageLogic = sanphamPageLogic;
    }

    @Method.get("/")
    public async trangchu(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {

        return res.namedView(req.isMobile() ? "trangchu_sp" : "trangchu", {
            title: "Trang Chủ"
        });
    }
}
