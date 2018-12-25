/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ISanPhamBaoMatApi, CreateSanPhamBaoMatData, UpdateSanPhamBaoMatParams } from "../lib/api/sanphambaomatApi";
import { SanPhamBaoMat } from "../lib/api/models";

export interface ISanPhamBaoMatPageLogic {
    getSanPhamBaoMats(request: PagedApiRequest): Promise<ApiListResponse<SanPhamBaoMat>>;
    createSanPhamBaoMat(data: CreateSanPhamBaoMatData): Promise<SanPhamBaoMat>;
    getSanPhamBaoMat(sanphambaomatId: number): Promise<SanPhamBaoMat>;
    updateSanPhamBaoMat(sanphambaomatId: number, params: UpdateSanPhamBaoMatParams): Promise<SanPhamBaoMat>;
    deleteSanPhamBaoMat(sanphambaomatId: number): Promise<void>;
}

@Dependency.register()
export class SanPhamBaoMatPageLogic extends PageLogicBase implements ISanPhamBaoMatPageLogic {
    static $inject: string[] = ["SanPhamBaoMatApi"];
    private sanphambaomatApi: ISanPhamBaoMatApi;
    constructor(
        sanphambaomatApi: ISanPhamBaoMatApi
    ) {
        super();
        this.sanphambaomatApi = sanphambaomatApi;
    }

    public async getSanPhamBaoMats(request: PagedApiRequest): Promise<ApiListResponse<SanPhamBaoMat>> {
        const sanphambaomats = await this.sanphambaomatApi.getSanPhamBaoMats(request);
        return sanphambaomats;
    }

    public async createSanPhamBaoMat(data: CreateSanPhamBaoMatData): Promise<SanPhamBaoMat> {
        const sanphambaomats = await this.sanphambaomatApi.createSanPhamBaoMat(data);
        return sanphambaomats;
    }

    public async getSanPhamBaoMat(sanphambaomatId: number): Promise<SanPhamBaoMat> {
        const sanphambaomat = await this.sanphambaomatApi.getSanPhamBaoMat(sanphambaomatId);
        return sanphambaomat;
    }

    public async updateSanPhamBaoMat(sanphambaomatId: number, params: UpdateSanPhamBaoMatParams): Promise<SanPhamBaoMat> {
        const sanphambaomat = await this.sanphambaomatApi.updateSanPhamBaoMat(sanphambaomatId, params);
        return sanphambaomat;
    }

    public async deleteSanPhamBaoMat(sanphambaomatId: number): Promise<void> {
        const sanphambaomat = await this.sanphambaomatApi.deleteSanPhamBaoMat(sanphambaomatId);
        return sanphambaomat;
    }
}
