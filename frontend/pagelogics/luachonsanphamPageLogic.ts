/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ILuaChonSanPhamApi, CreateLuaChonSanPhamData, UpdateLuaChonSanPhamParams } from "../lib/api/luachonsanphamApi";
import { LuaChonSanPham } from "../lib/api/models";

export interface ILuaChonSanPhamPageLogic {
    getLuaChonSanPhams(request: PagedApiRequest): Promise<ApiListResponse<LuaChonSanPham>>;
    createLuaChonSanPham(data: CreateLuaChonSanPhamData): Promise<LuaChonSanPham>;
    getLuaChonSanPham(luachonsanphamId: number): Promise<LuaChonSanPham>;
    updateLuaChonSanPham(luachonsanphamId: number, params: UpdateLuaChonSanPhamParams): Promise<LuaChonSanPham>;
    deleteLuaChonSanPham(luachonsanphamId: number): Promise<void>;
}

@Dependency.register()
export class LuaChonSanPhamPageLogic extends PageLogicBase implements ILuaChonSanPhamPageLogic {
    static $inject: string[] = ["LuaChonSanPhamApi"];
    private luachonsanphamApi: ILuaChonSanPhamApi;
    constructor(
        luachonsanphamApi: ILuaChonSanPhamApi
    ) {
        super();
        this.luachonsanphamApi = luachonsanphamApi;
    }

    public async getLuaChonSanPhams(request: PagedApiRequest): Promise<ApiListResponse<LuaChonSanPham>> {
        const luachonsanphams = await this.luachonsanphamApi.getLuaChonSanPhams(request);
        return luachonsanphams;
    }

    public async createLuaChonSanPham(data: CreateLuaChonSanPhamData): Promise<LuaChonSanPham>{
        const luachonsanphams = await this.luachonsanphamApi.createLuaChonSanPham(data);
        return luachonsanphams;
    }

    public async getLuaChonSanPham(luachonsanphamId: number): Promise<LuaChonSanPham>{
        const luachonsanpham = await this.luachonsanphamApi.getLuaChonSanPham(luachonsanphamId);
        return luachonsanpham;
    }

    public async updateLuaChonSanPham(luachonsanphamId: number, params: UpdateLuaChonSanPhamParams): Promise<LuaChonSanPham>{
        const luachonsanpham = await this.luachonsanphamApi.updateLuaChonSanPham(luachonsanphamId, params);
        return luachonsanpham;
    }

    public async deleteLuaChonSanPham(luachonsanphamId: number): Promise<void>{
        const luachonsanpham = await this.luachonsanphamApi.deleteLuaChonSanPham(luachonsanphamId);
        return luachonsanpham;
    }
}
