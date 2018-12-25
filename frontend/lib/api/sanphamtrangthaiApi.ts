/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { SanPhamTrangThai } from "./models";

/* Api input parameters section */
export interface CreateSanPhamTrangThaiData {
    trangthai: boolean;
}

export interface UpdateSanPhamTrangThaiParams {
    trangthai?: boolean;
}


/* Api interface section */
export interface ISanPhamTrangThaiApi {
    getSanPhamTrangThais(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamTrangThai>>;
    getSanPhamTrangThai(sanphamtrangthaiId: number): Promise<SanPhamTrangThai>;
    createSanPhamTrangThai(data: CreateSanPhamTrangThaiData): Promise<SanPhamTrangThai>;
    updateSanPhamTrangThai(sanphamtrangthaiId: number, params: UpdateSanPhamTrangThaiParams): Promise<SanPhamTrangThai>;
    deleteSanPhamTrangThai(sanphamtrangthaiId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class SanPhamTrangThaiApi extends ApiBase implements ISanPhamTrangThaiApi {
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

    public async getSanPhamTrangThais(params?: PagedApiRequest): Promise<ApiListResponse<SanPhamTrangThai>> {
        const response = await this.get<ApiListResponse<SanPhamTrangThai>>("/sanpham/sanpham_trangthai/", params);
        return response.body!;
    }

    public async getSanPhamTrangThai(sanphamtrangthaiId: number): Promise<SanPhamTrangThai> {
        const response = await this.get<SanPhamTrangThai>(`/sanpham/sanpham_trangthai/${sanphamtrangthaiId}/`);
        return response.body!;
    }

    public async createSanPhamTrangThai(data: CreateSanPhamTrangThaiData): Promise<SanPhamTrangThai> {
        const response = await this.post<CreateSanPhamTrangThaiData, SanPhamTrangThai>("/sanpham/sanpham_trangthai/", data);
        return response.body!;
    }

    public async updateSanPhamTrangThai(sanphamtrangthaiId: number, params: UpdateSanPhamTrangThaiParams): Promise<SanPhamTrangThai> {
        const response = await this.put<UpdateSanPhamTrangThaiParams, SanPhamTrangThai>(`/sanpham/sanpham_trangthai/${sanphamtrangthaiId}/`, params);
        return response.body!;
    }

    public async deleteSanPhamTrangThai(sanphamtrangthaiId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/sanpham_trangthai/${sanphamtrangthaiId}/`);
    }
}
