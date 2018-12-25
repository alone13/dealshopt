/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as bluebird from "bluebird";

import * as customValidators from "./customValidators";
import {IField, IForm, IValidator} from "forms";

const fields = forms.fields;
const validators = forms.validators;

const REQIRED_VALIDATOR_MESSAGE = "Error";
const MINLENGTH_VALIDATOR_MESSAGE = "Error";
const MAXLENGTH_VALIDATOR_MESSAGE = "Error";
const DATEFORMAT_VALIDATOR_MESSAGE = "Error";
const EMAIL_VALIDATOR_MESSAGE = "Error";
const URL_VALIDATOR_MESSAGE = "Error。";

export interface IRequiredField {
    required?: boolean | string;
    customRequired?: forms.IValidator;
}

export interface ITextField extends IRequiredField {
    minlength?: number;
    maxlength?: number;
    optionMinTemplate?: string;
}

export interface IDateField extends IRequiredField {
    customFormat?: RegExp;
}

export interface IChoiceField extends IRequiredField {
    choices: any[] | { [value: string]: string } | { [value: number]: string };
    isChoiceId?: boolean;
    defaultFirstOption?: boolean;
}

export interface INumberField extends IRequiredField {
    minValue?: number;
    maxValue?: number;
}

export interface IArrayField extends IRequiredField {
    itemField?: forms.IField;
}

export function numberField(data: INumberField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    if (data.required) {
        options.required = validators.required(REQIRED_VALIDATOR_MESSAGE);
    }
    options.validators = options.validators || [];
    options.validators.push(customValidators.halfWidthNumber());
    if (data.minValue) {
        options.validators.push(customValidators.minValue(data.minValue));
    }
    if (data.maxValue) {
        options.validators.push(customValidators.maxValue(data.maxValue));
    }
    return fields.number(options);
}

export function passwordField(data: ITextField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];

    options.validators.push(customValidators.halfWidthAndSpecialCharacters());

    return rawTextField(data, options);
}

export function emailField(data: ITextField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];
    options.validators.push(validators.email(EMAIL_VALIDATOR_MESSAGE));
    options.validators.push(customValidators.halfWidthAndSpecialCharacters());

    const field = textField(data, options);
    const originalParse = field["parse"];
    field["parse"] = (rawData: string) => {
        const parsed = originalParse(rawData);
        return parsed.normalize("NFKC");
    };

    return field;
}

export function phoneNumber(data: ITextField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];
    options.validators.push(customValidators.phone());
    options.validators.push(customValidators.halfWidthNumberOrDash());
    options.validators.push(customValidators.blacklistedPhoneNumbers());

    const field = textField(data, options);

    const originalParse = field["parse"];
    field["parse"] = (rawData: string) => {
        const parsed = originalParse(rawData);
        return parsed
            .normalize("NFKC")
            .replace(/[\u2212\u30fc]+/g, "-");
    };

    return field;
}

export function textField(data: ITextField, opts?: forms.IField): forms.IField {
    const field = rawTextField(data, opts);

    const originalParse = field["parse"];
    field["parse"] = (rawData: string) => {
        const parsed = originalParse(rawData);
        return parsed.trim();
    };

    return field;
}

export function rawTextField(data: ITextField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];

    if (data.required) {
        const message = typeof data.required === "string"
            ? <string>data.required
            : REQIRED_VALIDATOR_MESSAGE;
        options.required = validators.required(message);

        // non blank
        options.validators.push(customValidators.nonBlank(message));
    }

    if (data.customRequired) {
        options.required = data.customRequired;
    }

    const template = data.optionMinTemplate ? data.optionMinTemplate : MINLENGTH_VALIDATOR_MESSAGE;
    if (data.minlength && data.minlength > 0) {
        options.validators.push(customValidators.minlength(
            data.minlength,
            template.replace("%{minlength}%", data.minlength.toString()
        )));
        options["minlength"] = data.minlength;
    }
    if (data.maxlength && data.maxlength > 0) {
        options.validators.push(validators.maxlength(
            data.maxlength,
            MAXLENGTH_VALIDATOR_MESSAGE.replace("%{maxlength}%", data.maxlength.toString()
        )));
        options["maxlength"] = data.maxlength;
    }

    return fields.string(options);
}

export function dateField(data: IDateField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];

    if (data.required) {
        const message = typeof data.required === "string"
            ? <string>data.required
            : REQIRED_VALIDATOR_MESSAGE;
        options.required = validators.required(message);
    }
    if (data.customRequired) {
        options.required = data.customRequired;
    }

    options.validators.push(validators.regexp(data.customFormat || /\d{4}\/\d{2}\/\d{2}/, DATEFORMAT_VALIDATOR_MESSAGE));

    return fields.string(options);
}

export function choiceField(data: IChoiceField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];
    options.choices = data.choices;
    if (data.defaultFirstOption) {
        options.value = options.value || options.choices[0];
    }
    if (data.required) {
        const message = typeof data.required === "string"
            ? <string>data.required
            : REQIRED_VALIDATOR_MESSAGE;
        options.required = validators.required(message);
    }
    if (data.customRequired) {
        options.required = data.customRequired;
    }

    options.validators.push((form: forms.IForm<any>, field: forms.IField, callback: Function) => {
        const allowedValues = field.choices instanceof Array
            ? <any[]>field.choices
            : Object.keys(field.choices);

        if (allowedValues.map(v => (v.value || v).toString()).indexOf(field.data) === -1) {
            return callback("Error");
        }
        callback();
    });

    return fields.string(options);
}

export function fileField(data: IRequiredField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || { validators: [] };
    if (data.required) {
        options.required = validators.required(REQIRED_VALIDATOR_MESSAGE);
    }
    return fields.string(options);
}

export function urlField(data: ITextField, opts?: forms.IField): forms.IField {
    const options: forms.IField = opts || {};
    options.validators = options.validators || [];
    options.validators.unshift(validators.url(false, URL_VALIDATOR_MESSAGE));

    return textField(data, options);
}

export async function arrayField(data: IArrayField): Promise<forms.IField> {
    const options: forms.IField = {
        validators: []
    };

    options.validators!.push(async function (form: forms.IForm<any>, field: forms.IField, callback: Function): Promise<void> {
        if (!Array.isArray(field.data)) {
            return callback("The given data is not array");
        }

        const validations: Promise<any>[] = [];
        for (const item of field.data) {
            const validatingPromise = new Promise<any>((resolve, reject) => {

                const fieldTemp: forms.IField = {
                    data: item
                };
                for (const validator of data.itemField!.validators!) {
                    validator(form, fieldTemp, (err: any, result: any) => {
                        if (err) {
                            return reject(err);
                        }
                        resolve(result);
                    });
                }
            });
            validations.push(validatingPromise);
        }

        bluebird.all(validations).done(() => callback(null), err => callback(err));
    });

    const field = fields.array(options);
    field["parse"] = function (raw_data: any) {
        if (typeof raw_data === 'undefined' || raw_data === '') { return []; }
        return Array.isArray(raw_data) ? raw_data : [raw_data];
    }

    return field;
}
