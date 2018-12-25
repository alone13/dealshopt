/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { TinTuc } from "./models";

/* Api input parameters section */
export interface CreateTinTucData {
    danhmuc_id: number;
    tieude: string;
    hinhanh: string;
    mota: string;
    noidung: string;
    ngaydang: string;
    trangthai: boolean;
}

export interface UpdateTinTucParams {
    danhmuc_id?: number;
    tieude?: string;
    hinhanh?: string;
    mota?: string;
    noidung?: string;
    ngaydang?: string;
    trangthai?: boolean;
}


/* Api interface section */
export interface ITinTucApi {
    getTinTucs(params?: PagedApiRequest): Promise<ApiListResponse<TinTuc>>;
    getTinTuc(tintucId: number): Promise<TinTuc>;
    createTinTuc(data: CreateTinTucData): Promise<TinTuc>;
    updateTinTuc(tintucId: number, params: UpdateTinTucParams): Promise<TinTuc>;
    deleteTinTuc(tintucId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class TinTucApi extends ApiBase implements ITinTucApi {
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

    public async getTinTucs(params?: PagedApiRequest): Promise<ApiListResponse<TinTuc>> {
        const response = await this.get<ApiListResponse<TinTuc>>("/tintuc/tintuc/", params);
        return response.body!;
    }

    public async getTinTuc(tintucId: number): Promise<TinTuc> {
        const response = await this.get<TinTuc>(`/tintuc/tintuc/${tintucId}/`);
        return response.body!;
    }

    public async createTinTuc(data: CreateTinTucData): Promise<TinTuc> {
        const response = await this.post<CreateTinTucData, TinTuc>("/tintuc/tintuc/", data);
        return response.body!;
    }

    public async updateTinTuc(tintucId: number, params: UpdateTinTucParams): Promise<TinTuc> {
        const response = await this.put<UpdateTinTucParams, TinTuc>(`/tintuc/tintuc/${tintucId}/`, params);
        return response.body!;
    }

    public async deleteTinTuc(tintucId: number): Promise<void> {
        await this.delete<any, void>(`/tintuc/tintuc/${tintucId}/`);
    }
}
