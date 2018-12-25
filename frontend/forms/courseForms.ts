/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as customFields from "./customFields";

export interface ICourseForm {
    name: string;
};

export var courseForm = forms.create<ICourseForm>({
    name: customFields.textField({ required: true })
});
