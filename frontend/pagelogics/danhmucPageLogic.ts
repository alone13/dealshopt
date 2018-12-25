/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IDanhMucApi, CreateDanhMucData, UpdateDanhMucParams } from "../lib/api/danhmucApi";
import { DanhMuc } from "../lib/api/models";

export interface IDanhMucPageLogic {
    getDanhMucs(request: PagedApiRequest): Promise<ApiListResponse<DanhMuc>>;
    createDanhMuc(data: CreateDanhMucData): Promise<DanhMuc>;
    getDanhMuc(danhmucId: number): Promise<DanhMuc>;
    updateDanhMuc(danhmucId: number, params: UpdateDanhMucParams): Promise<DanhMuc>;
    deleteDanhMuc(danhmucId: number): Promise<void>;
}

@Dependency.register()
export class DanhMucPageLogic extends PageLogicBase implements IDanhMucPageLogic {
    static $inject: string[] = ["DanhMucApi"];
    private danhmucApi: IDanhMucApi;
    constructor(
        danhmucApi: IDanhMucApi
    ) {
        super();
        this.danhmucApi = danhmucApi;
    }

    public async getDanhMucs(request: PagedApiRequest): Promise<ApiListResponse<DanhMuc>> {
        const danhmucs = await this.danhmucApi.getDanhMucs(request);
        return danhmucs;
    }

    public async createDanhMuc(data: CreateDanhMucData): Promise<DanhMuc> {
        const danhmucs = await this.danhmucApi.createDanhMuc(data);
        return danhmucs;
    }

    public async getDanhMuc(danhmucId: number): Promise<DanhMuc> {
        const danhmuc = await this.danhmucApi.getDanhMuc(danhmucId);
        return danhmuc;
    }

    public async updateDanhMuc(danhmucId: number, params: UpdateDanhMucParams): Promise<DanhMuc> {
        const danhmuc = await this.danhmucApi.updateDanhMuc(danhmucId, params);
        return danhmuc;
    }

    public async deleteDanhMuc(danhmucId: number): Promise<void> {
        const danhmuc = await this.danhmucApi.deleteDanhMuc(danhmucId);
        return danhmuc;
    }
}
