/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { ITaiKhoanPageLogic } from "../pagelogics/taikhoanPageLogic";
import { IRolePageLogic } from "../pagelogics/rolePageLogic";
import { taikhoanForm } from "../forms/taikhoanForms";

export class TaiKhoanController extends Controller {
    static $inject: string[] = ["TaiKhoanPageLogic", "RolePageLogic"];

    private rolePageLogic: IRolePageLogic;
    private taikhoanPageLogic: ITaiKhoanPageLogic;

    constructor(
        taikhoanPageLogic: ITaiKhoanPageLogic,
        rolePageLogic: IRolePageLogic
    ) {
        super();
        this.taikhoanPageLogic = taikhoanPageLogic;
        this.rolePageLogic = rolePageLogic;
    }

    @Method.get("/quanlytaikhoan/")
    @Method.post("/quanlytaikhoan/")
    public async taikhoan(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = taikhoanForm;
        if (req.method === "POST") {
            console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                // let attachment = req.file;
                //console.log("ten", data.ten);
                //console.log("trangthai", data.trangthai);
                await this.taikhoanPageLogic.createTaiKhoan({
                    tendangnhap: data.tendangnhap,
                    matkhau: data.matkhau,
                    role_id: data.role_id
                });
            }
            form = formResult.form;
        }

        let taikhoans = await this.taikhoanPageLogic.getTaiKhoans({
            limit: 5,
            offset: 0
        });

        let roles = await this.rolePageLogic.getRoles({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "taikhoan_sp" : "taikhoan", {
            title: "Quản Lý Tài Khoản",
            form: form,
            taikhoans: taikhoans ? taikhoans.results : null,
            roles: roles ? roles.results : null
        });
    }

    @Method.get("/quanlytaikhoan/:id/")
    @Method.post("/quanlytaikhoan/:id/")
    public async taikhoandetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = taikhoanForm;
        let taikhoanId: number = parseInt(req.params.id, 10) || 0;
        let roleId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            console.log("vao");
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                //console.log("ten", data.ten);
                //console.log("trangthai", data.trangthai);
                await this.taikhoanPageLogic.updateTaiKhoan(taikhoanId, {
                    tendangnhap: data.tendangnhap,
                    matkhau: data.matkhau,
                    role_id: data.role_id
                });
                return res.redirect(`/quanlytaikhoan/`);
            }
            form = formResult.form;
        }

        let taikhoan = await this.taikhoanPageLogic.getTaiKhoan(taikhoanId);

        let role = await this.rolePageLogic.getRole(roleId);

        return res.namedView(req.isMobile() ? "amthuc_sp" : "amthucdetail", {
            title: "Quản Lý Tài Khoản",
            form: form,
            taikhoan: taikhoan,
            role: role
        });
    }
}
