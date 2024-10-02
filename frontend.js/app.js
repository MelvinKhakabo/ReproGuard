#sources

import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    // Fetching health resources
    axios.get('http://localhost:8000/api/health-resources/')
      .then(response => setResources(response.data))
      .catch(error => console.error("Error fetching resources:", error));
  }, []);

  return (
    <div className="App">
      <h1>Health Resources</h1>
      <ul>
        {resources.map(resource => (
          <li key={resource.id}>{resource.title}: {resource.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
