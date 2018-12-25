/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IHoatDongForm {
    ten: string;
};

export var hoatdongForm = forms.create<IHoatDongForm>({
    ten: customFields.textField({ required: true })
});
