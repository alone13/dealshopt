/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { DanhMuc } from "./models";

/* Api input parameters section */
export interface CreateDanhMucData {
    danhmuccha: number;
    tendanhmuc: string;
    trangthai: boolean;
    link: string;
}

export interface UpdateDanhMucParams {
    danhmuccha?: number;
    tendanhmuc?: string;
    trangthai?: boolean;
    link?: string;
}


/* Api interface section */
export interface IDanhMucApi {
    getDanhMucs(params?: PagedApiRequest): Promise<ApiListResponse<DanhMuc>>;
    getDanhMuc(danhmucId: number): Promise<DanhMuc>;
    createDanhMuc(data: CreateDanhMucData): Promise<DanhMuc>;
    updateDanhMuc(danhmucId: number, params: UpdateDanhMucParams): Promise<DanhMuc>;
    deleteDanhMuc(danhmucId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class DanhMucApi extends ApiBase implements IDanhMucApi {
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

    public async getDanhMucs(params?: PagedApiRequest): Promise<ApiListResponse<DanhMuc>> {
        const response = await this.get<ApiListResponse<DanhMuc>>("/danhmuc/danhmuc/", params);
        return response.body!;
    }

    public async getDanhMuc(danhmucId: number): Promise<DanhMuc> {
        const response = await this.get<DanhMuc>(`/danhmuc/danhmuc/${danhmucId}/`);
        return response.body!;
    }

    public async createDanhMuc(data: CreateDanhMucData): Promise<DanhMuc> {
        const response = await this.post<CreateDanhMucData, DanhMuc>("/danhmuc/danhmuc/", data);
        return response.body!;
    }

    public async updateDanhMuc(danhmucId: number, params: UpdateDanhMucParams): Promise<DanhMuc> {
        const response = await this.put<UpdateDanhMucParams, DanhMuc>(`/danhmuc/danhmuc/${danhmucId}/`, params);
        return response.body!;
    }

    public async deleteDanhMuc(danhmucId: number): Promise<void> {
        await this.delete<any, void>(`/danhmuc/danhmuc/${danhmucId}/`);
    }
}
