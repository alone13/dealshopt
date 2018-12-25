/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ISanPhamGiaChiTietPageLogic } from "../pagelogics/sanphamgiachitietPageLogic";
import { ISanPhamGiaPageLogic } from "../pagelogics/sanphamgiaPageLogic";
import { giachitietForm } from "../forms/sanphamgiachitietForms";

export class SanPhamGiaChiTietController extends Controller {
    static $inject: string[] = ["SanPhamGiaChiTietPageLogic", "SanPhamGiaPageLogic"];

    private sanphamgiachitietPageLogic: ISanPhamGiaChiTietPageLogic;
    private sanphamgiaPageLogic: ISanPhamGiaPageLogic;

    constructor(
        sanphamgiachitietPageLogic: ISanPhamGiaChiTietPageLogic,
        sanphamgiaPageLogic: ISanPhamGiaPageLogic
    ) {
        super();
        this.sanphamgiachitietPageLogic = sanphamgiachitietPageLogic;
        this.sanphamgiaPageLogic = sanphamgiaPageLogic;
    }

    @Method.get("/quanlysanphamgiachitiet/")
    @Method.post("/quanlysanphamgiachitiet/")
    public async giachitiet(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = giachitietForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamgiachitietPageLogic.createSanPhamGiaChiTiet({
                    sanpham_gia_id: data.sanpham_gia_id,
                    gia: data.gia,
                    ngaybd: data.ngaybd,
                    ngaykt: data.ngaykt,
                    is_active: data.is_active
                });
            }
            form = formResult.form;
        }

        let sanphamgias = await this.sanphamgiaPageLogic.getSanPhamGias({
            limit: 5,
            offset: 0
        });
        let sanphamgiachitiets = await this.sanphamgiachitietPageLogic.getSanPhamGiaChiTiets({
            limit: 5,
            offset: 0
        });
        return res.namedView(req.isMobile() ? "giachitiet_sp" : "giachitiet", {
            title: "Quản Lý Giá Chi Tiết",
            sanphamgiachitiets: sanphamgiachitiets ? sanphamgiachitiets.results : null
        });
    }

    @Method.get("/quanlysanphamgiachitiet/:id/")
    @Method.post("/quanlysanphamgiachitiet/:id/")
    public async giachitietdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = giachitietForm;
        let sanphamgiaId: number = parseInt(req.params.id, 10) || 0;
        let sanphamgiachitietId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.sanphamgiachitietPageLogic.updateSanPhamGiaChiTiet(sanphamgiachitietId, {
                    sanpham_gia_id: data.sanpham_gia_id,
                    gia: data.gia,
                    ngaybd: data.ngaybd,
                    ngaykt: data.ngaykt,
                    is_active: data.is_active
                });
                return res.redirect(`/quanlysanphamgiachitiet/`);
            }
            form = formResult.form;
        }

        let sanphamgia = await this.sanphamgiaPageLogic.getSanPhamGia(sanphamgiaId);
        let sanphamgiachitiet = await this.sanphamgiachitietPageLogic.getSanPhamGiaChiTiet(sanphamgiachitietId);

        return res.namedView(req.isMobile() ? "giachitiet_sp" : "giachitietdetail", {
            title: "Quản Lý Giá Chi Tiết",
            form: form,
            sanphamgia: sanphamgia,
            sanphamgiachitiet: sanphamgiachitiet,
        });
    }
}
