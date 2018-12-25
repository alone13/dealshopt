/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { TaiKhoan } from "./models";

/* Api input parameters section */
export interface CreateTaiKhoanData {
    tendangnhap: string;
    matkhau: string;
    role_id: number;
}

export interface UpdateTaiKhoanParams {
    tendangnhap?: string;
    matkhau?: string;
    role_id?: number;
}


/* Api interface section */
export interface ITaiKhoanApi {
    getTaiKhoans(params?: PagedApiRequest): Promise<ApiListResponse<TaiKhoan>>;
    getTaiKhoan(taikhoanId: number): Promise<TaiKhoan>;
    createTaiKhoan(data: CreateTaiKhoanData): Promise<TaiKhoan>;
    updateTaiKhoan(taikhoanId: number, params: UpdateTaiKhoanParams): Promise<TaiKhoan>;
    deleteTaiKhoan(taikhoanId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class TaiKhoanApi extends ApiBase implements ITaiKhoanApi {
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

    public async getTaiKhoans(params?: PagedApiRequest): Promise<ApiListResponse<TaiKhoan>> {
        const response = await this.get<ApiListResponse<TaiKhoan>>("/taikhoan/taikhoan/", params);
        return response.body!;
    }

    public async getTaiKhoan(taikhoanId: number): Promise<TaiKhoan> {
        const response = await this.get<TaiKhoan>(`/taikhoan/taikhoan/${taikhoanId}/`);
        return response.body!;
    }

    public async createTaiKhoan(data: CreateTaiKhoanData): Promise<TaiKhoan> {
        const response = await this.post<CreateTaiKhoanData, TaiKhoan>("/taikhoan/taikhoan/", data);
        return response.body!;
    }

    public async updateTaiKhoan(taikhoanId: number, params: UpdateTaiKhoanParams): Promise<TaiKhoan> {
        const response = await this.put<UpdateTaiKhoanParams, TaiKhoan>(`/taikhoan/taikhoan/${taikhoanId}/`, params);
        return response.body!;
    }

    public async deleteTaiKhoan(taikhoanId: number): Promise<void> {
        await this.delete<any, void>(`/taikhoan/taikhoan/${taikhoanId}/`);
    }
}
