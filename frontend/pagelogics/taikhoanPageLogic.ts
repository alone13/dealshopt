/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ITaiKhoanApi, CreateTaiKhoanData, UpdateTaiKhoanParams } from "../lib/api/taikhoanApi";
import { TaiKhoan } from "../lib/api/models";

export interface ITaiKhoanPageLogic {
    getTaiKhoans(request: PagedApiRequest): Promise<ApiListResponse<TaiKhoan>>;
    createTaiKhoan(data: CreateTaiKhoanData): Promise<TaiKhoan>;
    getTaiKhoan(taikhoanId: number): Promise<TaiKhoan>;
    updateTaiKhoan(taikhoanId: number, params: UpdateTaiKhoanParams): Promise<TaiKhoan>;
    deleteTaiKhoan(taikhoanId: number): Promise<void>;
}

@Dependency.register()
export class TaiKhoanPageLogic extends PageLogicBase implements ITaiKhoanPageLogic {
    static $inject: string[] = ["TaiKhoanApi"];
    private taikhoanApi: ITaiKhoanApi;
    constructor(
        taikhoanApi: ITaiKhoanApi
    ) {
        super();
        this.taikhoanApi = taikhoanApi;
    }

    public async getTaiKhoans(request: PagedApiRequest): Promise<ApiListResponse<TaiKhoan>> {
        const taikhoans = await this.taikhoanApi.getTaiKhoans(request);
        return taikhoans;
    }

    public async createTaiKhoan(data: CreateTaiKhoanData): Promise<TaiKhoan> {
        const taikhoans = await this.taikhoanApi.createTaiKhoan(data);
        return taikhoans;
    }

    public async getTaiKhoan(taikhoanId: number): Promise<TaiKhoan> {
        const taikhoan = await this.taikhoanApi.getTaiKhoan(taikhoanId);
        return taikhoan;
    }

    public async updateTaiKhoan(taikhoanId: number, params: UpdateTaiKhoanParams): Promise<TaiKhoan> {
        const taikhoan = await this.taikhoanApi.updateTaiKhoan(taikhoanId, params);
        return taikhoan;
    }

    public async deleteTaiKhoan(taikhoanId: number): Promise<void> {
        const taikhoan = await this.taikhoanApi.deleteTaiKhoan(taikhoanId);
        return taikhoan;
    }
}
