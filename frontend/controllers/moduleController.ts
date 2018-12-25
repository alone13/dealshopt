/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IModulePageLogic } from "../pagelogics/modulePageLogic";
import { moduleForm } from "../forms/moduleForms";

export class ModuleController extends Controller {
    static $inject: string[] = ["ModulePageLogic"];

    private modulePageLogic: IModulePageLogic;

    constructor(
        modulePageLogic: IModulePageLogic
    ) {
        super();
        this.modulePageLogic = modulePageLogic;
    }

    @Method.get("/quanlymodule/")
    @Method.post("/quanlymodule/")
    public async module(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = moduleForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.modulePageLogic.createModule({
                    ten: data.ten
                });
            }
            form = formResult.form;
        }

        let modules = await this.modulePageLogic.getModules({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "module_sp" : "module", {
            title: "Quản Lý Module",
            form: form,
            modules: modules ? modules.results : null
        });
    }

    @Method.get("/quanlymodule/:id/")
    @Method.post("/quanlymodule/:id/")
    public async moduledetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = moduleForm;
        let moduleId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.modulePageLogic.updateModule(moduleId, {
                    ten: data.ten
                });
                return res.redirect(`/quanlymodule/`);
            }
            form = formResult.form;
        }

        let module1 = await this.modulePageLogic.getModule(moduleId);

        return res.namedView(req.isMobile() ? "module_sp" : "moduledetail", {
            title: "Quản Lý Module",
            form: form,
            module1: module1
        });
    }
}
