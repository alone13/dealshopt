/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ITinTucForm {
    danhmuc_id: number;
    tieude: string;
    hinhanh: string;
    mota: string;
    noidung: string;
    ngaydang: string;
    trangthai: boolean;
};

export var tintucForm = forms.create<ITinTucForm>({
    danhmuc_id: customFields.textField({ required: true }),
    tieude: customFields.textField({ required: true }),
    hinhanh: customFields.textField({ required: true }),
    mota: customFields.textField({ required: true }),
    noidung: customFields.textField({ required: true }),
    ngaydang: customFields.textField({ required: true }),
    trangthai: customFields.textField({ required: true })
});
