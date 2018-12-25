/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface IRoleForm {
    ten: string;
};

export var roleForm = forms.create<IRoleForm>({
    ten: customFields.textField({ required: true })
});
