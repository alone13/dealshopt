/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IQuanHuyenPageLogic } from "../pagelogics/quanhuyenPageLogic";
import { ITinhThanhPageLogic } from "../pagelogics/tinhthanhPageLogic";
import { quanhuyenForm } from "../forms/quanhuyenForms";

export class QuanHuyenController extends Controller {
    static $inject: string[] = ["QuanHuyenPageLogic", "TinhThanhPageLogic"];

    private quanhuyenPageLogic: IQuanHuyenPageLogic;
    private tinhthanhPageLogic: ITinhThanhPageLogic;

    constructor(
        quanhuyenPageLogic: IQuanHuyenPageLogic,
        tinhthanhPageLogic: ITinhThanhPageLogic
    ) {
        super();
        this.quanhuyenPageLogic = quanhuyenPageLogic;
        this.tinhthanhPageLogic = tinhthanhPageLogic;
    }

    @Method.get("/quanlyquanhuyen/")
    @Method.post("/quanlyquanhuyen/")
    public async quanhuyen(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = quanhuyenForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                await this.quanhuyenPageLogic.createQuanHuyen({
                    tinh_id: data.tinh_id,
                    ten: data.ten,
                    trangthai: data.trangthai
                });
            }
            form = formResult.form;
        }

        let quanhuyens = await this.quanhuyenPageLogic.getQuanHuyens({
            limit: 5,
            offset: 0
        });

        let tinhthanhs = await this.tinhthanhPageLogic.getTinhThanhs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "quanhuyen_sp" : "quanhuyen", {
            title: "Quản Lý Quận Huyện",
            form: form,
            quanhuyens: quanhuyens ? quanhuyens.results : null,
            tinhthanhs: tinhthanhs ? tinhthanhs.results : null
        });
    }

    @Method.get("/quanlyquanhuyen/:id/")
    @Method.post("/quanlyquanhuyen/:id/")
    public async quanhuyendetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = quanhuyenForm;
        let quanhuyenId: number = parseInt(req.params.id, 10) || 0;
        let tinhthanhId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.quanhuyenPageLogic.updateQuanHuyen(quanhuyenId, {
                    tinh_id: data.tinh_id,
                    ten: data.ten,
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlyquanhuyen/`);
            }
            form = formResult.form;
        }

        let quanhuyen = await this.quanhuyenPageLogic.getQuanHuyen(quanhuyenId);
        let tinhthanh = await this.tinhthanhPageLogic.getTinhThanh(tinhthanhId);

        return res.namedView(req.isMobile() ? "quanhuyen_sp" : "quanhuyendetail", {
            title: "Quản Lý Quận Huyện",
            form: form,
            quanhuyen: quanhuyen,
            tinhthanh: tinhthanh
        });
    }
}
