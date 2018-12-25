/// <reference path="../../typings/izischool.d.ts"/>

import * as intravenous from "intravenous";
import * as convict from "convict";

export interface IConfigurationManager {
    registerSettings(name: string, schema: convict.Schema, path: string): void;
}

export class ConfiguraionManager implements IConfigurationManager {
    constructor(container: intravenous.IContainer) {
        this.container = container;
        this.settings = {};
    }

    private container: intravenous.IContainer;
    private settings: {
        [key: string]: convict.Config
    };

    public registerSettings(name: string, schema: convict.Schema, path: string): void {
        const config = convict(schema);
        config.loadFile(path);
        this.settings[name] = config;
        this.container.register(name, config.get("settings"));
    }
}
