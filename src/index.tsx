import * as React from "react";
import { render } from "react-dom";

import App from "./App";
import { PROJECTS, USERS } from "./api/data";
import { ProjectData, ProjectsResponse, SERVER, UserData } from "./api";

const rootElement = document.getElementById("root");
render(<App />, rootElement);

(window as any).test = () => {
  const testUser = async (user?: UserData) => {
    const pageSize = 5;
    const userString = user != null ? `User ${user.name} (ID: ${user.id})` : `All users`;
    let totalCountFromApi = 0;
    let hasMoreResults = true;
    let lastProject: ProjectData | undefined = undefined;

    while (hasMoreResults) {
      const page: ProjectsResponse = await SERVER.getProjects({ pageSize, startAfter: lastProject, userId: user?.id?.toString() });
      if (page.hasMoreResults && page.projects.length < pageSize) {
        console.log(
          `❌ ${userString} // Improperly sized page - hasMoreResults: true but results.length < pageSize`
        );
        console.groupEnd();
        return;
      }
      totalCountFromApi += page.projects.length;
      hasMoreResults = page.hasMoreResults;
      lastProject = page.projects[page.projects.length - 1];
    }

    const filterCallback = user ? (project: ProjectData) => project.creatorId === user.id : undefined;
    const totalCountFromRepo = filterCallback ? PROJECTS.filter(filterCallback).length : PROJECTS.length;

    if (totalCountFromApi !== totalCountFromRepo) {
      console.log(`❌ ${userString} // Mismatch: API count = ${totalCountFromApi}, Repo count = ${totalCountFromRepo}`);
    } else {
      console.log(`✅ ${userString} // Counts match: ${totalCountFromApi}`);
    }
  }
  Promise.all([...USERS.map(testUser), testUser()]);
}