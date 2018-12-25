/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { IModule_HoatDongApi, CreateModule_HoatDongData, UpdateModule_HoatDongParams } from "../lib/api/modulehoatdongApi";
import { Module_HoatDong } from "../lib/api/models";

export interface IModule_HoatDongPageLogic {
    getModule_HoatDongs(request: PagedApiRequest): Promise<ApiListResponse<Module_HoatDong>>;
    createModule_HoatDong(data: CreateModule_HoatDongData): Promise<Module_HoatDong>;
    getModule_HoatDong(modulehdId: number): Promise<Module_HoatDong>;
    updateModule_HoatDong(modulehdId: number, params: UpdateModule_HoatDongParams): Promise<Module_HoatDong>;
    deleteModule_HoatDong(modulehdId: number): Promise<void>;
}

@Dependency.register()
export class Module_HoatDongPageLogic extends PageLogicBase implements IModule_HoatDongPageLogic {
    static $inject: string[] = ["Role_ModuleApi"];
    private modulehoatdongApi: IModule_HoatDongApi;
    constructor(
        modulehoatdongApi: IModule_HoatDongApi
    ) {
        super();
        this.modulehoatdongApi = modulehoatdongApi;
    }

    public async getModule_HoatDongs(request: PagedApiRequest): Promise<ApiListResponse<Module_HoatDong>> {
        const modulehds = await this.modulehoatdongApi.getModule_HoatDongs(request);
        return modulehds;
    }

    public async createModule_HoatDong(data: CreateModule_HoatDongData): Promise<Module_HoatDong> {
        const modulehds = await this.modulehoatdongApi.createModule_HoatDong(data);
        return modulehds;
    }

    public async getModule_HoatDong(modulehdId: number): Promise<Module_HoatDong> {
        const modulehd = await this.modulehoatdongApi.getModule_HoatDong(modulehdId);
        return modulehd;
    }

    public async updateModule_HoatDong(modulehdId: number, params: UpdateModule_HoatDongParams): Promise<Module_HoatDong> {
        const modulehd = await this.modulehoatdongApi.updateModule_HoatDong(modulehdId, params);
        return modulehd;
    }

    public async deleteModule_HoatDong(modulehdId: number): Promise<void> {
        const modulehd = await this.modulehoatdongApi.deleteModule_HoatDong(modulehdId);
        return modulehd;
    }
}
