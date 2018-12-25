/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { SanPham } from "./models";

/* Api input parameters section */
export interface CreateSanPhamData {
    user_cuahang_id: number;
    theloai_id: number;
    danhmuc_id: number;
    baomat_id: number;
    trangthai_id: number;
    amthuc_id: number;
    tinhthanh_id: number;
    quanhuyen_id: number;
    tensanpham: string;
    hinhanh: string;
    ngaydang: string;
    soluong: number;
}

export interface UpdateSanPhamParams {
    user_cuahang_id?: number;
    theloai_id?: number;
    danhmuc_id?: number;
    baomat_id?: number;
    trangthai_id?: number;
    amthuc_id?: number;
    tinhthanh_id?: number;
    quanhuyen_id?: number;
    tensanpham?: string;
    hinhanh?: string;
    ngaydang?: string;
    soluong?: number;
}


/* Api interface section */
export interface ISanPhamApi {
    getSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<SanPham>>;
    getSanPham(sanphamId: number): Promise<SanPham>;
    createSanPham(data: CreateSanPhamData): Promise<SanPham>;
    updateSanPham(sanphamId: number, params: UpdateSanPhamParams): Promise<SanPham>;
    deleteSanPham(sanphamId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class SanPhamApi extends ApiBase implements ISanPhamApi {
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

    public async getSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<SanPham>> {
        const response = await this.get<ApiListResponse<SanPham>>("/sanpham/sanpham/", params);
        return response.body!;
    }

    public async getSanPham(sanphamId: number): Promise<SanPham> {
        const response = await this.get<SanPham>(`/sanpham/sanpham/${sanphamId}/`);
        return response.body!;
    }

    public async createSanPham(data: CreateSanPhamData): Promise<SanPham> {
        const response = await this.post<CreateSanPhamData, SanPham>("/sanpham/sanpham/", data);
        return response.body!;
    }

    public async updateSanPham(sanphamId: number, params: UpdateSanPhamParams): Promise<SanPham> {
        const response = await this.put<UpdateSanPhamParams, SanPham>(`/sanpham/sanpham/${sanphamId}/`, params);
        return response.body!;
    }

    public async deleteSanPham(sanphamId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/sanpham/${sanphamId}/`);
    }
}
