/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IRoleApi, CreateRoleData, UpdateRoleParams } from "../lib/api/roleApi";
import { Role } from "../lib/api/models";

export interface IRolePageLogic {
    getRoles(request: PagedApiRequest): Promise<ApiListResponse<Role>>;
    createRole(data: CreateRoleData): Promise<Role>;
    getRole(roleId: number): Promise<Role>;
    updateRole(roleId: number, params: UpdateRoleParams): Promise<Role>;
    deleteRole(roleId: number): Promise<void>;
}

@Dependency.register()
export class RolePageLogic extends PageLogicBase implements IRolePageLogic {
    static $inject: string[] = ["RoleApi"];
    private roleApi: IRoleApi;
    constructor(
        roleApi: IRoleApi
    ) {
        super();
        this.roleApi = roleApi;
    }

    public async getRoles(request: PagedApiRequest): Promise<ApiListResponse<Role>> {
        const roles = await this.roleApi.getRoles(request);
        return roles;
    }

    public async createRole(data: CreateRoleData): Promise<Role> {
        const roles = await this.roleApi.createRole(data);
        return roles;
    }

    public async getRole(roleId: number): Promise<Role> {
        const role = await this.roleApi.getRole(roleId);
        return role;
    }

    public async updateRole(roleId: number, params: UpdateRoleParams): Promise<Role> {
        const role = await this.roleApi.updateRole(roleId, params);
        return role;
    }

    public async deleteRole(roleId: number): Promise<void> {
        const role = await this.roleApi.deleteRole(roleId);
        return role;
    }
}
