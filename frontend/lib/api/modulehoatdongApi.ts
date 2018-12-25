/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Module_HoatDong } from "./models";

/* Api input parameters section */
export interface CreateModule_HoatDongData {
    module_id: number;
    hoatdong_id: number;
}

export interface UpdateModule_HoatDongParams {
    module_id?: number;
    hoatdong_id?: number;
}


/* Api interface section */
export interface IModule_HoatDongApi {
    getModule_HoatDongs(params?: PagedApiRequest): Promise<ApiListResponse<Module_HoatDong>>;
    getModule_HoatDong(modulehdId: number): Promise<Module_HoatDong>;
    createModule_HoatDong(data: CreateModule_HoatDongData): Promise<Module_HoatDong>;
    updateModule_HoatDong(modulehdId: number, params: UpdateModule_HoatDongParams): Promise<Module_HoatDong>;
    deleteModule_HoatDong(modulehdId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class Module_HoatDongApi extends ApiBase implements IModule_HoatDongApi {
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

    public async getModule_HoatDongs(params?: PagedApiRequest): Promise<ApiListResponse<Module_HoatDong>> {
        const response = await this.get<ApiListResponse<Module_HoatDong>>("/admin/moduleaction/", params);
        return response.body!;
    }

    public async getModule_HoatDong(modulehdId: number): Promise<Module_HoatDong> {
        const response = await this.get<Module_HoatDong>(`/admin/moduleaction/${modulehdId}/`);
        return response.body!;
    }

    public async createModule_HoatDong(data: CreateModule_HoatDongData): Promise<Module_HoatDong> {
        const response = await this.post<CreateModule_HoatDongData, Module_HoatDong>("/admin/moduleaction/", data);
        return response.body!;
    }

    public async updateModule_HoatDong(modulehdId: number, params: UpdateModule_HoatDongParams): Promise<Module_HoatDong> {
        const response = await this.put<UpdateModule_HoatDongParams, Module_HoatDong>(`/admin/moduleaction/${modulehdId}/`, params);
        return response.body!;
    }

    public async deleteModule_HoatDong(modulehdId: number): Promise<void> {
        await this.delete<any, void>(`/admin/moduleaction/${modulehdId}/`);
    }
}
