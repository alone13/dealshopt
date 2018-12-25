/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ITinTucApi, CreateTinTucData, UpdateTinTucParams } from "../lib/api/tintucApi";
import { TinTuc } from "../lib/api/models";

export interface ITinTucPageLogic {
    getTinTucs(request: PagedApiRequest): Promise<ApiListResponse<TinTuc>>;
    createTinTuc(data: CreateTinTucData): Promise<TinTuc>;
    getTinTuc(danhmucId: number): Promise<TinTuc>;
    updateTinTuc(danhmucId: number, params: UpdateTinTucParams): Promise<TinTuc>;
    deleteTinTuc(danhmucId: number): Promise<void>;
}

@Dependency.register()
export class TinTucPageLogic extends PageLogicBase implements ITinTucPageLogic {
    static $inject: string[] = ["TinTucApi"];
    private tintucApi: ITinTucApi;
    constructor(
        tintucApi: ITinTucApi
    ) {
        super();
        this.tintucApi = tintucApi;
    }

    public async getTinTucs(request: PagedApiRequest): Promise<ApiListResponse<TinTuc>> {
        const tintucs = await this.tintucApi.getTinTucs(request);
        return tintucs;
    }

    public async createTinTuc(data: CreateTinTucData): Promise<TinTuc> {
        const tintucs = await this.tintucApi.createTinTuc(data);
        return tintucs;
    }

    public async getTinTuc(tintucId: number): Promise<TinTuc> {
        const tintuc = await this.tintucApi.getTinTuc(tintucId);
        return tintuc;
    }

    public async updateTinTuc(tintucId: number, params: UpdateTinTucParams): Promise<TinTuc> {
        const tintuc = await this.tintucApi.updateTinTuc(tintucId, params);
        return tintuc;
    }

    public async deleteTinTuc(tintucId: number): Promise<void> {
        const tintuc = await this.tintucApi.deleteTinTuc(tintucId);
        return tintuc;
    }
}
