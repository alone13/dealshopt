declare module "convict" {
	function convict(schema: convict.Schema): convict.Config;

	module convict {
		interface Schema {
			[name: string]: convict.Schema | {
				default: any;
				doc?: string;
				format?: any;
				env?: string;
				arg?: string;
			};
		}

		interface Config {
			get(name: string): any;
            getProperties(): any;
			default(name: string): any;
			has(name: string): boolean;
			set(name: string, value: any): void;
			load(conf: Object): void;
			loadFile(file: string): void;
			loadFile(files: string[]): void;
			validate(options?: { strict: boolean }): void;
		}
	}

	export = convict;
}
