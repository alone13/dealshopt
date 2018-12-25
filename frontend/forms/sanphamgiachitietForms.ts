/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ISanPhamGiaCTForm {
    sanpham_gia_id: number;
    gia: string;
    ngaybd: string;
    ngaykt: string;
    is_active: boolean;
};

export var giachitietForm = forms.create<ISanPhamGiaCTForm>({
    sanpham_gia_id: customFields.textField({ required: true }),
    gia: customFields.textField({ required: true }),
    ngaybd: customFields.textField({required:true}),
    ngaykt: customFields.textField({required:true}),
    is_active: customFields.textField({required: true})
});
