import { ProjectData, UserData } from "./types";

export interface ProjectsResponse {
  projects: ProjectData[];
  hasMoreResults: boolean;
}

const PROJECTS_REQUEST_TIMEOUT_MS = 1000;

export const PROJECTS_REQUEST_TIMEOUT_MESSAGE =
  "Request timed out. Possible infinite loop in api/pagination.py.";

export class ProjectsRequestTimeoutError extends Error {
  constructor(message: string = PROJECTS_REQUEST_TIMEOUT_MESSAGE) {
    super(message);
    this.name = "ProjectsRequestTimeoutError";
  }
}

function isAbortError(error: unknown): boolean {
  return (
    typeof error === "object" &&
    error !== null &&
    "name" in error &&
    error.name === "AbortError"
  );
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

    if (options?.userId) {
      url.searchParams.append('userId', options.userId);
    }
    if (options?.startAfter?.id) {
      url.searchParams.append('startAfterId', options.startAfter.id.toString());
    }
    if (options?.pageSize) {
      url.searchParams.append('pageSize', options.pageSize.toString());
    }

    const controller = new AbortController();
    const timeoutId = window.setTimeout(() => controller.abort(), PROJECTS_REQUEST_TIMEOUT_MS);

    try {
      const response = await fetch(url, { signal: controller.signal });
      return response.json();
    } catch (error) {
      if (isAbortError(error)) {
        throw new ProjectsRequestTimeoutError();
      }
      throw error;
    } finally {
      window.clearTimeout(timeoutId);
    }
  }
}

export const SERVER = new DefaultServer();
