/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ISanPhamGiaApi, CreateSanPhamGiaData, UpdateSanPhamGiaParams } from "../lib/api/sanphamgiaApi";
import { SanPhamGia } from "../lib/api/models";

export interface ISanPhamGiaPageLogic {
    getSanPhamGias(request: PagedApiRequest): Promise<ApiListResponse<SanPhamGia>>;
    createSanPhamGia(data: CreateSanPhamGiaData): Promise<SanPhamGia>;
    getSanPhamGia(sanphamgiaId: number): Promise<SanPhamGia>;
    updateSanPhamGia(sanphamgiaId: number, params: UpdateSanPhamGiaParams): Promise<SanPhamGia>;
    deleteSanPhamGia(sanphamgiaId: number): Promise<void>;
}

@Dependency.register()
export class SanPhamGiaPageLogic extends PageLogicBase implements ISanPhamGiaPageLogic {
    static $inject: string[] = ["SanPhamGiaApi"];
    private sanphamgiaApi: ISanPhamGiaApi;
    constructor(
        sanphamgiaApi: ISanPhamGiaApi
    ) {
        super();
        this.sanphamgiaApi = sanphamgiaApi;
    }

    public async getSanPhamGias(request: PagedApiRequest): Promise<ApiListResponse<SanPhamGia>> {
        const sanphamgias = await this.sanphamgiaApi.getSanPhamGias(request);
        return sanphamgias;
    }

    public async createSanPhamGia(data: CreateSanPhamGiaData): Promise<SanPhamGia> {
        const sanphamgias = await this.sanphamgiaApi.createSanPhamGia(data);
        return sanphamgias;
    }

    public async getSanPhamGia(sanphamgiaId: number): Promise<SanPhamGia> {
        const sanphamgia = await this.sanphamgiaApi.getSanPhamGia(sanphamgiaId);
        return sanphamgia;
    }

    public async updateSanPhamGia(sanphamgiaId: number, params: UpdateSanPhamGiaParams): Promise<SanPhamGia> {
        const sanphamgia = await this.sanphamgiaApi.updateSanPhamGia(sanphamgiaId, params);
        return sanphamgia;
    }

    public async deleteSanPhamGia(sanphamgiaId: number): Promise<void> {
        const sanphamgia = await this.sanphamgiaApi.deleteSanPhamGia(sanphamgiaId);
        return sanphamgia;
    }
}
