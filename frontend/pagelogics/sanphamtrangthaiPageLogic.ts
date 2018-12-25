/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ISanPhamTrangThaiApi, CreateSanPhamTrangThaiData, UpdateSanPhamTrangThaiParams } from "../lib/api/sanphamtrangthaiApi";
import { SanPhamTrangThai } from "../lib/api/models";

export interface ISanPhamTrangThaiPageLogic {
    getSanPhamTrangThais(request: PagedApiRequest): Promise<ApiListResponse<SanPhamTrangThai>>;
    createSanPhamTrangThai(data: CreateSanPhamTrangThaiData): Promise<SanPhamTrangThai>;
    getSanPhamTrangThai(sanphamtrangthaiId: number): Promise<SanPhamTrangThai>;
    updateSanPhamTrangThai(sanphamtrangthaiId: number, params: UpdateSanPhamTrangThaiParams): Promise<SanPhamTrangThai>;
    deleteSanPhamTrangThai(sanphamtrangthaiId: number): Promise<void>;
}

@Dependency.register()
export class SanPhamTrangThaiPageLogic extends PageLogicBase implements ISanPhamTrangThaiPageLogic {
    static $inject: string[] = ["SanPhamTrangThaiApi"];
    private sanphamtrangthaiApi: ISanPhamTrangThaiApi;
    constructor(
        sanphamtrangthaiApi: ISanPhamTrangThaiApi
    ) {
        super();
        this.sanphamtrangthaiApi = sanphamtrangthaiApi;
    }

    public async getSanPhamTrangThais(request: PagedApiRequest): Promise<ApiListResponse<SanPhamTrangThai>> {
        const sanphamtrangthais = await this.sanphamtrangthaiApi.getSanPhamTrangThais(request);
        return sanphamtrangthais;
    }

    public async createSanPhamTrangThai(data: CreateSanPhamTrangThaiData): Promise<SanPhamTrangThai> {
        const sanphamtrangthais = await this.sanphamtrangthaiApi.createSanPhamTrangThai(data);
        return sanphamtrangthais;
    }

    public async getSanPhamTrangThai(sanphamtrangthaiId: number): Promise<SanPhamTrangThai> {
        const sanphamtrangthai = await this.sanphamtrangthaiApi.getSanPhamTrangThai(sanphamtrangthaiId);
        return sanphamtrangthai;
    }

    public async updateSanPhamTrangThai(sanphamtrangthaiId: number, params: UpdateSanPhamTrangThaiParams): Promise<SanPhamTrangThai> {
        const sanphamtrangthai = await this.sanphamtrangthaiApi.updateSanPhamTrangThai(sanphamtrangthaiId, params);
        return sanphamtrangthai;
    }

    public async deleteSanPhamTrangThai(sanphamtrangthaiId: number): Promise<void> {
        const sanphamtrangthai = await this.sanphamtrangthaiApi.deleteSanPhamTrangThai(sanphamtrangthaiId);
        return sanphamtrangthai;
    }
}
