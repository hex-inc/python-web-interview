import { ProjectData, UserData } from "./types";

export interface ProjectsResponse {
  projects: ProjectData[];
  hasMoreResults: boolean;
}

const API_BASE = `http://127.0.0.1:${process.env.REACT_APP_API_PORT || "5000"}`;

class DefaultServer {
  async getUsers(): Promise<UserData[]> {
    const response = await fetch(`${API_BASE}/api/users`);
    return response.json();
  }

  async getProjects(options?: {
    userId?: string;
    startAfter?: ProjectData;
    pageSize?: number;
  }): Promise<ProjectsResponse> {
    const url = new URL(`${API_BASE}/api/projects`);

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
