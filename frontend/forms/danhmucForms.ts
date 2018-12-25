/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IDanhMucForm {
    danhmuccha: number;
    tendanhmuc: string;
    trangthai: boolean;
    link: string;
};

export var danhmucForm = forms.create<IDanhMucForm>({
    danhmuccha: customFields.textField({ required: true }),
    tendanhmuc: customFields.textField({ required: true }),
    trangthai: customFields.textField({ required: true }),
    link: customFields.textField({ required: true })
});
