/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { KhachHang } from "./models";

/* Api input parameters section */
export interface CreateKhachHangData {
    tenkhachhang: string;
    diachi: string;
    email: string;
    sdt: number;
}

export interface UpdateKhachHangParams {
    tenkhachhang?: string;
    diachi?: string;
    email?: string;
    sdt?: number;
}


/* Api interface section */
export interface IKhachHangApi {
    getKhachHangs(params?: PagedApiRequest): Promise<ApiListResponse<KhachHang>>;
    getKhachHang(khachhangId: number): Promise<KhachHang>;
    createKhachHang(data: CreateKhachHangData): Promise<KhachHang>;
    updateKhachHang(khachhangId: number, params: UpdateKhachHangParams): Promise<KhachHang>;
    deleteKhachHang(khachhangId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class KhachHangApi extends ApiBase implements IKhachHangApi {
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

    public async getKhachHangs(params?: PagedApiRequest): Promise<ApiListResponse<KhachHang>> {
        const response = await this.get<ApiListResponse<KhachHang>>("/dathang/khachhang/", params);
        return response.body!;
    }

    public async getKhachHang(khachhangId: number): Promise<KhachHang> {
        const response = await this.get<KhachHang>(`/dathang/khachhang/${khachhangId}/`);
        return response.body!;
    }

    public async createKhachHang(data: CreateKhachHangData): Promise<KhachHang> {
        const response = await this.post<CreateKhachHangData, KhachHang>("/dathang/khachhang/", data);
        return response.body!;
    }

    public async updateKhachHang(khachhangId: number, params: UpdateKhachHangParams): Promise<KhachHang> {
        const response = await this.put<UpdateKhachHangParams, KhachHang>(`/dathang/khachhang/${khachhangId}/`, params);
        return response.body!;
    }

    public async deleteKhachHang(khachhangId: number): Promise<void> {
        await this.delete<any, void>(`/dathang/khachhang/${khachhangId}/`);
    }
}
