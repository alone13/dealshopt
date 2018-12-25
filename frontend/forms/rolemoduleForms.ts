/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IRole_ModuleForm {
    module_id: number;
    role_id: number;
};

export var role_moduleForm = forms.create<IRole_ModuleForm>({
    module_id: customFields.textField({ required: true }),
    role_id: customFields.textField({ required: true })
});
