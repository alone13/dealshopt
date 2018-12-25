/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Role } from "./models";

/* Api input parameters section */
export interface CreateRoleData {
    ten: string;
}

export interface UpdateRoleParams {
    ten?: string;
}


/* Api interface section */
export interface IRoleApi {
    getRoles(params?: PagedApiRequest): Promise<ApiListResponse<Role>>;
    getRole(roleId: number): Promise<Role>;
    createRole(data: CreateRoleData): Promise<Role>;
    updateRole(roleId: number, params: UpdateRoleParams): Promise<Role>;
    deleteRole(roleId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class RoleApi extends ApiBase implements IRoleApi {
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

    public async getRoles(params?: PagedApiRequest): Promise<ApiListResponse<Role>> {
        const response = await this.get<ApiListResponse<Role>>("/admin/role/", params);
        return response.body!;
    }

    public async getRole(roleId: number): Promise<Role> {
        const response = await this.get<Role>(`/admin/role/${roleId}/`);
        return response.body!;
    }

    public async createRole(data: CreateRoleData): Promise<Role> {
        const response = await this.post<CreateRoleData, Role>("/admin/role/", data);
        return response.body!;
    }

    public async updateRole(roleId: number, params: UpdateRoleParams): Promise<Role> {
        const response = await this.put<UpdateRoleParams, Role>(`/admin/role/${roleId}/`, params);
        return response.body!;
    }

    public async deleteRole(roleId: number): Promise<void> {
        await this.delete<any, void>(`/admin/role/${roleId}/`);
    }
}
