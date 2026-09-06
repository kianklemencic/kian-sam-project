import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/incidents")
      .then((response) => response.json())
      .then((data) => {
        setIncidents(data);
      })
      .catch((error) => {
        console.error("Error fetching incidents:", error);
      });
  }, []);

  return (
    <main>
      <h1>Operations Dashboard</h1>

      <h2>Incidents</h2>

      {incidents.map((incident) => (
        <div key={incident.id}>
          <h3>{incident.title}</h3>
          <p>Priority: {incident.priority}</p>
          <p>Status: {incident.status}</p>
        </div>
      ))}
    </main>
  );
}

export default App;