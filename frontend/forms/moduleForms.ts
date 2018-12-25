/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IModuleForm {
    ten: string;
};

export var moduleForm = forms.create<IModuleForm>({
    ten: customFields.textField({ required: true })
});
