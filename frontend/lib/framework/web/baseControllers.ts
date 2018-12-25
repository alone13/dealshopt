/// <reference path="../../../typings/izischool.d.ts"/>

import * as express from "express";
import * as fs from "fs";
import * as wrench from "wrench";
import * as path from "path";
import * as intravenous from "intravenous";

import { Controller } from "./controller";

export function BaseControllers(app: express.Application, controllersDir: string, container: intravenous.IContainer): void {
    const controllers = wrench.readdirSyncRecursive(controllersDir);

    const processedControllers: { name: string, path: string }[] = [];
    controllers.forEach((ctrlFileName) => {
        if (path.extname(ctrlFileName) !== ".ts") {
            return;
        }
        /* tslint:disable:no-require-imports */
        const jsModuleFile = path.basename(ctrlFileName, ".ts");
        const jsModuleFilePath = path.join(controllersDir, path.dirname(ctrlFileName), `${jsModuleFile}.js`);
        const module: Object = require(jsModuleFilePath);
        /* tslint:enable */
        for (const m in module) {
            if (!module.hasOwnProperty(m)) {
                continue;
            }
            if (!m.endsWith("Controller")) {
                continue;
            }

            const existing = processedControllers.find(c => c.name === m);
            if (existing) {
                console.log(`Duplicate controllers found (${m}) in ${existing.path} and ${jsModuleFilePath}`); /* DO NOT REMOVE */
                continue;
            }
            container.register(m, module[m], "perRequest");
            processedControllers.push({
                name: m,
                path: jsModuleFilePath
            });
        }
    });

    processedControllers.forEach((ctrl) => {
        const router = express.Router();
        try {
            const controller = <Controller>container.get(ctrl.name);
            controller._registerController(container, router);
            app.use(router);
        } catch (err) {
            console.error(`Error during ${ctrl.name} registration`, err);
            throw err;
        }
    });

}
