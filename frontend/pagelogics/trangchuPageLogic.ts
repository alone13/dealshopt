/// <reference path='../typings/izischool.d.ts' />

import * as bluebird from "bluebird";

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";

export interface ITrangChuPageLogic {
  getString(): Promise<string>;
}


@Dependency.register()
export class TrangChuPageLogic extends PageLogicBase implements ITrangChuPageLogic {

    // static $inject: string[] = [""];

    constructor() {
        super();
    }

    public async getString(): Promise<string> {
        return "";
    }
}
