/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { TheLoaiSanPham } from "./models";

/* Api input parameters section */
export interface CreateTheLoaiSanPhamData {
    ten:string;
    link: string;
    trangthai: boolean;
}

export interface UpdateTheLoaiSanPhamParams {
    ten?:string;
    link?: string;
    trangthai?: boolean;
}


/* Api interface section */
export interface ITheLoaiSanPhamApi {
    getTheLoaiSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<TheLoaiSanPham>>;
    getTheLoaiSanPham(theloaisanphamId: number): Promise<TheLoaiSanPham>;
    createTheLoaiSanPham(data: CreateTheLoaiSanPhamData): Promise<TheLoaiSanPham>;
    updateTheLoaiSanPham(theloaisanphamId: number, params: UpdateTheLoaiSanPhamParams): Promise<TheLoaiSanPham>;
    deleteTheLoaiSanPham(theloaisanphamId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class TheLoaiSanPhamApi extends ApiBase implements ITheLoaiSanPhamApi {
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

    public async getTheLoaiSanPhams(params?: PagedApiRequest): Promise<ApiListResponse<TheLoaiSanPham>> {
        const response = await this.get<ApiListResponse<TheLoaiSanPham>>("/sanpham/theloai_sanpham/", params);
        return response.body!;
    }

    public async getTheLoaiSanPham(theloaisanphamId: number): Promise<TheLoaiSanPham> {
        const response = await this.get<TheLoaiSanPham>(`/sanpham/theloai_sanpham/${theloaisanphamId}/`);
        return response.body!;
    }

    public async createTheLoaiSanPham(data: CreateTheLoaiSanPhamData): Promise<TheLoaiSanPham> {
        const response = await this.post<CreateTheLoaiSanPhamData, TheLoaiSanPham>("/sanpham/theloai_sanpham/", data);
        return response.body!;
    }

    public async updateTheLoaiSanPham(theloaisanphamId: number, params: UpdateTheLoaiSanPhamParams): Promise<TheLoaiSanPham> {
        const response = await this.put<UpdateTheLoaiSanPhamParams, TheLoaiSanPham>(`/sanpham/theloai_sanpham/${theloaisanphamId}/`, params);
        return response.body!;
    }

    public async deleteTheLoaiSanPham(theloaisanphamId: number): Promise<void> {
        await this.delete<any, void>(`/sanpham/theloai_sanpham/${theloaisanphamId}/`);
    }
}
