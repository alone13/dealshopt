/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IQuanHuyenForm {
    tinh_id: number;
    ten: string;
    trangthai: boolean;
};

export var quanhuyenForm = forms.create<IQuanHuyenForm>({
    tinh_id: customFields.textField({ required: true }),
    ten: customFields.textField({ required: true }),
    trangthai: customFields.textField({ required: true })
});
