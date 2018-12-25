/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IHoatDongPageLogic } from "../pagelogics/hoatdongPageLogic";
import { hoatdongForm } from "../forms/hoatdongForms";

export class HoatDongController extends Controller {
    static $inject: string[] = ["HoatDongPageLogic"];

    private hoatdongPageLogic: IHoatDongPageLogic;

    constructor(
        hoatdongPageLogic: IHoatDongPageLogic
    ) {
        super();
        this.hoatdongPageLogic = hoatdongPageLogic;
    }

    @Method.get("/quanlyhoatdong/")
    @Method.post("/quanlyhoatdong/")
    public async hoatdong(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = hoatdongForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.hoatdongPageLogic.createHoatDong({
                    ten: data.ten
                });
            }
            form = formResult.form;
        }

        let hoatdongs = await this.hoatdongPageLogic.getHoatDongs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "hoatdong_sp" : "hoatdong", {
            title: "Quản Lý Hoạt Động",
            form: form,
            hoatdongs: hoatdongs ? hoatdongs.results : null
        });
    }

    @Method.get("/quanlyhoatdong/:id/")
    @Method.post("/quanlyhoatdong/:id/")
    public async hoatdongdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = hoatdongForm;
        let hoatdongId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.hoatdongPageLogic.updateHoatDong(hoatdongId, {
                    ten: data.ten
                });
                return res.redirect(`/quanlyhoatdong/`);
            }
            form = formResult.form;
        }

        let hoatdong = await this.hoatdongPageLogic.getHoatDong(hoatdongId);

        return res.namedView(req.isMobile() ? "hoatdong_sp" : "hoatdongdetail", {
            title: "Quản Lý Hoạt Động",
            form: form,
            hoatdong: hoatdong
        });
    }
}
