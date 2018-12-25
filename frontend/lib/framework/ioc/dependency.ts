/// <reference path="../../../typings/izischool.d.ts"/>

import * as intravenous from "intravenous";
import * as wrench from "wrench";
import * as path from "path";

interface IRegisterMeta extends Function {
    __dep_meta__: {
        register?: boolean;
        customName?: string;
        environment?: string;
        scope?: string;
    };
}

export interface IRegistrationOptions {
    name?: string;
    env?: string;
    scope?: "singleton" | "perRequest" | "unique";
}

export class Dependency {
    static register(options?: IRegistrationOptions): ClassDecorator {
        return (target: Function) => {
            Dependency.injectDependencyMetadata(target, options);
        };
    }

    static registerType(ctor: Function, options?: IRegistrationOptions): void {
        Dependency.injectDependencyMetadata(ctor, options);
    }

    private static injectDependencyMetadata(target: Function, options?: IRegistrationOptions): void {
        (<IRegisterMeta>target).__dep_meta__ = (<IRegisterMeta>target).__dep_meta__ || {};
        (<IRegisterMeta>target).__dep_meta__.register = true;
        if (options && options.name) {
            (<IRegisterMeta>target).__dep_meta__.customName = options.name;
            (<IRegisterMeta>target).__dep_meta__.environment = options.env;
            (<IRegisterMeta>target).__dep_meta__.scope = options.scope;
        }
    }
}

export function Discover(container: intravenous.IContainer, dir: string, env: string): void {
    const moduleFiles = wrench.readdirSyncRecursive(dir);

    const registeredModules: Object = {};
    moduleFiles.forEach((moduleFile: string) => {
        if (path.extname(moduleFile) !== ".ts") {
            return;
        }
        const jsModuleFile = path.basename(moduleFile, ".ts");
        const jsModuleFilePath = path.join(dir, path.dirname(moduleFile), `${jsModuleFile}.js`);
        /* tslint:disable:no-require-imports */
        const module: Object = require(jsModuleFilePath);
        /* tslint:enable */
        for (const m in module) {
            if (!module.hasOwnProperty(m)) {
                continue;
            }

            const obj: IRegisterMeta = module[m];
            if (!(obj.__dep_meta__ && obj.__dep_meta__.register)) {
                continue;
            }

            if (obj.__dep_meta__.environment && obj.__dep_meta__.environment !== env) {
                continue;
            }

            const registrationName = obj.__dep_meta__.customName || m;
            const scope = obj.__dep_meta__.scope;

            if (registeredModules[registrationName]) {
                continue;
            }

            container.register(registrationName, module[m], scope);
            registeredModules[registrationName] = m;
        }
    });
}
