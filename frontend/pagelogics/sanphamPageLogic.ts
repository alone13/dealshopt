/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ISanPhamApi, CreateSanPhamData, UpdateSanPhamParams } from "../lib/api/sanphamApi";
import { SanPham } from "../lib/api/models";

export interface ISanPhamPageLogic {
    getSanPhams(request: PagedApiRequest): Promise<ApiListResponse<SanPham>>;
    createSanPham(data: CreateSanPhamData): Promise<SanPham>;
    getSanPham(sanphamId: number): Promise<SanPham>;
    updateSanPham(sanphamId: number, params: UpdateSanPhamParams): Promise<SanPham>;
    deleteSanPham(sanphamId: number): Promise<void>;
}

@Dependency.register()
export class SanPhamPageLogic extends PageLogicBase implements ISanPhamPageLogic {
    static $inject: string[] = ["SanPhamApi"];
    private sanphamApi: ISanPhamApi;
    constructor(
        sanphamApi: ISanPhamApi
    ) {
        super();
        this.sanphamApi = sanphamApi;
    }

    public async getSanPhams(request: PagedApiRequest): Promise<ApiListResponse<SanPham>> {
        const sanphams = await this.sanphamApi.getSanPhams(request);
        return sanphams;
    }

    public async createSanPham(data: CreateSanPhamData): Promise<SanPham> {
        const sanphams = await this.sanphamApi.createSanPham(data);
        return sanphams;
    }

    public async getSanPham(sanphamId: number): Promise<SanPham> {
        const sanpham = await this.sanphamApi.getSanPham(sanphamId);
        return sanpham;
    }

    public async updateSanPham(sanphamId: number, params: UpdateSanPhamParams): Promise<SanPham> {
        const sanpham = await this.sanphamApi.updateSanPham(sanphamId, params);
        return sanpham;
    }

    public async deleteSanPham(sanphamId: number): Promise<void> {
        const sanpham = await this.sanphamApi.deleteSanPham(sanphamId);
        return sanpham;
    }
}
