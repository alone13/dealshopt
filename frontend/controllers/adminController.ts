/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ITaiKhoanPageLogic } from "../pagelogics/taikhoanPageLogic";
import { IAdminPageLogic } from "../pagelogics/adminPageLogic";
import { adminForm } from "../forms/adminForms";

export class AdminController extends Controller {
    static $inject: string[] = ["TaiKhoanPageLogic", "AdminPageLogic"];

    private adminPageLogic: IAdminPageLogic;
    private taikhoanPageLogic: ITaiKhoanPageLogic;

    constructor(
        taikhoanPageLogic: ITaiKhoanPageLogic,
        adminPageLogic: IAdminPageLogic
    ) {
        super();
        this.taikhoanPageLogic = taikhoanPageLogic;
        this.adminPageLogic = adminPageLogic;
    }

    @Method.get("/quanlyadmin/")
    @Method.post("/quanlyadmin/")
    public async admin(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = adminForm;
        if (req.method === "POST") {
            console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                //console.log("ten", data.ten);
                //console.log("trangthai", data.trangthai);
                await this.adminPageLogic.createAdmin({
                    taikhoan_id: data.taikhoan_id
                });
            }
            form = formResult.form;
        }

        let admins = await this.adminPageLogic.getAdmins({
            limit: 5,
            offset: 0
        });

        let taikhoans = await this.taikhoanPageLogic.getTaiKhoans({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "admin_sp" : "admin", {
            title: "Quản Lý Admin",
            form: form,
            taikhoans: taikhoans ? taikhoans.results : null,
            admins: admins ? admins.results : null
        });
    }

    @Method.get("/quanlyadmin/:id/")
    @Method.post("/quanlyadmin/:id/")
    public async admindetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = adminForm;
        let taikhoanId: number = parseInt(req.params.id, 10) || 0;
        let adminId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                //console.log("ten", data.ten);
                //console.log("trangthai", data.trangthai);
                await this.adminPageLogic.updateAdmin(adminId, {
                    taikhoan_id: data.taikhoan_id
                });
                return res.redirect(`/quanlyadmin/`);
            }
            form = formResult.form;
        }

        let taikhoan = await this.taikhoanPageLogic.getTaiKhoan(taikhoanId);

        let admin = await this.adminPageLogic.getAdmin(adminId);

        return res.namedView(req.isMobile() ? "admin_sp" : "admindetail", {
            title: "Quản Lý Admin",
            form: form,
            taikhoan: taikhoan,
            admin: admin
        });
    }
}
