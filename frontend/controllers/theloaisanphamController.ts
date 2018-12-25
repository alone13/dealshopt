/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ITheLoaiSanPhamPageLogic } from "../pagelogics/theloaisanphamPageLogic";
import { theloaisanphamForm } from "../forms/theloaisanphamForms";

export class TheLoaiSanPhamController extends Controller {
    static $inject: string[] = ["TheLoaiSanPhamPageLogic"];

    private theloaisanphamPageLogic: ITheLoaiSanPhamPageLogic;

    constructor(
        theloaisanphamPageLogic: ITheLoaiSanPhamPageLogic
    ) {
        super();
        this.theloaisanphamPageLogic = theloaisanphamPageLogic;
    }

    @Method.get("/quanlytheloaisanpham/")
    @Method.post("/quanlytheloaisanpham/")
    public async theloai(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = theloaisanphamForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.theloaisanphamPageLogic.createTheLoaiSanPham({
                    ten: data.ten,
                    link: data.link,
                    trangthai: data.trangthai
                });
            }
            form = formResult.form;
        }


        let theloaisanphams = await this.theloaisanphamPageLogic.getTheLoaiSanPhams({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "theloai_sp" : "theloai", {
            title: "Quản Lý Thể Loại",
            form: form,
            theLoaisanphams: theloaisanphams ? theloaisanphams.results : null
        });
    }

    @Method.get("/quanlytheloaisanpham/:id/")
    @Method.post("/quanlytheloaisanpham/:id/")
    public async tinhthanhdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = theloaisanphamForm;
        let theloaisanphamId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.theloaisanphamPageLogic.updateTheLoaiSanPham(theloaisanphamId, {
                    ten: data.ten,
                    link: data.link,
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlytheloaisanpham/`);
            }
            form = formResult.form;
        }

        let theloaisanpham = await this.theloaisanphamPageLogic.getTheLoaiSanPham(theloaisanphamId);

        return res.namedView(req.isMobile() ? "theloai_sp" : "theloaidetail", {
            title: "Quản Lý Thể Loại - Sản Phẩm",
            form: form,
            theloaisanpham: theloaisanpham
        });
    }
}
