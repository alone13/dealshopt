/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ISanPhamBaoMatPageLogic } from "../pagelogics/sanphambaomatPageLogic";
import { sanphambaomatForm } from "../forms/sanphambaomatForms";

export class SanPhamBaoMatController extends Controller {
    static $inject: string[] = ["SanPhamBaoMatPageLogic"];

    private sanphambaomatPageLogic: ISanPhamBaoMatPageLogic;

    constructor(
        sanphambaomatPageLogic: ISanPhamBaoMatPageLogic
    ) {
        super();
        this.sanphambaomatPageLogic = sanphambaomatPageLogic;
    }

    @Method.get("/quanlysanphambaomat/")
    @Method.post("/quanlysanphambaomat/")
    public async baomat(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphambaomatForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphambaomatPageLogic.createSanPhamBaoMat({
                    ten: data.ten
                });
            }
            form = formResult.form;
        }

        let sanphambaomats = await this.sanphambaomatPageLogic.getSanPhamBaoMats({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "baomat_sp" : "baomat", {
            title: "Quản Lý Sản Phẩm - Bảo Mật",
            form: form,
            sanphambaomats: sanphambaomats ? sanphambaomats.results : null
        });
    }

    @Method.get("/quanlysanphambaomat/:id/")
    @Method.post("/quanlysanphambaomat/:id/")
    public async baomatdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphambaomatForm;
        let sanphambaomatId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphambaomatPageLogic.updateSanPhamBaoMat(sanphambaomatId, {
                    ten: data.ten
                });
                return res.redirect(`/quanlysanphambaomat/`);
            }
            form = formResult.form;
        }

        let sanphambaomat = await this.sanphambaomatPageLogic.getSanPhamBaoMat(sanphambaomatId);

        return res.namedView(req.isMobile() ? "baomat_sp" : "baomatdetail", {
            title: "Quản Lý Sản Phẩm - Bảo Mật",
            form: form,
            sanphambaomat: sanphambaomat
        });
    }
}
