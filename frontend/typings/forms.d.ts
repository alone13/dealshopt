declare module "forms" {
    import * as express from "express";

    export interface IForm<T> {
        fields: { [name: string]: IField };
        data: any;
        handle(req: express.Request, callbacks: ICallbacks<T>): void;
        bind(data: any): IBoundForm<T>;
        toHTML(iterator?: (name: string, object: IField) => string): string;
    }

    export interface IBoundForm<T> extends IForm<T> {
        data: T;
        validate(callback: (error: any, form: IBoundForm<T>) => void): void;
        isValid(): boolean;
    }

    export interface ICallbacks<T> {
        success?: (form: IBoundForm<T>) => void;
        error?: (form: IBoundForm<T>) => void;
        empty?: (form: IBoundForm<T>) => void;
        other?: (form: IBoundForm<T>) => void;
    }

    export interface IField {
        name?: string;
        label?: string;
        required?: boolean|IValidator;
        validators?: IValidator[];
        id?: string;
        value?: any;
        data?: any;
        choices?: any[] | { [value: string]: string } | { [value: number]: string };
        error?: string;
    }

    export interface IValidator {
        (form: IForm<any>, field: IField, callback: Function): void;
    }

    export function create<T>(fields: { [name: string]: IField }, opts?: {
        validatePastFirstError?: boolean;
    }): IForm<T>;

    export var fields: {
        string(opts?: IField): IField;
        number(opts?: IField): IField;
        boolean(opts?: IField): IField;
        array(opts?: IField): IField;
        password(opts?: IField): IField;
        email(opts?: IField): IField;
        tel(opts?: IField): IField;
        url(opts?: IField): IField;
        date(opts?: IField): IField;
    };

    export var validators: {
        matchField(matchField: string, message: string): IValidator;
        matchValue(valueGetter: Function, message: string): IValidator;
        required(message: string): IValidator;
        requiresFieldIfEmpty(alternateField: string, message: string): IValidator;
        min(val: number, message: string): IValidator;
        max(val: number, message: string): IValidator;
        range(min: number, max: number, message: string): IValidator;
        minlength(val: number, message: string): IValidator;
        maxlength(val: number, message: string): IValidator;
        rangelength(min: number, max: number, message: string): IValidator;
        regexp(regex: string|RegExp, message: string): IValidator;
        color(message: string): IValidator;
        email(message: string): IValidator;
        url(includeLocalhost: boolean, message: string): IValidator;
        date(message: string): IValidator;
        alphanumeric(message: string): IValidator;
        digits(message: string): IValidator;
        integer(message: string): IValidator;
    };
}
