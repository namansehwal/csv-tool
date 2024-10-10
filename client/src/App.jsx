import React, { useState } from "react";
import axios from "axios";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import DataTable from "./DataTable";

function Home() {
  const [csvFile, setCsvFile] = useState(null);
  const [uploadSuccess, setUploadSuccess] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const handleFileChange = (e) => {
    setCsvFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!csvFile) {
      setErrorMessage("Please select a CSV file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", csvFile);

    try {
      const response = await axios.post(
        "http://localhost:8000/api/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      if (response.status === 201) {
        setUploadSuccess(true);
        setErrorMessage("");
      }
    } catch (error) {
      setErrorMessage("There was an error uploading the file.");
      console.error(error);
    }
  };

  return (
    <div className="App">
      <center>
        <h1>CSV Uploader Tool</h1>
        <form onSubmit={handleSubmit}>
          <input type="file" accept=".csv" onChange={handleFileChange} />
          <button type="submit">Upload CSV</button>
        </form>
        {uploadSuccess && <p>File uploaded successfully!</p>}
        {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
        <Link to="/data-table">
          <button>View Data Table</button>
        </Link>
      </center>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/data-table" element={<DataTable />} />
      </Routes>
    </Router>
  );
}

export default App;
