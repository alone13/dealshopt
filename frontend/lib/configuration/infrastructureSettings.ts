/// <reference path="../../typings/izischool.d.ts"/>

import * as convict from "convict";

export interface IInfrastructureSettings {
    endpoints: {
        apps: string;
    };
    frontend: {
        staticDomain: string;
        endpoint: string;
        sessionSecret: string;
    };
}

export var infrastructureSettingsSchema: convict.Schema = {
    endpoints: {
        apps: { default: "http://localhost:8000/" }
    },
    frontend: {
        staticDomain: { default: "localhost:2016" },
        endpoint: { default: "http://localhost:2016" },
        sessionSecret: { default: "nya" }
    }
};
