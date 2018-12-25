/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IAmThucForm {
    ten: string;
    trangthai: boolean;
};

export var amthucForm = forms.create<IAmThucForm>({
    ten: customFields.textField({ required: true }),
    trangthai: customFields.textField({required: true})
});
