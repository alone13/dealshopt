/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IRole_ModulePageLogic } from "../pagelogics/rolemodulePageLogic";
import { IRolePageLogic } from "../pagelogics/rolePageLogic";
import { IModulePageLogic } from "../pagelogics/modulePageLogic";
import { role_moduleForm } from "../forms/rolemoduleForms";

export class Role_ModuleController extends Controller {
    static $inject: string[] = ["Role_ModulePageLogic", "RolePageLogic", "ModulePageLogic"];

    private rolemodulePageLogic: IRole_ModulePageLogic;
    private rolePageLogic: IRolePageLogic;
    private modulePageLogic: IModulePageLogic;

    constructor(
        rolemodulePageLogic: IRole_ModulePageLogic,
        rolePageLogic: IRolePageLogic,
        modulePageLogic: IModulePageLogic
    ) {
        super();
        this.rolemodulePageLogic = rolemodulePageLogic;
        this.rolePageLogic = rolePageLogic;
        this.modulePageLogic = modulePageLogic;
    }

    @Method.get("/quanlypermission/")
    @Method.post("/quanlypermission/")
    public async permission(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = role_moduleForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.rolemodulePageLogic.createRole_Module({
                    module_id: data.module_id,
                    role_id: data.role_id
                });
            }
            form = formResult.form;
        }

        let role_modules = await this.rolemodulePageLogic.getRole_Modules({
            limit: 5,
            offset: 0
        });

        let roles = await this.rolePageLogic.getRoles({
            limit: 5,
            offset: 0
        });

        let modules = await this.modulePageLogic.getModules({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "permission_sp" : "permission", {
            title: "Quản Lý Role - Module",
            form: form,
            role_modules: role_modules ? role_modules.results : null,
            roles: roles ? roles.results : null,
            modules: modules ? modules.results : null
        });
    }

    @Method.get("/quanlypermission/:id/")
    @Method.post("/quanlypermission/:id/")
    public async permissiondetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = role_moduleForm;
        let role_moduleId: number = parseInt(req.params.id, 10) || 0;
        let roleId: number = parseInt(req.params.id, 10) || 0;
        let moduleId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.rolemodulePageLogic.updateRole_Module(role_moduleId, {
                    module_id: data.module_id,
                    role_id: data.role_id
                });
                return res.redirect(`/quanlypermission/`);
            }
            form = formResult.form;
        }

        let role_module = await this.rolemodulePageLogic.getRole_Module(role_moduleId);
        let role = await this.rolePageLogic.getRole(roleId);
        let module1 = await this.modulePageLogic.getModule(moduleId);

        return res.namedView(req.isMobile() ? "permission_sp" : "permissiondetail", {
            title: "Quản Lý Role - Module",
            form: form,
            role_module: role_module,
            role: role,
            module1: module1
        });
    }
}
