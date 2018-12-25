/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { TinhThanh } from "./models";

/* Api input parameters section */
export interface CreateTinhThanhData {
    ten:string;
    trangthai: boolean;
}

export interface UpdateTinhThanhParams {
    ten?:string;
    trangthai?: boolean;
}


/* Api interface section */
export interface ITinhThanhApi {
    getTinhThanhs(params?: PagedApiRequest): Promise<ApiListResponse<TinhThanh>>;
    getTinhThanh(tinhthanhId: number): Promise<TinhThanh>;
    createTinhThanh(data: CreateTinhThanhData): Promise<TinhThanh>;
    updateTinhThanh(tinhthanhId: number, params: UpdateTinhThanhParams): Promise<TinhThanh>;
    deleteTinhThanh(tinhthanhId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class TinhThanhApi extends ApiBase implements ITinhThanhApi {
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

    public async getTinhThanhs(params?: PagedApiRequest): Promise<ApiListResponse<TinhThanh>> {
        const response = await this.get<ApiListResponse<TinhThanh>>("/sanpham/tinhthanh/", params);
        return response.body!;
    }

    public async getTinhThanh(tinhthanhId: number): Promise<TinhThanh> {
        const response = await this.get<TinhThanh>(`/sanpham/tinhthanh/${tinhthanhId}/`);
        return response.body!;
    }

    public async createTinhThanh(data: CreateTinhThanhData): Promise<TinhThanh> {
        const response = await this.post<CreateTinhThanhData, TinhThanh>("/sanpham/tinhthanh/", data);
        return response.body!;
    }

    public async updateTinhThanh(tinhthanhId: number, params: UpdateTinhThanhParams): Promise<TinhThanh> {
        const response = await this.put<UpdateTinhThanhParams, TinhThanh>(`/sanpham/tinhthanh/${tinhthanhId}/`, params);
        return response.body!;
    }

    public async deleteTinhThanh(tinhthanhId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/tinhthanh/${tinhthanhId}/`);
    }
}
