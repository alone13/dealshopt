/// <reference path='./typings/izischool.d.ts' />

import * as express from "express";
import * as path from "path";
import * as nunjucks from "nunjucks";
import * as intravenous from "intravenous";
import * as http from "http";
import * as bodyParser from "body-parser";
import * as bluebird from "bluebird";

import { BaseControllers } from "./lib/framework/web/baseControllers";
import { ErrorController } from "./controllers/errorController";
import { Discover } from "./lib/framework/ioc/dependency";
import { AwaitExtension, PartialViewExtension } from "./lib/framework/web/viewExtensions";
import { IApplicationGlobal } from "./lib/framework/applicationGlobal";

import { ConfiguraionManager } from "./lib/framework/configuration";

import * as infrastructureSettings from "./lib//configuration/infrastructureSettings";
import { DiscoverResolvers } from "./lib/framework/web/parameterResolver";

export class Application {
    public app: express.Express;
    public server: http.Server;
    public env: string;

    private appGlobal: IApplicationGlobal;

    constructor() {
        this.appGlobal = {};
    }

    async run(): Promise<void> {
        try {
            this.env = process.env.NODE_ENV || "development";
            this.app = express();

            bluebird.config({
                warnings: false
            });

            const container = await this.configureDependencies();
            this.appGlobal.container = container;
            this.confiureViews(container);
            this.configureMiddleware(container);

            const port = parseInt(process.env.PORT || "2016", 10);
            this.app.set("port", port);
            this.app.set("env", this.env);
            this.app.set("applicationGlobal", this.appGlobal);
            this.app.set("container", container);

            this.server = http.createServer(this.app);
            this.server.listen(port);
            this.server.on("error", this.onError);
        } catch (error) {
            console.error(error);
        }
    }

    close(done?: Function): void {
        this.server.close(done);
    }

    private confiureViews(container: intravenous.IContainer): void {
        this.app.set("view engine", "jinja2");
        this.app.set("views", path.join(__dirname, "views"));
        const environment = nunjucks.configure("./views", {
            express: this.app,
            autoescape: true,
            watch: this.env === "production"
        });

        const infraSettings = <infrastructureSettings.IInfrastructureSettings>container.get("InfrastructureSettings");

        environment.addGlobal("ENV", this.env);
        environment.addGlobal("STATIC_URL", `//${infraSettings.frontend.staticDomain}/`);
        environment.addExtension("PartialViewExtension", new PartialViewExtension(container, environment));
        environment.addExtension("AwaitExtension", new AwaitExtension());

        this.appGlobal.env = environment;
    }

    private async configureDependencies(): Promise<intravenous.IContainer> {
        const container = intravenous.create();
        const configurationManager = new ConfiguraionManager(container);
        configurationManager.registerSettings(
            "InfrastructureSettings",
            infrastructureSettings.infrastructureSettingsSchema,
            path.join(__dirname, "settings/infrastructureSettings.json")
        );

        container.register("ConfigurationManager", configurationManager, "singleton");
        container.register("RequestId", "appstart");
        container.register("ClientId", function() { this.get = function() { return  "appstart"; } });

        Discover(container, path.join(__dirname, "/lib"), this.env);
        Discover(container, path.join(__dirname, "/pagelogics"), this.env);
        DiscoverResolvers(container, path.join(__dirname, "/lib/"));

        return container;
    }

    private configureMiddleware(container: intravenous.IContainer): void {
        this.app.disable("etag");
        this.app.use(bodyParser.json({ limit: "10mb" }));
        this.app.use(bodyParser.urlencoded({ limit: "50mb", extended: false }));
        this.app.use(express.static(path.join(__dirname, "static"), {
              maxAge: 10 * 1000
          }));

        BaseControllers(this.app, path.join(__dirname, "controllers"), container);
        const errorController = <ErrorController>container.get("ErrorController");
        this.app.use(errorController.error.bind(errorController));
        this.app.use(errorController.noUrlMatched.bind(errorController));
    }

    private onError(error: Error): void {
        console.error(error);
    }
}
