/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ILuaChonSanPhamPageLogic } from "../pagelogics/luachonsanphamPageLogic";
import { ISanPhamPageLogic } from "../pagelogics/sanphamPageLogic";
import { luachonForm } from "../forms/luachonForms";

export class LuaChonSanPhamController extends Controller {
    static $inject: string[] = ["LuaChonSanPhamPageLogic", "SanPhamPageLogic"];

    private luachonsanphamPageLogic: ILuaChonSanPhamPageLogic;
    private sanphamPageLogic: ISanPhamPageLogic;

    constructor(
        luachonsanphamPageLogic: ILuaChonSanPhamPageLogic,
        sanphamPageLogic: ISanPhamPageLogic
    ) {
        super();
        this.luachonsanphamPageLogic = luachonsanphamPageLogic;
        this.sanphamPageLogic = sanphamPageLogic;
    }

    @Method.get("/quanlyluachonsanpham/")
    @Method.post("/quanlyluachonsanpham/")
    public async luachon(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = luachonForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.luachonsanphamPageLogic.createLuaChonSanPham({
                    sanpham_id: data.sanpham_id,
                    ten: data.ten
                });
            }
            form = formResult.form;
        }

        let luachonsanphams = await this.luachonsanphamPageLogic.getLuaChonSanPhams({
            limit: 5,
            offset: 0
        });

        let sanphams = await this.sanphamPageLogic.getSanPhams({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "luachon_sp" : "luachon", {
            title: "Quản Lý Lựa Chọn",
            form: form,
            luachonsanphams: luachonsanphams ? luachonsanphams.results : null
        });
    }

    @Method.get("/quanlyluachonsanpham/:id/")
    @Method.post("/quanlyluachonsanpham/:id/")
    public async luachondetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = luachonForm;
        let luachonId: number = parseInt(req.params.id, 10) || 0;
        let sanphamId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.luachonsanphamPageLogic.updateLuaChonSanPham(luachonId, {
                    sanpham_id: data.sanpham_id,
                    ten: data.ten
                });
                return res.redirect(`/quanlyluachonsanpham/`);
            }
            form = formResult.form;
        }

        let luachonsanpham = await this.luachonsanphamPageLogic.getLuaChonSanPham(luachonId);
        let sanpham = await this.sanphamPageLogic.getSanPham(sanphamId);

        return res.namedView(req.isMobile() ? "luachon_sp" : "luachondetail", {
            title: "Quản Lý Lựa Chọn",
            form: form,
            luachonsanpham: luachonsanpham,
            sanpham: sanpham
        });
    }
}
