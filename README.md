# CSV Uploader Tool

This project is a simple CSV uploader tool built using **Django**, **React**, **SQLite**, and **Docker**. The tool allows users to upload CSV files and maps the uploaded data to a predefined database structure. It also includes basic operations like displaying the mapped data.

## Features

- Upload CSV files and map them to a predefined database structure.
- Handle multiple classes and states for each entry.
- Simple UI for uploading and viewing results.
- Dockerized setup for easy deployment.

## Tech Stack

- **Backend**: Django, SQLite
- **Frontend**: React
- **Containerization**: Docker

## Installation and Setup

Follow the steps below to set up and run the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/namansehwal/csv-tool.git
   cd csv-tool
   ```

2. **Run Docker:**
   Make sure Docker is installed on your system. You can then build and run the project using Docker Compose.

   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   Once the containers are up, the app should be running. Open your browser and navigate to:

   ```
   http://localhost:5174
   ```

   The React frontend will be served on this URL.

4. **Backend API:**
   The Django backend will be running on:

   ```
   http://localhost:8000
   ```

5. **Stopping the application:**
   To stop the application, run:
   ```bash
   docker-compose down
   ```

## How to Use

A sample file, test.csv, is attached to this project for testing purposes. Follow these steps to test the application:

1. Start the application using Docker as explained in the setup steps above.
2. Navigate to http://localhost:5174 in your browser.
3. Upload the provided test.csv file through the user interface.
4. Once uploaded, the data will be mapped to the predefined database structure and displayed in the application.

## Notes

- Ensure the CSV headers align with the expected structure.
- The app will map names, classes, schools, and states based on predefined rules.

## What I would have done if I had more time

1. **Validation Improvements**: Add advanced validation to ensure uploaded CSVs have valid formats and handle potential issues like missing fields or invalid data types.
2. **Error Handling**: Better error messaging for the user interface to show precise reasons for upload failures, such as mismatched headers or incomplete data.
3. **Scalability**: Implement pagination for large CSV files, optimizing both the frontend and backend to handle large datasets efficiently.
4. **User Authentication**: Add user authentication to allow multiple users to upload and manage their CSV files separately.
5. **Database Expansion**: Extend the database structure to allow for more complex mappings or relational data handling.
6. **UI/UX Enhancements**: Improve the frontend design for a better user experience, including a drag-and-drop CSV upload feature and progress indicators during file uploads.
