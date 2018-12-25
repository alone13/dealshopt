/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Admin } from "./models";

/* Api input parameters section */
export interface CreateAdminData {
    taikhoan_id: number;
}

export interface UpdateAdminParams {
    taikhoan_id?: number;
}


/* Api interface section */
export interface IAdminApi {
    getAdmins(params?: PagedApiRequest): Promise<ApiListResponse<Admin>>;
    getAdmin(adminId: number): Promise<Admin>;
    createAdmin(data: CreateAdminData): Promise<Admin>;
    updateAdmin(adminId: number, params: UpdateAdminParams): Promise<Admin>;
    deleteAdmin(adminId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class AdminApi extends ApiBase implements IAdminApi {
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

    public async getAdmins(params?: PagedApiRequest): Promise<ApiListResponse<Admin>> {
        const response = await this.get<ApiListResponse<Admin>>("/admin/admin/", params);
        return response.body!;
    }

    public async getAdmin(adminId: number): Promise<Admin> {
        const response = await this.get<Admin>(`/admin/admin/${adminId}/`);
        return response.body!;
    }

    public async createAdmin(data: CreateAdminData): Promise<Admin> {
        const response = await this.post<CreateAdminData, Admin>("/admin/admin/", data);
        return response.body!;
    }

    public async updateAdmin(adminId: number, params: UpdateAdminParams): Promise<Admin> {
        const response = await this.put<UpdateAdminParams, Admin>(`/admin/admin/${adminId}/`, params);
        return response.body!;
    }

    public async deleteAdmin(adminId: number): Promise<void> {
        await this.delete<any, void>(`/admin/admin/${adminId}/`);
    }
}
