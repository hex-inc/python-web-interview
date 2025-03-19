import * as React from "react";
import { SERVER, UserData } from "./api";
import Projects, { NameById } from "./Projects";

export default function Workspace() {
  const [users, setUsers] = React.useState<UserData[]>(() => [])
  const [nameById, setNameById] = React.useState<NameById>(() => ({}));
  const [selectedUser, setSelectedUser] = React.useState<number | undefined>();

  React.useEffect(() => {
    SERVER.getUsers().then((data) => {
      setUsers(data);
      setNameById(data.reduce<NameById>((acc, user) => {
        acc[user.id] = user.name;
        return acc;
      }, {}));
    });
  }, []);

  const onSelectUser = React.useCallback((event: React.ChangeEvent<HTMLSelectElement>) => {
    if (event.target.value === "-1") {
      setSelectedUser(undefined);
    } else {
      setSelectedUser(parseInt(event.target.value));
    }
  }, []);

  return (
    <div className="workspace">
      <h1>My Workspace</h1>
      <div className="header">
        <div>User</div>
        <select onChange={onSelectUser}>
          <option value={-1}>ALL</option>
          {users.map(user => (
            <option key={`user-${user.id}`} value={user.id}>{user.name}</option>
          ))}
        </select>
      </div>
      <Projects key={`projects-${selectedUser}`} selectedUser={selectedUser} nameById={nameById} />
    </div>
  );
}