/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ILuaChonSanPhamForm {
    sanpham_id: number;
    ten: string;
};

export var luachonForm = forms.create<ILuaChonSanPhamForm>({
    sanpham_id: customFields.textField({ required: true }),
    ten: customFields.textField({ required: true })
});
