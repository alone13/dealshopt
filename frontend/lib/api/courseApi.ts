/// <reference path="../../typings/izischool.d.ts"/>

/* Import section */
import { Dependency } from "../framework/ioc/dependency";
import { ApiBase, ApiListResponse, PagedApiRequest } from "./apiBase";
import { IInfrastructureSettings } from "../configuration/infrastructureSettings";
import { Course } from "./models";

/* Api input parameters section */
export interface CreateCourseData {
    name: string;
}

export interface UpdateCourseParams {
    name?: string;
}


/* Api interface section */
export interface ICourseApi {
    getCourses(params?: PagedApiRequest): Promise<ApiListResponse<Course>>;
    getCourse(courseId: number): Promise<Course>;
    createCourse(data: CreateCourseData): Promise<Course>;
    updateCourse(courseId: number, params: UpdateCourseParams): Promise<Course>;
    deleteCourse(courseId: number): Promise<void>;
}

/* Api implementation section */
@Dependency.register()
export class CourseApi extends ApiBase implements ICourseApi {
    static $inject: string[] = ["InfrastructureSettings", "RequestId"];
    constructor(
      infrastructureSettings: IInfrastructureSettings,
      requestId: string
    ) {
        super(
          infrastructureSettings.endpoints.apps,
          requestId
        );
    }

    public async getCourses(params?: PagedApiRequest): Promise<ApiListResponse<Course>> {
        const response = await this.get<ApiListResponse<Course>>("/course/course/", params);
        return response.body!;
    }

    public async getCourse(courseId: number): Promise<Course> {
        const response = await this.get<Course>(`/course/course/${courseId}/`);
        return response.body!;
    }

    public async createCourse(data: CreateCourseData): Promise<Course> {
        const response = await this.post<CreateCourseData, Course>("/course/course/", data);
        return response.body!;
    }

    public async updateCourse(courseId: number, params: UpdateCourseParams): Promise<Course> {
        const response = await this.put<UpdateCourseParams, Course>(`/course/course/${courseId}/`, params);
        return response.body!;
    }

    public async deleteCourse(courseId: number): Promise<void> {
        await this.delete<any, void>(`/course/course/${courseId}/`);
    }
}
