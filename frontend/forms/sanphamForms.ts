/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ISanPhamForm {
    user_cuahang_id: number;
    theloai_id: number;
    danhmuc_id: number;
    baomat_id: number;
    trangthai_id: number;
    amthuc_id: number;
    tinhthanh_id: number;
    quanhuyen_id: number;
    tensanpham: string;
    hinhanh: string;
    ngaydang: string;
    soluong:number;
};

export var sanphamForm = forms.create<ISanPhamForm>({
    user_cuahang_id: customFields.textField({ required: true }),
    theloai_id: customFields.textField({ required: true }),
    danhmuc_id: customFields.textField({ required: true }),
    baomat_id: customFields.textField({ required: true }),
    trangthai_id: customFields.textField({ required: true }),
    amthuc_id: customFields.textField({ required: true }),
    tinhthanh_id: customFields.textField({ required: true }),
    quanhuyen_id: customFields.textField({ required: true }),
    tensanpham: customFields.textField({ required: true }),
    hinhanh: customFields.textField({ required: true }),
    ngaydang: customFields.textField({ required: true }),
    soluong: customFields.textField({ required: true })
});
