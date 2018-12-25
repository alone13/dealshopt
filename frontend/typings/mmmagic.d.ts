declare module "mmmagic" {

    export class Magic {
        constructor(flags?: number);
        constructor(magicPath?: string, flags?: number);
        detectFile(path: string, callback?: (err: Error, result: string) => void): void;
        detectFileAsync(path: string): Promise<string>;
        detect(buf: Buffer, callback?: (err: Error, result: string) => void): void;
        detectAsync(buf: Buffer): Promise<string>;
    }

    /**
     * No flags (default for Windows)
     */
    export var MAGIC_NONE: number;
    /**
     * Turn on debugging
     */
    export var MAGIC_DEBUG: number;
    /**
     * Follow symlinks (default for *nix)
     */
    export var MAGIC_SYMLINK: number;
    /**
     * Look at the contents of devices
     */
    export var MAGIC_DEVICES: number;
    /**
     * Return the MIME type
     */
    export var MAGIC_MIME_TYPE: number;
    /**
     * Return all matches
     */
    export var MAGIC_CONTINUE: number;
    /**
     * Print warnings to stderr
     */
    export var MAGIC_CHECK: number;
    /**
     * Restore access time on exit
     */
    export var MAGIC_PRESERVE_ATIME: number;
    /**
     * Don't translate unprintable chars
     */
    export var MAGIC_RAW: number;
    /**
     * Return the MIME encoding
     */
    export var MAGIC_MIME_ENCODING: number;
    /**
     * MAGIC_MIME_TYPE|MAGIC_MIME_ENCODING
     */
    export var MAGIC_MIME: number;
    /**
     * Return the Apple creator and type
     */
    export var MAGIC_APPLE: number;
    /**
     * Don't check for tar files
     */
    export var MAGIC_NO_CHECK_TAR: number;
    /**
     * Don't check magic entries
     */
    export var MAGIC_NO_CHECK_SOFT: number;
    /**
     * Don't check application type
     */
    export var MAGIC_NO_CHECK_APPTYPE: number;
    /**
     * Don't check for elf details
     */
    export var MAGIC_NO_CHECK_ELF: number;
    /**
     * Don't check for text files
     */
    export var MAGIC_NO_CHECK_TEXT: number;
    /**
     * Don't check for cdf files
     */
    export var MAGIC_NO_CHECK_CDF: number;
    /**
     * Don't check tokens
     */
    export var MAGIC_NO_CHECK_TOKENS: number;
    /**
     * Don't check text encodings
     */
    export var MAGIC_NO_CHECK_ENCODING: number;
}
