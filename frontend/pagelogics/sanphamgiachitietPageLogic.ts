/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ISanPhamGiaChiTietApi, CreateSanPhamGiaChiTietData, UpdateSanPhamGiaChiTietParams } from "../lib/api/sanphamgiachitietApi";
import { SanPhamGiaChiTiet } from "../lib/api/models";

export interface ISanPhamGiaChiTietPageLogic {
    getSanPhamGiaChiTiets(request: PagedApiRequest): Promise<ApiListResponse<SanPhamGiaChiTiet>>;
    createSanPhamGiaChiTiet(data: CreateSanPhamGiaChiTietData): Promise<SanPhamGiaChiTiet>;
    getSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<SanPhamGiaChiTiet>;
    updateSanPhamGiaChiTiet(sanphamgiachitietId: number, params: UpdateSanPhamGiaChiTietParams): Promise<SanPhamGiaChiTiet>;
    deleteSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<void>;
}

@Dependency.register()
export class SanPhamGiaChiTietPageLogic extends PageLogicBase implements ISanPhamGiaChiTietPageLogic {
    static $inject: string[] = ["SanPhamGiaChiTietApi"];
    private sanphamgiachitietApi: ISanPhamGiaChiTietApi;
    constructor(
        sanphamgiachitietApi: ISanPhamGiaChiTietApi
    ) {
        super();
        this.sanphamgiachitietApi = sanphamgiachitietApi;
    }

    public async getSanPhamGiaChiTiets(request: PagedApiRequest): Promise<ApiListResponse<SanPhamGiaChiTiet>> {
        const sanphamgiachitiets = await this.sanphamgiachitietApi.getSanPhamGiaChiTiets(request);
        return sanphamgiachitiets;
    }

    public async createSanPhamGiaChiTiet(data: CreateSanPhamGiaChiTietData): Promise<SanPhamGiaChiTiet> {
        const sanphamgiachitiets = await this.sanphamgiachitietApi.createSanPhamGiaChiTiet(data);
        return sanphamgiachitiets;
    }

    public async getSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<SanPhamGiaChiTiet> {
        const sanphamgiachitiet = await this.sanphamgiachitietApi.getSanPhamGiaChiTiet(sanphamgiachitietId);
        return sanphamgiachitiet;
    }

    public async updateSanPhamGiaChiTiet(sanphamgiachitietId: number, params: UpdateSanPhamGiaChiTietParams): Promise<SanPhamGiaChiTiet> {
        const sanphamgiachitiet = await this.sanphamgiachitietApi.updateSanPhamGiaChiTiet(sanphamgiachitietId, params);
        return sanphamgiachitiet;
    }

    public async deleteSanPhamGiaChiTiet(sanphamgiachitietId: number): Promise<void> {
        const sanphamgiachitiet = await this.sanphamgiachitietApi.deleteSanPhamGiaChiTiet(sanphamgiachitietId);
        return sanphamgiachitiet;
    }
}
