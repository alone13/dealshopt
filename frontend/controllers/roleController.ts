/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IRolePageLogic } from "../pagelogics/rolePageLogic";
import { roleForm } from "../forms/roleForms";

export class RoleController extends Controller {
    static $inject: string[] = ["RolePageLogic"];

    private rolePageLogic: IRolePageLogic;

    constructor(
        rolePageLogic: IRolePageLogic
    ) {
        super();
        this.rolePageLogic = rolePageLogic;
    }

    @Method.get("/quanlyquyen/")
    @Method.post("/quanlyquyen/")
    public async role(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = roleForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.rolePageLogic.createRole({
                    ten: data.ten
                });
            }
            form = formResult.form;
        }

        let roles = await this.rolePageLogic.getRoles({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "role_sp" : "role", {
            title: "Quản Lý Role",
            form: form,
            roles: roles ? roles.results : null
        });
    }

    @Method.get("/quanlyquyen/:id/")
    @Method.post("/quanlyquyen/:id/")
    public async roledetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = roleForm;
        let roleId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.rolePageLogic.updateRole(roleId, {
                    ten: data.ten
                });
                return res.redirect(`/quanlyquyen/`);
            }
            form = formResult.form;
        }

        let role = await this.rolePageLogic.getRole(roleId);

        return res.namedView(req.isMobile() ? "role_sp" : "roledetail", {
            title: "Quản Lý Role",
            form: form,
            role: role
        });
    }
}
