import * as React from "react";
import { render } from "react-dom";

import App from "./App";
import { ProjectData, ProjectsResponse, SERVER, UserData } from "./api";

const rootElement = document.getElementById("root");
render(<App />, rootElement);

// Expected project counts from api/data.py seed data.
const EXPECTED_PROJECT_COUNTS: Record<number, number> = {
  0: 0,
  1: 5,
  2: 15,
  3: 4,
  4: 16,
  5: 14,
  6: 11,
  7: 10,
  8: 12,
  9: 13,
};
const TOTAL_PROJECTS = 100;

(window as any).test = async () => {
  const users = await SERVER.getUsers();

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

    const totalCountFromRepo = user != null ? EXPECTED_PROJECT_COUNTS[user.id] : TOTAL_PROJECTS;

    if (totalCountFromApi !== totalCountFromRepo) {
      console.log(`❌ ${userString} // Mismatch: API count = ${totalCountFromApi}, Repo count = ${totalCountFromRepo}`);
    } else {
      console.log(`✅ ${userString} // Counts match: ${totalCountFromApi}`);
    }
  };

  await Promise.all([...users.map(testUser), testUser()]);
};