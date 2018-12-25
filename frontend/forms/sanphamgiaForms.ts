/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ISanPhamGiaForm {
    sanpham_id: number;
};

export var sanphamgiaForm = forms.create<ISanPhamGiaForm>({
    sanpham_id: customFields.textField({ required: true }),
});
