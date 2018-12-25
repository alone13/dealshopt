/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IModuleApi, CreateModuleData, UpdateModuleParams } from "../lib/api/moduleApi";
import { Module } from "../lib/api/models";

export interface IModulePageLogic {
    getModules(request: PagedApiRequest): Promise<ApiListResponse<Module>>;
    createModule(data: CreateModuleData): Promise<Module>;
    getModule(moduleId: number): Promise<Module>;
    updateModule(moduleId: number, params: UpdateModuleParams): Promise<Module>;
    deleteModule(moduleId: number): Promise<void>;
}

@Dependency.register()
export class ModulePageLogic extends PageLogicBase implements IModulePageLogic {
    static $inject: string[] = ["ModuleApi"];
    private moduleApi: IModuleApi;
    constructor(
        moduleApi: IModuleApi
    ) {
        super();
        this.moduleApi = moduleApi;
    }

    public async getModules(request: PagedApiRequest): Promise<ApiListResponse<Module>> {
        const modules = await this.moduleApi.getModules(request);
        return modules;
    }

    public async createModule(data: CreateModuleData): Promise<Module> {
        const modules = await this.moduleApi.createModule(data);
        return modules;
    }

    public async getModule(moduleId: number): Promise<Module> {
        const module1 = await this.moduleApi.getModule(moduleId);
        return module1;
    }

    public async updateModule(moduleId: number, params: UpdateModuleParams): Promise<Module> {
        const module1 = await this.moduleApi.updateModule(moduleId, params);
        return module1;
    }

    public async deleteModule(moduleId: number): Promise<void> {
        const module1 = await this.moduleApi.deleteModule(moduleId);
        return module1;
    }
}
