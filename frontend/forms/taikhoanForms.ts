/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ITaiKhoanForm {
    tendangnhap: string;
    matkhau: string;
    role_id: number;
};

export var taikhoanForm = forms.create<ITaiKhoanForm>({
    tendangnhap: customFields.textField({ required: true }),
    matkhau: customFields.textField({ required: true }),
    role_id: customFields.textField({ required: true })
});
