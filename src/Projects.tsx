import * as React from "react";
import { ProjectData, SERVER } from "./api";

export interface NameById {
  [key: number]: string;
}

interface ProjectsProps {
  selectedUser?: number;
  nameById: NameById;
}

export default function Projects({ selectedUser, nameById }: ProjectsProps) {
  const [projects, setProjects] = React.useState<ProjectData[] | null>(() => null);
  const [hasMoreResults, setHasMoreResults] = React.useState<boolean>(false);
  const [error, setError] = React.useState<string | null>(null);

  const fetchProjects = React.useCallback((startAfter?: ProjectData, overwrite = false) => {
    SERVER.getProjects({ pageSize: 5, startAfter, userId: selectedUser?.toString() }).then((page) => {
      setError(null);
      if (overwrite) {
        setProjects(_ => ([...(page.projects ?? [])]));
      } else {
        setProjects(projects => [...(projects ?? []), ...page.projects]);
      }
      setHasMoreResults(page.hasMoreResults);
    }).catch((err) => {
      setError(err.message);
    });
  }, [selectedUser]);

  const loadMore = React.useCallback(() => {
    const start = projects?.length ? projects[projects.length - 1] : undefined;
    fetchProjects(start);
  }, [projects, fetchProjects])

  React.useEffect(() => {
    fetchProjects(undefined, true);
  }, [selectedUser, fetchProjects]);

  if (error) {
    return (
      <div className="error-overlay">
        <h1>Server error:</h1>
        <pre>{error}</pre>
      </div>
    );
  }

  return (
    <div className="projects">
      {projects?.length === 0 && (<div>No projects found.</div>)}
      {projects?.map(project => (
        <div className="project" key={`project-${project.id}`}>
          <div>(ID {project.id}) {project.title}</div><div>{nameById[project.creatorId]}</div>
        </div>
      ))}
      <button disabled={!hasMoreResults} onClick={loadMore}>{projects?.length ? `${projects.length} Project(s) Loaded - ` : ''}Load more</button>
    </div>
  );
}