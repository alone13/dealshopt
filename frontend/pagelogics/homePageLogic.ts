/// <reference path='../typings/izischool.d.ts' />

import * as bluebird from "bluebird";

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";

export interface IHomePageLogic {
  getString(): Promise<string>;
}


@Dependency.register()
export class HomePageLogic extends PageLogicBase implements IHomePageLogic {

    // static $inject: string[] = [""];

    constructor() {
        super();
    }

    public async getString(): Promise<string> {
        return "";
    }
}
