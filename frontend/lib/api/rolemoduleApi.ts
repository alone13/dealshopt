/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Role_Module } from "./models";

/* Api input parameters section */
export interface CreateRole_ModuleData {
    module_id: number;
    role_id: number;
}

export interface UpdateRole_ModuleParams {
    module_id?: number;
    role_id?: number;
}


/* Api interface section */
export interface IRole_ModuleApi {
    getRole_Modules(params?: PagedApiRequest): Promise<ApiListResponse<Role_Module>>;
    getRole_Module(role_moduleId: number): Promise<Role_Module>;
    createRole_Module(data: CreateRole_ModuleData): Promise<Role_Module>;
    updateRole_Module(role_moduleId: number, params: UpdateRole_ModuleParams): Promise<Role_Module>;
    deleteRole_Module(role_moduleId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class Role_ModuleApi extends ApiBase implements IRole_ModuleApi {
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

    public async getRole_Modules(params?: PagedApiRequest): Promise<ApiListResponse<Role_Module>> {
        const response = await this.get<ApiListResponse<Role_Module>>("/admin/permission/", params);
        return response.body!;
    }

    public async getRole_Module(role_moduleId: number): Promise<Role_Module> {
        const response = await this.get<Role_Module>(`/admin/permission/${role_moduleId}/`);
        return response.body!;
    }

    public async createRole_Module(data: CreateRole_ModuleData): Promise<Role_Module> {
        const response = await this.post<CreateRole_ModuleData, Role_Module>("/admin/permission/", data);
        return response.body!;
    }

    public async updateRole_Module(role_moduleId: number, params: UpdateRole_ModuleParams): Promise<Role_Module> {
        const response = await this.put<UpdateRole_ModuleParams, Role_Module>(`/admin/permission/${role_moduleId}/`, params);
        return response.body!;
    }

    public async deleteRole_Module(role_moduleId: number): Promise<void> {
        await this.delete<any, void>(`/admin/permission/${role_moduleId}/`);
    }
}
