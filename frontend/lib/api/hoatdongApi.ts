/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { HoatDong } from "./models";

/* Api input parameters section */
export interface CreateHoatDongData {
    ten: string;
}

export interface UpdateHoatDongParams {
    ten?: string;
}


/* Api interface section */
export interface IHoatDongApi {
    getHoatDongs(params?: PagedApiRequest): Promise<ApiListResponse<HoatDong>>;
    getHoatDong(hoatdongId: number): Promise<HoatDong>;
    createHoatDong(data: CreateHoatDongData): Promise<HoatDong>;
    updateHoatDong(hoatdongId: number, params: UpdateHoatDongParams): Promise<HoatDong>;
    deleteHoatDong(moduleId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class HoatDongApi extends ApiBase implements IHoatDongApi {
    static $inject: string[] = ["InfrastructureSettings", "RequestId"];
    constructor(
        infrastructureSettings: IInfrastructureSettings,
        requestId: string
    ) {
        super(
            infrastructureSettings.endpoints.apps,
            requestId
        );
    }

    public async getHoatDongs(params?: PagedApiRequest): Promise<ApiListResponse<HoatDong>> {
        const response = await this.get<ApiListResponse<HoatDong>>("/admin/action/", params);
        return response.body!;
    }

    public async getHoatDong(hoatdongId: number): Promise<HoatDong> {
        const response = await this.get<HoatDong>(`/admin/action/${hoatdongId}/`);
        return response.body!;
    }

    public async createHoatDong(data: CreateHoatDongData): Promise<HoatDong> {
        const response = await this.post<CreateHoatDongData, HoatDong>("/admin/action/", data);
        return response.body!;
    }

    public async updateHoatDong(hoatdongId: number, params: UpdateHoatDongParams): Promise<HoatDong> {
        const response = await this.put<UpdateHoatDongParams, HoatDong>(`/admin/action/${hoatdongId}/`, params);
        return response.body!;
    }

    public async deleteHoatDong(hoatdongId: number): Promise<void> {
        await this.delete<any, void>(`/admin/action/${hoatdongId}/`);
    }
}
