/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IAmThucApi, CreateAmThucData, UpdateAmThucParams } from "../lib/api/amthucApi";
import { AmThuc } from "../lib/api/models";

export interface IAmThucPageLogic {
    getAmThucs(request: PagedApiRequest): Promise<ApiListResponse<AmThuc>>;
    createAmThuc(data: CreateAmThucData): Promise<AmThuc>;
    getAmThuc(amthucId: number): Promise<AmThuc>;
    updateAmThuc(amthucId: number, params: UpdateAmThucParams): Promise<AmThuc>;
    deleteAmThuc(amthucId: number): Promise<void>;
}

@Dependency.register()
export class AmThucPageLogic extends PageLogicBase implements IAmThucPageLogic {
    static $inject: string[] = ["AmThucApi"];
    private amthucApi: IAmThucApi;
    constructor(
        amthucApi: IAmThucApi
    ) {
        super();
        this.amthucApi = amthucApi;
    }

    public async getAmThucs(request: PagedApiRequest): Promise<ApiListResponse<AmThuc>> {
        const amthucs = await this.amthucApi.getAmThucs(request);
        return amthucs;
    }

    public async createAmThuc(data: CreateAmThucData): Promise<AmThuc> {
        const amthucs = await this.amthucApi.createAmThuc(data);
        return amthucs;
    }

    public async getAmThuc(amthucId: number): Promise<AmThuc> {
        const amthuc = await this.amthucApi.getAmThuc(amthucId);
        return amthuc;
    }

    public async updateAmThuc(amthucId: number, params: UpdateAmThucParams): Promise<AmThuc> {
        const amthuc = await this.amthucApi.updateAmThuc(amthucId, params);
        return amthuc;
    }

    public async deleteAmThuc(amthucId: number): Promise<void> {
        const amthuc = await this.amthucApi.deleteAmThuc(amthucId);
        return amthuc;
    }
}
