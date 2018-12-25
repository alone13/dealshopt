/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IKhachHangApi, CreateKhachHangData, UpdateKhachHangParams } from "../lib/api/khachhangApi";
import { KhachHang } from "../lib/api/models";

export interface IKhachHangPageLogic {
    getKhachHangs(params?: PagedApiRequest): Promise<ApiListResponse<KhachHang>>;
    createKhachHang(data: CreateKhachHangData): Promise<KhachHang>;
    getKhachHang(khachhangId: number): Promise<KhachHang>;
    updateKhachHang(khachhangId: number, params: UpdateKhachHangParams): Promise<KhachHang>;
    deleteKhachHang(khachhangId: number): Promise<void>;
}

@Dependency.register()
export class KhachHangPageLogic extends PageLogicBase implements IKhachHangPageLogic {
    static $inject: string[] = ["KhachHangApi"];
    private khachhangApi: IKhachHangApi;
    constructor(
        khachhangApi: IKhachHangApi
    ) {
        super();
        this.khachhangApi = khachhangApi;
    }

    public async getKhachHangs(request: PagedApiRequest): Promise<ApiListResponse<KhachHang>> {
        const khachhangs = await this.khachhangApi.getKhachHangs(request);
        return khachhangs;
    }

    public async createKhachHang(data: CreateKhachHangData): Promise<KhachHang> {
        const khachhangs = await this.khachhangApi.createKhachHang(data);
        return khachhangs;
    }

    public async getKhachHang(khachhangId: number): Promise<KhachHang> {
        const khachhang = await this.khachhangApi.getKhachHang(khachhangId);
        return khachhang;
    }

    public async updateKhachHang(khachhangId: number, params: UpdateKhachHangParams): Promise<KhachHang> {
        const khachhang = await this.khachhangApi.updateKhachHang(khachhangId, params);
        return khachhang;
    }

    public async deleteKhachHang(khachhangId: number): Promise<void> {
        const khachhang = await this.khachhangApi.deleteKhachHang(khachhangId);
        return khachhang;
    }
}
