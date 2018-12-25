/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { SanPhamGia } from "./models";

/* Api input parameters section */
export interface CreateSanPhamGiaData {
    sanpham_id: number;
}

export interface UpdateSanPhamGiaParams {
    sanpham_id?: number;
}


/* Api interface section */
export interface ISanPhamGiaApi {
    getSanPhamGias(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamGia>>;
    getSanPhamGia(sanphamgiaId: number): Promise<SanPhamGia>;
    createSanPhamGia(data: CreateSanPhamGiaData): Promise<SanPhamGia>;
    updateSanPhamGia(sanphamgiaId: number, params: UpdateSanPhamGiaParams): Promise<SanPhamGia>;
    deleteSanPhamGia(sanphamgiaId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class SanPhamGiaApi extends ApiBase implements ISanPhamGiaApi {
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

    public async getSanPhamGias(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamGia>> {
        const response = await this.get<ApiListResponse<SanPhamGia>>("/sanpham/sanpham_gia/", params);
        return response.body!;
    }

    public async getSanPhamGia(sanphamgiaId: number): Promise<SanPhamGia> {
        const response = await this.get<SanPhamGia>(`/sanpham/sanpham_gia/${sanphamgiaId}/`);
        return response.body!;
    }

    public async createSanPhamGia(data: CreateSanPhamGiaData): Promise<SanPhamGia> {
        const response = await this.post<CreateSanPhamGiaData, SanPhamGia>("/sanpham/sanpham_gia/", data);
        return response.body!;
    }

    public async updateSanPhamGia(sanphamgiaId: number, params: UpdateSanPhamGiaParams): Promise<SanPhamGia> {
        const response = await this.put<UpdateSanPhamGiaParams, SanPhamGia>(`/sanpham/sanpham_gia/${sanphamgiaId}/`, params);
        return response.body!;
    }

    public async deleteSanPhamGia(sanphamgiaId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/sanpham_gia/${sanphamgiaId}/`);
    }
}
