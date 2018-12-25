/// <reference path="./node/node.d.ts"/>

interface SearchParams {
    external_id?: string;
    email?: string;
}

declare module "node-zendesk" {

    export interface CallbackFunction<T> {
        (err: any, request: any, result: T): void;
    }

    export interface ZendeskPhotoThumbnail {
      id: number;
      name: string;
      content_url: string;
      content_type: string;
      size: number;
    }
    export interface ZendeskPhoto {
        id: number;
        name: string;
        content_url:  string;
        content_type: string;
        size: number;
        thumbnails: ZendeskPhotoThumbnail[];
    }
    export interface ZendeskUser {
        id: number;
        url: string;
        name: string;
        external_id: string;
        alias: string;
        created_at: string;
        updated_at: string;
        active: boolean;
        verified: boolean;
        shared: boolean;
        shared_agent: boolean;
        locale: string;
        locale_id: number;
        time_zone: string;
        last_login_at: string;
        email: string;
        phone: string;
        signature: string;
        details: string;
        notes: string;
        organization_id: string;
        role: string;
        custom_role_id: number;
        moderator: boolean;
        ticket_restriction: string;
        only_private_comments: boolean;
        tags: string[];
        restricted_agent: boolean;
        suspended: boolean;
        photo: ZendeskPhoto;
        user_fields: { [key: string]: any };
}
    export interface IZendeskClient {
        // 追加の時に以下のリンクを参考に：
        // https://github.com/blakmatrix/node-zendesk
        // https://developer.zendesk.com/rest_api/docs/core/introduction

        users: {
            search(params: SearchParams, callback: CallbackFunction<ZendeskUser[]>): void;
            searchAsync(params: SearchParams): Promise<[any, ZendeskUser[]]>;
        };
    }

    export function createClient(opts?: {
        username: string;
        token: string;
        remoteUri: string;
        oauth?: boolean;
        disableGlobalState?: boolean;
        debug?: boolean;
    }): IZendeskClient;
}
