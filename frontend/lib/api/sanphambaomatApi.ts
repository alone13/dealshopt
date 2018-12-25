/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { SanPhamBaoMat } from "./models";

/* Api input parameters section */
export interface CreateSanPhamBaoMatData {
    ten: string;
}

export interface UpdateSanPhamBaoMatParams {
    ten?: string;
}


/* Api interface section */
export interface ISanPhamBaoMatApi {
    getSanPhamBaoMats(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamBaoMat>>;
    getSanPhamBaoMat(sanphambaomatId: number): Promise<SanPhamBaoMat>;
    createSanPhamBaoMat(data: CreateSanPhamBaoMatData): Promise<SanPhamBaoMat>;
    updateSanPhamBaoMat(sanphambaomatId: number, params: UpdateSanPhamBaoMatParams): Promise<SanPhamBaoMat>;
    deleteSanPhamBaoMat(sanphambaomatId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class SanPhamBaoMatApi extends ApiBase implements ISanPhamBaoMatApi {
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

    public async getSanPhamBaoMats(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamBaoMat>> {
        const response = await this.get<ApiListResponse<SanPhamBaoMat>>("/sanpham/sanpham_baomat/", params);
        return response.body!;
    }

    public async getSanPhamBaoMat(sanphambaomatId: number): Promise<SanPhamBaoMat> {
        const response = await this.get<SanPhamBaoMat>(`/sanpham/sanpham_baomat/${sanphambaomatId}/`);
        return response.body!;
    }

    public async createSanPhamBaoMat(data: CreateSanPhamBaoMatData): Promise<SanPhamBaoMat> {
        const response = await this.post<CreateSanPhamBaoMatData, SanPhamBaoMat>("/sanpham/sanpham_baomat/", data);
        return response.body!;
    }

    public async updateSanPhamBaoMat(sanphambaomatId: number, params: UpdateSanPhamBaoMatParams): Promise<SanPhamBaoMat> {
        const response = await this.put<UpdateSanPhamBaoMatParams, SanPhamBaoMat>(`/sanpham/sanpham_baomat/${sanphambaomatId}/`, params);
        return response.body!;
    }

    public async deleteSanPhamBaoMat(sanphambaomatId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/sanpham_baomat/${sanphambaomatId}/`);
    }
}
