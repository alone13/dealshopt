/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IQuanHuyenApi, CreateQuanHuyenData, UpdateQuanHuyenParams } from "../lib/api/quanhuyenApi";
import { QuanHuyen } from "../lib/api/models";

export interface IQuanHuyenPageLogic {
    getQuanHuyens(request: PagedApiRequest): Promise<ApiListResponse<QuanHuyen>>;
    createQuanHuyen(data: CreateQuanHuyenData): Promise<QuanHuyen>;
    getQuanHuyen(quanhuyenId: number): Promise<QuanHuyen>;
    updateQuanHuyen(quanhuyenId: number, params: UpdateQuanHuyenParams): Promise<QuanHuyen>;
    deleteQuanHuyen(quanhuyenId: number): Promise<void>;
}

@Dependency.register()
export class QuanHuyenPageLogic extends PageLogicBase implements IQuanHuyenPageLogic {
    static $inject: string[] = ["QuanHuyenApi"];
    private quanhuyenApi: IQuanHuyenApi;
    constructor(
        quanhuyenApi: IQuanHuyenApi
    ) {
        super();
        this.quanhuyenApi = quanhuyenApi;
    }

    public async getQuanHuyens(request: PagedApiRequest): Promise<ApiListResponse<QuanHuyen>> {
        const quanhuyens = await this.quanhuyenApi.getQuanHuyens(request);
        return quanhuyens;
    }

    public async createQuanHuyen(data: CreateQuanHuyenData): Promise<QuanHuyen>{
        const quanhuyens = await this.quanhuyenApi.createQuanHuyen(data);
        return quanhuyens;
    }

    public async getQuanHuyen(quanhuyenId: number): Promise<QuanHuyen>{
        const quanhuyen = await this.quanhuyenApi.getQuanHuyen(quanhuyenId);
        return quanhuyen;
    }

    public async updateQuanHuyen(quanhuyenId: number, params: UpdateQuanHuyenParams): Promise<QuanHuyen>{
        const quanhuyen = await this.quanhuyenApi.updateQuanHuyen(quanhuyenId, params);
        return quanhuyen;
    }

    public async deleteQuanHuyen(quanhuyenId: number): Promise<void>{
        const quanhuyen = await this.quanhuyenApi.deleteQuanHuyen(quanhuyenId);
        return quanhuyen;
    }
}
