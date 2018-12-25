/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { AmThuc } from "./models";

/* Api input parameters section */
export interface CreateAmThucData {
    ten:string;
    trangthai: boolean;
}

export interface UpdateAmThucParams {
    ten?:string;
    trangthai?: boolean;
}


/* Api interface section */
export interface IAmThucApi {
    getAmThucs(params?: PagedApiRequest): Promise<ApiListResponse<AmThuc>>;
    getAmThuc(amthucId: number): Promise<AmThuc>;
    createAmThuc(data: CreateAmThucData): Promise<AmThuc>;
    updateAmThuc(amthucId: number, params: UpdateAmThucParams): Promise<AmThuc>;
    deleteAmThuc(amthucId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class AmThucApi extends ApiBase implements IAmThucApi {
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

    public async getAmThucs(params?: PagedApiRequest): Promise<ApiListResponse<AmThuc>> {
        const response = await this.get<ApiListResponse<AmThuc>>("/sanpham/amthuc/", params);
        return response.body!;
    }

    public async getAmThuc(amthucId: number): Promise<AmThuc> {
        const response = await this.get<AmThuc>(`/sanpham/amthuc/${amthucId}/`);
        return response.body!;
    }

    public async createAmThuc(data: CreateAmThucData): Promise<AmThuc> {
        const response = await this.post<CreateAmThucData, AmThuc>("/sanpham/amthuc/", data);
        return response.body!;
    }

    public async updateAmThuc(amthucId: number, params: UpdateAmThucParams): Promise<AmThuc> {
        const response = await this.put<UpdateAmThucParams, AmThuc>(`/sanpham/amthuc/${amthucId}/`, params);
        return response.body!;
    }

    public async deleteAmThuc(amthucId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/amthuc/${amthucId}/`);
    }
}
