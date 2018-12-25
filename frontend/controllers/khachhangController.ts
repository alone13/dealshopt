/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IKhachHangPageLogic } from "../pagelogics/khachhangPageLogic";
import { khachhangForm } from "../forms/khachhangForms";

export class KhachHangController extends Controller {
    static $inject: string[] = ["KhachHangPageLogic"];

    private khachhangPageLogic: IKhachHangPageLogic;

    constructor(
        khachhangPageLogic: IKhachHangPageLogic
    ) {
        super();
        this.khachhangPageLogic = khachhangPageLogic;
    }

    @Method.get("/quanlykhachhang/")
    @Method.post("/quanlykhachhang/")
    public async khachhang(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = khachhangForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.khachhangPageLogic.createKhachHang({
                    tenkhachhang: data.tenkhachhang,
                    diachi: data.diachi,
                    email: data.email,
                    sdt: data.sdt
                });
            }
            form = formResult.form;
        }

        let khachhangs = await this.khachhangPageLogic.getKhachHangs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "khachhang_sp" : "khachhang", {
            title: "Quản Lý Khách Hàng",
            form: form,
            khachhangs: khachhangs ? khachhangs.results : null
        });
    }

    @Method.get("/quanlykhachhang/:id/")
    @Method.post("/quanlykhachhang/:id/")
    public async khachhangdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = khachhangForm;
        let khachhangId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.khachhangPageLogic.updateKhachHang(khachhangId, {
                    tenkhachhang: data.tenkhachhang,
                    diachi: data.diachi,
                    email: data.email,
                    sdt: data.sdt
                });
                return res.redirect(`/quanlykhachhang/`);
            }
            form = formResult.form;
        }

        let khachhang = await this.khachhangPageLogic.getKhachHang(khachhangId);

        return res.namedView(req.isMobile() ? "khachhang_sp" : "khachhangdetail", {
            title: "Quản Lý Khách Hàng",
            form: form,
            khachhang: khachhang
        });
    }
}
