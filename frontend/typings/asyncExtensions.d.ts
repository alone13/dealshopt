declare module "redis" {
    export interface RedisClient {
        getAsync(...args: any[]): Promise<string>;
        setAsync(...args: any[]): Promise<string>;
        keysAsync(...args: any[]): Promise<any>;
        mgetAsync(...args: any[]): Promise<any>;
        setexAsync(...args: any[]): Promise<string>;
        delAsync(...args: any[]): Promise<string>;
        setnxAsync(key: string, value: string): Promise<boolean>;
        expireAsync(key: string, ttl: number): Promise<number>;

        saddAsync(key: string, ...members: any[]):  Promise<number>;
        sremAsync(key: string, ...members: any[]):  Promise<number>;
        smembersAsync(key: string):  Promise<string[]>;

        hgetAsync(key: string, field: string): Promise<string>;
        hmgetAsync(key: string, ...fields: string[]): Promise<string[]>;
    }

    export interface Multi {
        execAsync(): Promise<string[]>;
    }
}

declare module "fs" {
    export function statAsync(...args: any[]): Promise<any>;
}
