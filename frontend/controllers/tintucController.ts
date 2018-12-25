/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IDanhMucPageLogic } from "../pagelogics/danhmucPageLogic";
import { ITinTucPageLogic } from "../pagelogics/tintucPageLogic";
import { tintucForm } from "../forms/tintucForms";

export class TinTucController extends Controller {
    static $inject: string[] = ["TinTucPageLogic", "DanhMucPageLogic"];

    private danhmucPageLogic: IDanhMucPageLogic;
    private tintucPageLogic: ITinTucPageLogic;

    constructor(
        danhmucPageLogic: IDanhMucPageLogic,
        tintucPageLogic: ITinTucPageLogic
    ) {
        super();
        this.danhmucPageLogic = danhmucPageLogic;
        this.tintucPageLogic = tintucPageLogic;
    }

    @Method.get("/quanlytintuc/")
    @Method.post("/quanlytintuc/")
    public async tintuc(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = tintucForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.tintucPageLogic.createTinTuc({
                    danhmuc_id: data.danhmuc_id,
                    tieude: data.tieude,
                    hinhanh: data.hinhanh,
                    mota: data.mota,
                    noidung: data.noidung,
                    ngaydang: data.ngaydang,
                    trangthai: data.trangthai
                });
            }
            form = formResult.form;
        }

        let tintucs = await this.tintucPageLogic.getTinTucs({
            limit: 5,
            offset: 0
        });

        let danhmucs = await this.danhmucPageLogic.getDanhMucs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "tintuc_sp" : "tintuc", {
            title: "Quản Lý TinTuc",
            form: form,
            tintucs: tintucs ? tintucs.results : null,
            danhmucs: danhmucs ? danhmucs.results : null,
        });
    }

    @Method.get("/quanlytintuc/:id/")
    @Method.post("/quanlytintuc/:id/")
    public async tintucdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = tintucForm;
        let danhmucId: number = parseInt(req.params.id, 10) || 0;
        let tintucId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.tintucPageLogic.updateTinTuc(tintucId, {
                    danhmuc_id: data.danhmuc_id,
                    tieude: data.tieude,
                    hinhanh: data.hinhanh,
                    mota: data.mota,
                    noidung: data.noidung,
                    ngaydang: data.ngaydang,
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlytintuc/`);
            }
            form = formResult.form;
        }

        let tintuc = await this.tintucPageLogic.getTinTuc(tintucId);

        let danhmuc = await this.danhmucPageLogic.getDanhMuc(danhmucId);

        return res.namedView(req.isMobile() ? "tintuc_sp" : "tintucdetail", {
            title: "Quản Lý Tin Tức",
            form: form,
            danhmuc: danhmuc,
            tintuc: tintuc
        });
    }
}
