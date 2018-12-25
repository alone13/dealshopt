declare module "sharp" {
    import * as stream from "stream";

    /**
     * Constructor to which further methods are chained.
     * @param {string|Buffer} input If present, can be one of:
     *                              Buffer containing JPEG, PNG, WebP, GIF* or TIFF image data, or
     *                              String containing the filename of an image, with most major formats supported.
     */
    function s(input?: string|Buffer): s.Sharp;

    module s {
        interface Sharp extends stream.Duplex {
            /**
             * Crop the resized image to the exact size specified, the default behaviour.
             * @param  {gravity} gravity if present, is a {string} or an attribute of the {sharp.gravity} Object
             */
            crop(gravity?: string): Sharp;
            embed(): Sharp;
            background(color: { r: number, g: number, b: number, a: number }): Sharp;
            resize(width?: number, height?: number): Sharp;
            interpolateWith(interolator: string): Sharp;
            rotate(angle?: number): Sharp;
            quality(quality: number): Sharp;
            jpeg(): Sharp;
            png(): Sharp;
            toFormat(a: any): Sharp;

            on(event: string, listener: Function): this;
            toBuffer(callback?: (error: Error, buffer: Buffer) => void): Sharp;
        }

        export class gravity {
            static north: string;
            static east: string;
            static south: string;
            static west: string;
            static center: string;
            static centre: string;
        }

        export class interpolator {
            /**
             *  Use nearest neighbour interpolation, suitable for image enlargement only.
             */
            static nearest: string;

            /**
             *  Use bilinear interpolation, the default and fastest image reduction interpolation.
             */
            static bilinear: string;

            /**
             *  Use bicubic interpolation, which typically reduces performance by 5%.
             */
            static bicubic: string;

            /**
             *  Use VSQBS interpolation, which prevents "staircasing" and typically reduces performance by 5%.
             */
            static vertexSplitQuadraticBasisSpline: string;

            /**
             *  Use LBB interpolation, which prevents some "acutance" and typically reduces performance by a factor of 2.
             */
            static locallyBoundedBicubic: string;

            /**
             *  Use Nohalo interpolation, which prevents acutance and typically reduces performance by a factor of 3.
             */
            static nohalo: string;
        }

    }

    export = s;
}
