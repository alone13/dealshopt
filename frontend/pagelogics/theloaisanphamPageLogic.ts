/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ITheLoaiSanPhamApi, CreateTheLoaiSanPhamData, UpdateTheLoaiSanPhamParams } from "../lib/api/theloaisanphamApi";
import { TheLoaiSanPham } from "../lib/api/models";

export interface ITheLoaiSanPhamPageLogic {
    getTheLoaiSanPhams(request: PagedApiRequest): Promise<ApiListResponse<TheLoaiSanPham>>;
    createTheLoaiSanPham(data: CreateTheLoaiSanPhamData): Promise<TheLoaiSanPham>;
    getTheLoaiSanPham(theloaisanphamId: number): Promise<TheLoaiSanPham>;
    updateTheLoaiSanPham(theloaisanphamId: number, params: UpdateTheLoaiSanPhamParams): Promise<TheLoaiSanPham>;
    deleteTheLoaiSanPham(theloaisanphamId: number): Promise<void>;
}

@Dependency.register()
export class TheLoaiSanPhamPageLogic extends PageLogicBase implements ITheLoaiSanPhamPageLogic {
    static $inject: string[] = ["TheLoaiSanPhamApi"];
    private theloaisanphamApi: ITheLoaiSanPhamApi;
    constructor(
        theloaisanphamApi: ITheLoaiSanPhamApi
    ) {
        super();
        this.theloaisanphamApi = theloaisanphamApi;
    }

    public async getTheLoaiSanPhams(request: PagedApiRequest): Promise<ApiListResponse<TheLoaiSanPham>> {
        const theloaisanphams = await this.theloaisanphamApi.getTheLoaiSanPhams(request);
        return theloaisanphams;
    }

    public async createTheLoaiSanPham(data: CreateTheLoaiSanPhamData): Promise<TheLoaiSanPham> {
        const theloaisanphams = await this.theloaisanphamApi.createTheLoaiSanPham(data);
        return theloaisanphams;
    }

    public async getTheLoaiSanPham(theloaisanphamId: number): Promise<TheLoaiSanPham> {
        const theloaisanpham = await this.theloaisanphamApi.getTheLoaiSanPham(theloaisanphamId);
        return theloaisanpham;
    }

    public async updateTheLoaiSanPham(theloaisanphamId: number, params: UpdateTheLoaiSanPhamParams): Promise<TheLoaiSanPham> {
        const theloaisanpham = await this.theloaisanphamApi.updateTheLoaiSanPham(theloaisanphamId, params);
        return theloaisanpham;
    }

    public async deleteTheLoaiSanPham(theloaisanphamId: number): Promise<void> {
        const theloaisanpham = await this.theloaisanphamApi.deleteTheLoaiSanPham(theloaisanphamId);
        return theloaisanpham;
    }
}
