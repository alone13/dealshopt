/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IHoatDongApi, CreateHoatDongData, UpdateHoatDongParams } from "../lib/api/hoatdongApi";
import { HoatDong } from "../lib/api/models";

export interface IHoatDongPageLogic {
    getHoatDongs(request: PagedApiRequest): Promise<ApiListResponse<HoatDong>>;
    createHoatDong(data: CreateHoatDongData): Promise<HoatDong>;
    getHoatDong(hoatdongId: number): Promise<HoatDong>;
    updateHoatDong(hoatdongId: number, params: UpdateHoatDongParams): Promise<HoatDong>;
    deleteHoatDong(hoatdongId: number): Promise<void>;
}

@Dependency.register()
export class HoatDongPageLogic extends PageLogicBase implements IHoatDongPageLogic {
    static $inject: string[] = ["HoatDongApi"];
    private hoatdongApi: IHoatDongApi;
    constructor(
        hoatdongApi: IHoatDongApi
    ) {
        super();
        this.hoatdongApi = hoatdongApi;
    }

    public async getHoatDongs(request: PagedApiRequest): Promise<ApiListResponse<HoatDong>> {
        const hoatdongs = await this.hoatdongApi.getHoatDongs(request);
        return hoatdongs;
    }

    public async createHoatDong(data: CreateHoatDongData): Promise<HoatDong> {
        const hoatdongs = await this.hoatdongApi.createHoatDong(data);
        return hoatdongs;
    }

    public async getHoatDong(hoatdongId: number): Promise<HoatDong> {
        const hoatdong = await this.hoatdongApi.getHoatDong(hoatdongId);
        return hoatdong;
    }

    public async updateHoatDong(hoatdongId: number, params: UpdateHoatDongParams): Promise<HoatDong> {
        const hoatdong = await this.hoatdongApi.updateHoatDong(hoatdongId, params);
        return hoatdong;
    }

    public async deleteHoatDong(hoatdongId: number): Promise<void> {
        const hoatdong = await this.hoatdongApi.deleteHoatDong(hoatdongId);
        return hoatdong;
    }
}
