/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IModule_HoatDongForm {
    module_id: number;
    hoatdong_id: number;
};

export var modulehdForm = forms.create<IModule_HoatDongForm>({
    module_id: customFields.textField({ required: true }),
    hoatdong_id: customFields.textField({ required: true })
});
