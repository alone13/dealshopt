/// <reference path="../typings/izischool.d.ts"/>

import * as forms from "forms";
import * as url from "url";
import * as moment from "moment-timezone";

const validators = forms.validators;

function hasValue(field: forms.IField): boolean {
    return (field.data || "").trim().length !== 0;
}

function value(field: forms.IField): string {
    return (field.data || "").trim();
}

const PASSWORD_MATCH_MESSAGE = "Error";
export function passwordMatch(fieldName: string, message?: string): forms.IValidator {
    return validators.matchField(fieldName, message || PASSWORD_MATCH_MESSAGE);
}

export function minlength(val: number, message: string): forms.IValidator {
    const msg = message || `Please enter at least ${val} characters.`;
    return function (form: forms.IForm<any>, field: forms.IField, callback: Function): void {
        if (field.data.length >= val) {
            callback();
        } else {
            callback(msg.replace("%{length}%", field.data.length.toString()));
        }
    };
}

const NOT_ZERO = "Error";
export function notZero(message?: string): forms.IValidator {
    const msg = message || NOT_ZERO;
    return function (form: forms.IForm<any>, field: forms.IField, callback: Function): void {
        if (field.data === 0) {
            callback(msg);
        } else {
            callback();
        }
    };
}

const MAX_VALUE = "Error";
export function maxValue(val?: number, message?: string): forms.IValidator {
    const msg = message || MAX_VALUE;
    const max = val || 100000000;
    return function (form: forms.IForm<any>, field: forms.IField, callback: Function): void {
        if (field.data >= max) {
            callback(msg.replace("%{value}%", max.toString()));
        } else {
            callback();
        }
    };
}


const MIN_VALUE = "Error";
export function minValue(val?: number, message?: string): forms.IValidator {
    const msg = message || MIN_VALUE;
    const min = val || 1;
    return function (form: forms.IForm<any>, field: forms.IField, callback: Function): void {
        if (field.data < min) {
            callback(msg.replace("%{value}%", min.toString()));
        } else {
            callback();
        }
    };
}

const NON_BLANK_MESSAGE = "Non blank";
export function nonBlank(message?: string): forms.IValidator  {
    const msg = message || NON_BLANK_MESSAGE;
    return function (form: forms.IForm<any>, field: forms.IField, callback: Function): void {
        if (field.data.trim().length === 0) {
            callback(msg);
        } else {
            callback();
        }
    };
}
