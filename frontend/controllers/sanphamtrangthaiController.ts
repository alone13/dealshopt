/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ISanPhamTrangThaiPageLogic } from "../pagelogics/sanphamtrangthaiPageLogic";
import { sanphamtrangthaiForm } from "../forms/sanphamtrangthaiForms";

export class SanPhamTrangThaiController extends Controller {
    static $inject: string[] = ["SanPhamTrangThaiPageLogic"];

    private sanphamtrangthaiPageLogic: ISanPhamTrangThaiPageLogic;

    constructor(
        sanphamtrangthaiPageLogic: ISanPhamTrangThaiPageLogic
    ) {
        super();
        this.sanphamtrangthaiPageLogic = sanphamtrangthaiPageLogic;
    }

    @Method.get("/quanlysanphamtrangthai/")
    @Method.post("/quanlysanphamtrangthai/")
    public async trangthai(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamtrangthaiForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamtrangthaiPageLogic.createSanPhamTrangThai({
                    trangthai: data.trangthai
                });
            }
            form = formResult.form;
        }

        let sanphamtrangthais = await this.sanphamtrangthaiPageLogic.getSanPhamTrangThais({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "trangthai_sp" : "trangthai", {
            title: "Quản Lý Sản Phẩm - Trạng Thái",
            form: form,
            sanphamtrangthais: sanphamtrangthais ? sanphamtrangthais.results : null
        });
    }

    @Method.get("/quanlysanphamtrangthai/:id/")
    @Method.post("/quanlysanphamtrangthai/:id/")
    public async trangthaidetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamtrangthaiForm;
        let sanphamtrangthaiId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamtrangthaiPageLogic.updateSanPhamTrangThai(sanphamtrangthaiId, {
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlysanphamtrangthai/`);
            }
            form = formResult.form;
        }

        let sanphamtrangthai = await this.sanphamtrangthaiPageLogic.getSanPhamTrangThai(sanphamtrangthaiId);

        return res.namedView(req.isMobile() ? "trangthai_sp" : "trangthaidetail", {
            title: "Quản Lý Sản Phẩm - Trạng Thái",
            form: form,
            sanphamtrangthai: sanphamtrangthai
        });
    }
}
