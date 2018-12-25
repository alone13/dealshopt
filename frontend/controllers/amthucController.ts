/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IAmThucPageLogic } from "../pagelogics/amthucPageLogic";
import { amthucForm } from "../forms/amthucForms";

export class AmThucController extends Controller {
    static $inject: string[] = ["AmThucPageLogic"];

    private amthucPageLogic: IAmThucPageLogic;

    constructor(
        amthucPageLogic: IAmThucPageLogic
    ) {
        super();
        this.amthucPageLogic = amthucPageLogic;
    }

    @Method.get("/quanlyamthuc/")
    @Method.post("/quanlyamthuc/")
    public async amthuc(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = amthucForm;
        if (req.method === "POST") {
            console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                console.log("ten", data.ten);
                console.log("trangthai", data.trangthai);
                await this.amthucPageLogic.createAmThuc({
                    ten: data.ten,
                    trangthai: data.trangthai
                });
            }
            form = formResult.form;
        }

        let amthucs = await this.amthucPageLogic.getAmThucs({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "amthuc_sp" : "amthuc", {
            title: "Quản Lý Ẩm Thực",
            form: form,
            amthucs: amthucs ? amthucs.results : null
        });
    }

    @Method.get("/quanlyamthuc/:id/")
    @Method.post("/quanlyamthuc/:id/")
    public async amthucdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = amthucForm;
        let amthucId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
          console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                console.log("ten", data.ten);
                console.log("trangthai", data.trangthai);
                await this.amthucPageLogic.updateAmThuc(amthucId,{
                    ten: data.ten,
                    trangthai: data.trangthai
                });
                return res.redirect(`/quanlyamthuc/`);
            }
            form = formResult.form;
        }

        let amthuc = await this.amthucPageLogic.getAmThuc(amthucId);

        return res.namedView(req.isMobile() ? "amthuc_sp" : "amthucdetail", {
            title: "Quản Lý Ẩm Thực",
            form: form,
            amthuc: amthuc
        });
    }
}
