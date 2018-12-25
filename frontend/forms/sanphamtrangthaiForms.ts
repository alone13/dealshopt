/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ITrangThaiForm {
    trangthai: boolean;
};

export var sanphamtrangthaiForm = forms.create<ITrangThaiForm>({
    trangthai: customFields.textField({ required: true })
});
