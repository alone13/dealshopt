/// <reference path='../typings/izischool.d.ts' />

import * as express from "express";

import { Controller, Method } from "../lib/framework/web/controller";
import { IHomePageLogic } from "../pagelogics/homePageLogic";
import { ICoursePageLogic } from "../pagelogics/coursePageLogic";

export class HomeController extends Controller {
    static $inject: string[] = ["HomePageLogic", "CoursePageLogic"];

    private homePageLogic: IHomePageLogic;
    private coursePageLogic: ICoursePageLogic;

    constructor(
        homePageLogic: IHomePageLogic,
        coursePageLogic: ICoursePageLogic
    ) {
        super();
        this.homePageLogic = homePageLogic;
        this.coursePageLogic = coursePageLogic;
    }

    @Method.get("/Admin/")
    public async index(req: express.Request, res: express.Response, next: express.NextFunction): Promise<void> {

        return res.namedView(req.isMobile() ? "index_sp" : "index", {
            title: "Home"
        });
    }
}
