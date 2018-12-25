/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IKhachHangForm {
    tenkhachhang: string;
    diachi: string;
    email: string;
    sdt: number;
};

export var khachhangForm = forms.create<IKhachHangForm>({
    tenkhachhang: customFields.textField({ required: true }),
    diachi: customFields.textField({ required: true }),
    email: customFields.textField({ required: true }),
    sdt: customFields.textField({ required: true })
});
