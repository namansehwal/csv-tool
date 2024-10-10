import React, { useState, useEffect } from "react";
import axios from "axios";

function DataTable() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/users/")
      .then((response) => {
        setUsers(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the users!", error);
      });
  }, []);

  const goBack = () => {
    window.history.back();
  };

  return (
    <div>
      <center>
        <button onClick={goBack} style={{ marginBottom: "20px" }}>
          Go Back
        </button>
        <table border="10">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Class</th>
              <th>School</th>
              <th>State</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.class_name}</td>
                <td>{user.school}</td>
                <td>{user.state}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </center>
    </div>
  );
}

export default DataTable;
