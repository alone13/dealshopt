/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IModule_HoatDongPageLogic } from "../pagelogics/modulehdPageLogic";
import { IHoatDongPageLogic } from "../pagelogics/hoatdongPageLogic";
import { IModulePageLogic } from "../pagelogics/modulePageLogic";
import { modulehdForm } from "../forms/modulehdForms";

export class Module_HoatDongController extends Controller {
    static $inject: string[] = ["Module_HoatDongPageLogic", "HoatDongPageLogic", "ModulePageLogic"];

    private modulehdPageLogic: IModule_HoatDongPageLogic;
    private hoatdongPageLogic: IHoatDongPageLogic;
    private modulePageLogic: IModulePageLogic;

    constructor(
        modulehdPageLogic: IModule_HoatDongPageLogic,
        hoatdongPageLogic: IHoatDongPageLogic,
        modulePageLogic: IModulePageLogic
    ) {
        super();
        this.modulehdPageLogic = modulehdPageLogic;
        this.hoatdongPageLogic = hoatdongPageLogic;
        this.modulePageLogic = modulePageLogic;
    }

    @Method.get("/quanlymoduleaction/")
    @Method.post("/quanlymoduleaction/")
    public async modulehd(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = modulehdForm;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.modulehdPageLogic.createModule_HoatDong({
                    module_id: data.module_id,
                    hoatdong_id: data.hoatdong_id
                });
            }
            form = formResult.form;
        }

        let modulehds = await this.modulehdPageLogic.getModule_HoatDongs({
            limit: 5,
            offset: 0
        });

        let hoatdongs = await this.hoatdongPageLogic.getHoatDongs({
            limit: 5,
            offset: 0
        });

        let modules = await this.modulePageLogic.getModules({
            limit: 5,
            offset: 0
        });

        return res.namedView(req.isMobile() ? "modulehd_sp" : "modulehd", {
            title: "Quản Lý Module - Action",
            form: form,
            modulehds: modulehds ? modulehds.results : null,
            hoatdongs: hoatdongs ? hoatdongs.results : null,
            modules: modules ? modules.results : null
        });
    }

    @Method.get("/quanlymoduleaction/:id/")
    @Method.post("/quanlymoduleaction/:id/")
    public async modulehdetail(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {
        let form = modulehdForm;
        let modulehdId: number = parseInt(req.params.id, 10) || 0;
        let hoatdongId: number = parseInt(req.params.id, 10) || 0;
        let moduleId: number = parseInt(req.params.id, 10) || 0;
        if (req.method === "POST") {
            const formResult = await this.handleForm(req, form, true);
            if (formResult.success) {
                const data = formResult.data;
                await this.modulehdPageLogic.updateModule_HoatDong(modulehdId, {
                    module_id: data.module_id,
                    hoatdong_id: data.hoatdong_id
                });
                return res.redirect(`/quanlymoduleaction/`);
            }
            form = formResult.form;
        }

        let modulehd = await this.modulehdPageLogic.getModule_HoatDong(modulehdId);
        let hoatdong = await this.hoatdongPageLogic.getHoatDong(hoatdongId);
        let module1 = await this.modulePageLogic.getModule(moduleId);

        return res.namedView(req.isMobile() ? "modulehd_sp" : "modulehddetail", {
            title: "Quản Lý Module - Action",
            form: form,
            modulehd: modulehd,
            hoatdong: hoatdong,
            module1: module1
        });
    }
}
