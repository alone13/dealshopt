/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IRole_ModuleApi, CreateRole_ModuleData, UpdateRole_ModuleParams } from "../lib/api/rolemoduleApi";
import { Role_Module } from "../lib/api/models";

export interface IRole_ModulePageLogic {
    getRole_Modules(request: PagedApiRequest): Promise<ApiListResponse<Role_Module>>;
    createRole_Module(data: CreateRole_ModuleData): Promise<Role_Module>;
    getRole_Module(role_moduleId: number): Promise<Role_Module>;
    updateRole_Module(role_moduleId: number, params: UpdateRole_ModuleParams): Promise<Role_Module>;
    deleteRole_Module(role_moduleId: number): Promise<void>;
}

@Dependency.register()
export class Role_ModulePageLogic extends PageLogicBase implements IRole_ModulePageLogic {
    static $inject: string[] = ["Role_ModuleApi"];
    private role_moduleApi: IRole_ModuleApi;
    constructor(
        role_moduleApi: IRole_ModuleApi
    ) {
        super();
        this.role_moduleApi = role_moduleApi;
    }

    public async getRole_Modules(request: PagedApiRequest): Promise<ApiListResponse<Role_Module>> {
        const role_modules = await this.role_moduleApi.getRole_Modules(request);
        return role_modules;
    }

    public async createRole_Module(data: CreateRole_ModuleData): Promise<Role_Module> {
        const role_modules = await this.role_moduleApi.createRole_Module(data);
        return role_modules;
    }

    public async getRole_Module(role_moduleId: number): Promise<Role_Module> {
        const role_module = await this.role_moduleApi.getRole_Module(role_moduleId);
        return role_module;
    }

    public async updateRole_Module(role_moduleId: number, params: UpdateRole_ModuleParams): Promise<Role_Module> {
        const role_module = await this.role_moduleApi.updateRole_Module(role_moduleId, params);
        return role_module;
    }

    public async deleteRole_Module(role_moduleId: number): Promise<void> {
        const role_module = await this.role_moduleApi.deleteRole_Module(role_moduleId);
        return role_module;
    }
}
