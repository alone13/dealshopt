/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ITinhThanhForm {
    ten: string;
    trangthai: boolean;
};

export var tinhthanhForm = forms.create<ITinhThanhForm>({
    ten: customFields.textField({ required: true }),
    trangthai: customFields.textField({ required: true })
});
