/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ISanPhamGiaPageLogic } from "../pagelogics/sanphamgiaPageLogic";
import { ISanPhamPageLogic } from "../pagelogics/sanphamPageLogic";
import { sanphamgiaForm } from "../forms/sanphamgiaForms";

export class SanPhamGiaController extends Controller {
    static $inject: string[] = ["SanPhamGiaPageLogic", "SanPhamPageLogic"];

    private sanphamgiaPageLogic: ISanPhamGiaPageLogic;
    private sanphamPageLogic: ISanPhamPageLogic;

    constructor(
        sanphamgiaPageLogic: ISanPhamGiaPageLogic,
        sanphamPageLogic: ISanPhamPageLogic
    ) {
        super();
        this.sanphamgiaPageLogic = sanphamgiaPageLogic;
        this.sanphamPageLogic = sanphamPageLogic;
    }

    @Method.get("/quanlysanphamgia/")
    @Method.post("/quanlysanphamgia/")
    public async gia(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamgiaForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamgiaPageLogic.createSanPhamGia({
                    sanpham_id: data.sanpham_id
                });
            }
            form = formResult.form;
        }

        let sanphamgias = await this.sanphamgiaPageLogic.getSanPhamGias({
            limit: 5,
            offset: 0
        });

        let sanphams = await this.sanphamPageLogic.getSanPhams({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "gia_sp" : "gia", {
            title: "Quản Lý Giá",
            form: form,
            sanphamgias: sanphamgias ? sanphamgias.results : null,
            sanphams: sanphams ? sanphams.results : null
        });
    }

    @Method.get("/quanlysanphamgia/:id/")
    @Method.post("/quanlysanphamgia/:id/")
    public async giadetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = sanphamgiaForm;
        let sanphamgiaId: number = parseInt(req.params.id, 10) || 0;
        let sanphamId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamgiaPageLogic.updateSanPhamGia(sanphamgiaId, {
                    sanpham_id: data.sanpham_id
                });
                return res.redirect(`/quanlysanphamgia/`);
            }
            form = formResult.form;
        }

        let sanphamgia = await this.sanphamgiaPageLogic.getSanPhamGia(sanphamgiaId);
        let sanpham = await this.sanphamPageLogic.getSanPham(sanphamId);

        return res.namedView(req.isMobile() ? "gia_sp" : "giadetail", {
            title: "Quản Lý Sản Phẩm - Giá",
            form: form,
            sanphamgia: sanphamgia,
            sanpham: sanpham
        });
    }
}
