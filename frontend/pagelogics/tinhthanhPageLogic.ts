/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ITinhThanhApi, CreateTinhThanhData, UpdateTinhThanhParams } from "../lib/api/tinhthanhApi";
import { TinhThanh } from "../lib/api/models";

export interface ITinhThanhPageLogic {
    getTinhThanhs(request: PagedApiRequest): Promise<ApiListResponse<TinhThanh>>;
    createTinhThanh(data: CreateTinhThanhData): Promise<TinhThanh>;
    getTinhThanh(tinhthanhId: number): Promise<TinhThanh>;
    updateTinhThanh(tinhthanhId: number, params: UpdateTinhThanhParams): Promise<TinhThanh>;
    deleteTinhThanh(tinhthanhId: number): Promise<void>;
}

@Dependency.register()
export class TinhThanhPageLogic extends PageLogicBase implements ITinhThanhPageLogic {
    static $inject: string[] = ["TinhThanhApi"];
    private tinhthanhApi: ITinhThanhApi;
    constructor(
        tinhthanhApi: ITinhThanhApi
    ) {
        super();
        this.tinhthanhApi = tinhthanhApi;
    }

    public async getTinhThanhs(request: PagedApiRequest): Promise<ApiListResponse<TinhThanh>> {
        const tinhthanhs = await this.tinhthanhApi.getTinhThanhs(request);
        return tinhthanhs;
    }

    public async createTinhThanh(data: CreateTinhThanhData): Promise<TinhThanh> {
        const tinhthanhs = await this.tinhthanhApi.createTinhThanh(data);
        return tinhthanhs;
    }

    public async getTinhThanh(tinhthanhId: number): Promise<TinhThanh> {
        const tinhthanh = await this.tinhthanhApi.getTinhThanh(tinhthanhId);
        return tinhthanh;
    }

    public async updateTinhThanh(tinhthanhId: number, params: UpdateTinhThanhParams): Promise<TinhThanh> {
        const tinhthanh = await this.tinhthanhApi.updateTinhThanh(tinhthanhId, params);
        return tinhthanh;
    }

    public async deleteTinhThanh(tinhthanhId: number): Promise<void> {
        const tinhthanh = await this.tinhthanhApi.deleteTinhThanh(tinhthanhId);
        return tinhthanh;
    }
}
