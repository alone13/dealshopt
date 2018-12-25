/// <reference path="./express/express.d.ts" />


declare module Express {
    export interface Request {
        files: {
            [fieldname: string]: Multer.File[];
        } | Multer.File[];
        file: Multer.File;
    }

    module Multer {
        export interface File {
            /** Field name specified in the form */
            fieldname: string;
            /** Name of the file on the user's computer */
            originalname: string;
            /** Encoding type of the file */
            encoding: string;
            /** Mime type of the file */
            mimetype: string;
            /** Size of the file in bytes */
            size: number;
            /** The folder to which the file has been saved (DiskStorage) */
            destination: string;
            /** The name of the file within the destination (DiskStorage) */
            filename: string;
            /** Location of the uploaded file (DiskStorage) */
            path: string;
            /** A Buffer of the entire file (MemoryStorage) */
            buffer: Buffer;
        }
    }
}

declare module "multer" {
    import * as express from "express";

    function multer(options?: multer.Options): multer.Multer;

    module multer {
        interface Options {
            dest?: string;
            limits?: {
                fieldNameSize?: number;
                fieldSize?: number;
                fields?: number;
                fileSize?: number;
                files?: number;
                parts?: number;
                headerPairs?: number;
            };
        }

        interface Field {
            name: string;
            maxCount?: number;
        }

        interface Multer {
            single(fieldname: string): express.RequestHandler;
            array(fieldname: string, maxCount?: number): express.RequestHandler;
            fields(fields: Field[]): express.RequestHandler;
            any(): express.RequestHandler;
        }
    }

    export = multer;
}
