/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { SanPhamGiaChiTiet } from "./models";

/* Api input parameters section */
export interface CreateSanPhamGiaChiTietData {
    sanpham_gia_id: number;
    gia: string;
    ngaybd: string;
    ngaykt: string;
    is_active: boolean;
}

export interface UpdateSanPhamGiaChiTietParams {
    sanpham_gia_id?: number;
    gia: string;
    ngaybd: string;
    ngaykt: string;
    is_active: boolean;
}


/* Api interface section */
export interface ISanPhamGiaChiTietApi {
    getSanPhamGiaChiTiets(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamGiaChiTiet>>;
    getSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<SanPhamGiaChiTiet>;
    createSanPhamGiaChiTiet(data: CreateSanPhamGiaChiTietData): Promise<SanPhamGiaChiTiet>;
    updateSanPhamGiaChiTiet(sanphamgiachitietId: number, params: UpdateSanPhamGiaChiTietParams): Promise<SanPhamGiaChiTiet>;
    deleteSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class SanPhamGiaChiTietApi extends ApiBase implements ISanPhamGiaChiTietApi {
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

    public async getSanPhamGiaChiTiets(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamGiaChiTiet>> {
        const response = await this.get<ApiListResponse<SanPhamGiaChiTiet>>("/sanpham/sanpham_gia_chitiet/", params);
        return response.body!;
    }

    public async getSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<SanPhamGiaChiTiet> {
        const response = await this.get<SanPhamGiaChiTiet>(`/sanpham/sanpham_gia_chitiet/${sanphamgiachitietId}/`);
        return response.body!;
    }

    public async createSanPhamGiaChiTiet(data: CreateSanPhamGiaChiTietData): Promise<SanPhamGiaChiTiet> {
        const response = await this.post<CreateSanPhamGiaChiTietData, SanPhamGiaChiTiet>("/sanpham/sanpham_gia_chitiet/", data);
        return response.body!;
    }

    public async updateSanPhamGiaChiTiet(sanphamgiachitietId: number, params: UpdateSanPhamGiaChiTietParams): Promise<SanPhamGiaChiTiet> {
        const response = await this.put<UpdateSanPhamGiaChiTietParams, SanPhamGiaChiTiet>(`/sanpham/sanpham_gia_chitiet/${sanphamgiachitietId}/`, params);
        return response.body!;
    }

    public async deleteSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/sanpham_gia_chitiet/${sanphamgiachitietId}/`);
    }
}
