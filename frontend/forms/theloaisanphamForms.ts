/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ITheLoaiSanPhamForm {
    ten: string;
    link: string;
    trangthai: boolean;
};

export var theloaisanphamForm = forms.create<ITheLoaiSanPhamForm>({
    ten: customFields.textField({ required: true }),
    link: customFields.textField({ required: true }),
    trangthai: customFields.textField({ required: true })
});
