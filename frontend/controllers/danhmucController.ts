/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IDanhMucPageLogic } from "../pagelogics/danhmucPageLogic";
import { danhmucForm } from "../forms/danhmucForms";

export class DanhMucController extends Controller {
    static $inject: string[] = ["DanhMucPageLogic"];

    private danhmucPageLogic: IDanhMucPageLogic;

    constructor(
        danhmucPageLogic: IDanhMucPageLogic
    ) {
        super();
        this.danhmucPageLogic = danhmucPageLogic;
    }

    @Method.get("/quanlydanhmuc/")
    @Method.post("/quanlydanhmuc/")
    public async danhmuc(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = danhmucForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.danhmucPageLogic.createDanhMuc({
                    danhmuccha: data.danhmuccha,
                    tendanhmuc: data.tendanhmuc,
                    trangthai: data.trangthai,
                    link: data.link
                });
            }
            form = formResult.form;
        }

        let danhmucs = await this.danhmucPageLogic.getDanhMucs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "danhmuc_sp" : "danhmuc", {
            title: "Quản Lý Danh Mục",
            form: form,
            danhmucs: danhmucs ? danhmucs.results : null
        });
    }

    @Method.get("/quanlydanhmuc/:id/")
    @Method.post("/quanlydanhmuc/:id/")
    public async danhmucdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = danhmucForm;
        let danhmucId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.danhmucPageLogic.updateDanhMuc(danhmucId, {
                    danhmuccha: data.danhmuccha,
                    tendanhmuc: data.tendanhmuc,
                    trangthai: data.trangthai,
                    link: data.link
                });
                return res.redirect(`/quanlydanhmuc/`);
            }
            form = formResult.form;
        }

        let danhmuc = await this.danhmucPageLogic.getDanhMuc(danhmucId);

        return res.namedView(req.isMobile() ? "danhmuc_sp" : "danhmucdetail", {
            title: "Quản Lý Danh Mục",
            form: form,
            danhmuc: danhmuc
        });
    }
}
