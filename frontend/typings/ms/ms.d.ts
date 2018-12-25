// Type definitions for ms v0.7.1
// Project: https://github.com/guille/ms.js
// Definitions by: Zhiyuan Wang <https://github.com/danny8002/>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped

declare module "ms" {
    interface MsStatic {
        (value: number, options?: { long: boolean }): string;
        (value: string): number;
    }
    var ms: MsStatic;
    export = ms;
}
