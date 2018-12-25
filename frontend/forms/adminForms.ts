/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IAdminForm {
    taikhoan_id: number;
};

export var adminForm = forms.create<IAdminForm>({
    taikhoan_id: customFields.textField({ required: true })
});
