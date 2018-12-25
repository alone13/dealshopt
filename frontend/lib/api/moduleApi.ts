/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Module } from "./models";

/* Api input parameters section */
export interface CreateModuleData {
    ten: string;
}

export interface UpdateModuleParams {
    ten?: string;
}


/* Api interface section */
export interface IModuleApi {
    getModules(params?: PagedApiRequest): Promise<ApiListResponse<Module>>;
    getModule(moduleId: number): Promise<Module>;
    createModule(data: CreateModuleData): Promise<Module>;
    updateModule(moduleId: number, params: UpdateModuleParams): Promise<Module>;
    deleteModule(moduleId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class ModuleApi extends ApiBase implements IModuleApi {
    static $inject: string[] = ["InfrastructureSettings", "RequestId"];
    constructor(
        infrastructureSettings: IInfrastructureSettings,
        requestId: string
    ) {
        super(
            infrastructureSettings.endpoints.apps,
            requestId
        );
    }

    public async getModules(params?: PagedApiRequest): Promise<ApiListResponse<Module>> {
        const response = await this.get<ApiListResponse<Module>>("/admin/module/", params);
        return response.body!;
    }

    public async getModule(moduleId: number): Promise<Module> {
        const response = await this.get<Module>(`/admin/module/${moduleId}/`);
        return response.body!;
    }

    public async createModule(data: CreateModuleData): Promise<Module> {
        const response = await this.post<CreateModuleData, Module>("/admin/module/", data);
        return response.body!;
    }

    public async updateModule(moduleId: number, params: UpdateModuleParams): Promise<Module> {
        const response = await this.put<UpdateModuleParams, Module>(`/admin/module/${moduleId}/`, params);
        return response.body!;
    }

    public async deleteModule(moduleId: number): Promise<void> {
        await this.delete<any, void>(`/admin/module/${moduleId}/`);
    }
}
