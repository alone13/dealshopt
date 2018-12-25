/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IAdminApi, CreateAdminData, UpdateAdminParams } from "../lib/api/adminApi";
import { Admin } from "../lib/api/models";

export interface IAdminPageLogic {
    getAdmins(request: PagedApiRequest): Promise<ApiListResponse<Admin>>;
    createAdmin(data: CreateAdminData): Promise<Admin>;
    getAdmin(adminId: number): Promise<Admin>;
    updateAdmin(adminId: number, params: UpdateAdminParams): Promise<Admin>;
    deleteAdmin(adminId: number): Promise<void>;
}

@Dependency.register()
export class AdminPageLogic extends PageLogicBase implements IAdminPageLogic {
    static $inject: string[] = ["AdminApi",];
    private adminApi: IAdminApi;
    constructor(
        adminApi: IAdminApi
    ) {
        super();
        this.adminApi = adminApi;
    }

    public async getAdmins(request: PagedApiRequest): Promise<ApiListResponse<Admin>> {
        const admins = await this.adminApi.getAdmins(request);
        return admins;
    }

    public async createAdmin(data: CreateAdminData): Promise<Admin> {
        const admins = await this.adminApi.createAdmin(data);
        return admins;
    }

    public async getAdmin(adminId: number): Promise<Admin> {
        const admin = await this.adminApi.getAdmin(adminId);
        return admin;
    }

    public async updateAdmin(adminId: number, params: UpdateAdminParams): Promise<Admin> {
        const admin = await this.adminApi.updateAdmin(adminId, params);
        return admin;
    }

    public async deleteAdmin(adminId: number): Promise<void> {
        const admin = await this.adminApi.deleteAdmin(adminId);
        return admin;
    }
}
