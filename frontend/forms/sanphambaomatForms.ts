/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IBaoMatForm {
    ten: string;
};

export var sanphambaomatForm = forms.create<IBaoMatForm>({
    ten: customFields.textField({ required: true })
});
