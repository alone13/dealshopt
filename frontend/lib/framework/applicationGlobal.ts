/// <reference path="../../typings/izischool.d.ts"/>

import * as intravenous from "intravenous";
import * as nunjucks from "nunjucks";

export interface IApplicationGlobal {
    container?: intravenous.IContainer;
    env?: nunjucks.IEnvironment;
}
