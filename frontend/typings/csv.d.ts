/// <reference path="./node/node.d.ts"/>

declare module "csv" {

    interface CSVParserOptions {
      delimiter?: string;
      rowDelimiter?: string;
      quote?: string;
      escape?: string;
      columns?: string[]|boolean|Function;
      comment?: string;
      objname?: string;
      relax?: boolean;
      skip_empty_lines?: boolean;
      trim?: boolean;
      ltrim?: boolean;
      rtrim?: boolean;
      auto_parse?: boolean;
      auto_parse_date?: boolean;
    }

    interface CSVParserCallbackFunction {
        (err: any, output: string[][]): void;
    }

    export function parse(data: string, options?: CSVParserOptions, callback?: CSVParserCallbackFunction): void;
    export function parse(buffer: Buffer, options?: CSVParserOptions, callback?: CSVParserCallbackFunction): void;
    export function parseAsync(data: string, options?: CSVParserOptions): Promise<any[]>;
    export function parseAsync(buffer: Buffer, options?: CSVParserOptions): Promise<any[]>;

}
