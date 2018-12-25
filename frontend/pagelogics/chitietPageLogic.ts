/// <reference path='../typings/izischool.d.ts' />

import * as bluebird from "bluebird";

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";

export interface IChiTietPageLogic {
  getString(): Promise<string>;
}


@Dependency.register()
export class ChiTietPageLogic extends PageLogicBase implements IChiTietPageLogic {

    // static $inject: string[] = [""];

    constructor() {
        super();
    }

    public async getString(): Promise<string> {
        return "";
    }
}
