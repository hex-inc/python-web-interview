import { ProjectData, UserData } from "./types";

export interface ProjectsResponse {
  projects: ProjectData[];
  hasMoreResults: boolean;
}

class DefaultServer {
  async getUsers(): Promise<UserData[]> {
    const response = await fetch('http://127.0.0.1:5000/api/users');
    return response.json();
  }

  async getProjects(options?: {
    userId?: string;
    startAfter?: ProjectData;
    pageSize?: number;
  }): Promise<ProjectsResponse> {
    const url = new URL('http://127.0.0.1:5000/api/projects');

    if (options?.userId != null) {
      url.searchParams.append('userId', options.userId);
    }
    if (options?.startAfter?.id != null) {
      url.searchParams.append('startAfterId', options.startAfter.id.toString());
    }
    if (options?.pageSize != null) {
      url.searchParams.append('pageSize', options.pageSize.toString());
    }

    const response = await fetch(url);
    return response.json();
  }
}

export const SERVER = new DefaultServer();
