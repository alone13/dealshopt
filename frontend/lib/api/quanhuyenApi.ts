/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { QuanHuyen } from "./models";

/* Api input parameters section */
export interface CreateQuanHuyenData {
    tinh_id:number;
    ten:string;
    trangthai: boolean;
}

export interface UpdateQuanHuyenParams {
    tinh_id?:number;
    ten?:string;
    trangthai?: boolean;
}


/* Api interface section */
export interface IQuanHuyenApi {
    getQuanHuyens(params?: PagedApiRequest): Promise<ApiListResponse<QuanHuyen>>;
    getQuanHuyen(quanhuyenId: number): Promise<QuanHuyen>;
    createQuanHuyen(data: CreateQuanHuyenData): Promise<QuanHuyen>;
    updateQuanHuyen(quanhuyenId: number, params: UpdateQuanHuyenParams): Promise<QuanHuyen>;
    deleteQuanHuyen(quanhuyenId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class QuanHuyenApi extends ApiBase implements IQuanHuyenApi {
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

    public async getQuanHuyens(params?: PagedApiRequest): Promise<ApiListResponse<QuanHuyen>> {
        const response = await this.get<ApiListResponse<QuanHuyen>>("/sanpham/quanhuyen/", params);
        return response.body!;
    }

    public async getQuanHuyen(quanhuyenId: number): Promise<QuanHuyen> {
        const response = await this.get<QuanHuyen>(`/sanpham/quanhuyen/${quanhuyenId}/`);
        return response.body!;
    }

    public async createQuanHuyen(data: CreateQuanHuyenData): Promise<QuanHuyen> {
        const response = await this.post<CreateQuanHuyenData, QuanHuyen>("/sanpham/quanhuyen/", data);
        return response.body!;
    }

    public async updateQuanHuyen(quanhuyenId: number, params: UpdateQuanHuyenParams): Promise<QuanHuyen> {
        const response = await this.put<UpdateQuanHuyenParams, QuanHuyen>(`/sanpham/quanhuyen/${quanhuyenId}/`, params);
        return response.body!;
    }

    public async deleteQuanHuyen(quanhuyenId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/quanhuyen/${quanhuyenId}/`);
    }
}
