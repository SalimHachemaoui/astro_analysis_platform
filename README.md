# Astro Analysis Platform

This project is an example of microservices architecture using FastAPI to create an astro analysis platform. It includes multiple services for data collection, analysis, visualization, and notifications. The frontend is developed with Vue.js.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

- `Front-end/astro_analysis_frontend`: Contains the frontend developed in Vue.js.
- `service_data_collection`: Microservice for data collection.
- `service_data_analysis`: Microservice for data analysis.
- `service_visualization`: Microservice for data visualization.
- `service_notification`: Microservice for notifications.
- `docker-compose.yml`: Configuration file to orchestrate the Docker services.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SalimHachemaoui/astro_analysis_platform.git
   cd astro_analysis_platform
   ```

2. Ensure Docker and Docker Compose are installed on your machine.

3. Start the services with Docker Compose:
   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images for each service and start them.

## Accessing the Application

Once all services are running, you can access the frontend application at:
```
http://localhost:8080
```

## Service Descriptions

### Data Collection Service

- **Endpoint to collect data:**
  - URL: `/data/`
  - Method: `POST`
  - Description: Collects data sent in JSON format.

- **Endpoint to get data:**
  - URL: `/data/`
  - Method: `GET`
  - Description: Returns the collected data in JSON format.

### Data Analysis Service

- **Endpoint to analyze data:**
  - URL: `/analyze/`
  - Method: `POST`
  - Description: Analyzes the provided data and returns the results.

### Data Visualization Service

- **Endpoint to visualize data:**
  - URL: `/visualize/`
  - Method: `GET`
  - Description: Generates visualizations from the analyzed data.

### Notification Service

- **Endpoint to create a notification:**
  - URL: `/notifications/`
  - Method: `POST`
  - Description: Creates a new notification.

- **Endpoint to get notifications:**
  - URL: `/notifications/`
  - Method: `GET`
  - Description: Returns the list of notifications.

- **Note:** A notification is automatically generated each time new data is collected via the data collection endpoint.

## Example Workflow

1. **Data Collection:**
   - Send a `POST` request to `/data/` with the data to be collected.
   - **Note:** This will automatically trigger a notification.

2. **Data Analysis:**
   - Send a `POST` request to `/analyze/` with the collected data.
   
3. **Data Visualization:**
   - Access `/visualize/` to see the visualizations of the analyzed data.
   
4. **Notifications:**
   - Check the generated notifications by accessing `/notifications/`.

## Contribution

Contributions are welcome. Please create a new branch for each feature or bug fix and submit a pull request for review.

