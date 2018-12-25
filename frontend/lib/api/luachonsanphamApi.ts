/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { LuaChonSanPham } from "./models";

/* Api input parameters section */
export interface CreateLuaChonSanPhamData {
    sanpham_id: number;
    ten:string;
}

export interface UpdateLuaChonSanPhamParams {
    sanpham_id?: number;
    ten?:string;
}


/* Api interface section */
export interface ILuaChonSanPhamApi {
    getLuaChonSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<LuaChonSanPham>>;
    getLuaChonSanPham(luachonsanphamId: number): Promise<LuaChonSanPham>;
    createLuaChonSanPham(data: CreateLuaChonSanPhamData): Promise<LuaChonSanPham>;
    updateLuaChonSanPham(luachonsanphamId: number, params: UpdateLuaChonSanPhamParams): Promise<LuaChonSanPham>;
    deleteLuaChonSanPham(luachonsanphamId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class LuaChonSanPhamApi extends ApiBase implements ILuaChonSanPhamApi {
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

    public async getLuaChonSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<LuaChonSanPham>> {
        const response = await this.get<ApiListResponse<LuaChonSanPham>>("/sanpham/luachon_sanpham/", params);
        return response.body!;
    }

    public async getLuaChonSanPham(luachonsanphamId: number): Promise<LuaChonSanPham> {
        const response = await this.get<LuaChonSanPham>(`/sanpham/luachon_sanpham/${luachonsanphamId}/`);
        return response.body!;
    }

    public async createLuaChonSanPham(data: CreateLuaChonSanPhamData): Promise<LuaChonSanPham> {
        const response = await this.post<CreateLuaChonSanPhamData, LuaChonSanPham>("/sanpham/luachon_sanpham/", data);
        return response.body!;
    }

    public async updateLuaChonSanPham(luachonsanphamId: number, params: UpdateLuaChonSanPhamParams): Promise<LuaChonSanPham> {
        const response = await this.put<UpdateLuaChonSanPhamParams, LuaChonSanPham>(`/sanpham/luachon_sanpham/${luachonsanphamId}/`, params);
        return response.body!;
    }

    public async deleteLuaChonSanPham(luachonsanphamId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/luachon_sanpham/${luachonsanphamId}/`);
    }
}
