/// <reference path="../typings/izischool.d.ts"/>

import { PageLogicBase } from "./pageLogicBase";
import { Dependency } from "../lib/framework/ioc/dependency";
import { ApiListResponse, PagedApiRequest } from "../lib/api/apiBase";
import { ICourseApi } from "../lib/api/courseApi";
import { Course } from "../lib/api/models";

export interface ICoursePageLogic {
    getCourses(request: PagedApiRequest): Promise<ApiListResponse<Course>>;
}

@Dependency.register()
export class CoursePageLogic extends PageLogicBase implements ICoursePageLogic {
    static $inject: string[] = ["CourseApi"];
    private courseApi: ICourseApi;
    constructor(
        courseApi: ICourseApi
    ) {
        super();
        this.courseApi = courseApi;
    }

    public async getCourses(request: PagedApiRequest): Promise<ApiListResponse<Course>> {
        const courses = await this.courseApi.getCourses(request);
        return courses;
    }
}
