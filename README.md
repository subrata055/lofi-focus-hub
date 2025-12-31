# Lo-Fi Focus Hub

Step 2: Complete the commit

A minimalist Pomodoro timer web application with ambient vibes and session tracking.

## Features

- **Focus Timer**: 25-minute Pomodoro countdown with Start, Pause, and Reset controls
- **Task Input**: Simple field to track what you're focusing on
- **Vibe Selector**: Choose ambient backgrounds (Rainy, Cafe, Late Night, Forest, Ocean)
- **Session Log**: Automatic saving of completed sessions to SQLite database
- **Modern UI**: Dark mode, glassmorphism design with smooth transitions

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser to `http://localhost:5000`

## Usage

1. Enter what you want to focus on in the task input
2. Select your preferred vibe from the dropdown
3. Click Start to begin your 25-minute focus session
4. Use Pause/Resume as needed
5. When the timer completes, your session is automatically saved
6. View your recent sessions in the log below

The app creates a local SQLite database (`focus_sessions.db`) to store your session history.

## Docker Setup

### Option 1: Using Docker Compose (Recommended)

1. Build and run the container:
   ```
   docker-compose up --build
   ```

2. Open your browser to `http://localhost:5000`

3. To stop the container:
   ```
   docker-compose down
   ```

### Option 2: Using Docker directly

1. Build the image:
   ```
   docker build -t lofi-focus-hub .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 -v $(pwd)/data:/app/data lofi-focus-hub
   ```

### Data Persistence

The Docker setup includes volume mounting to persist your session data:
- Sessions are stored in `./data/focus_sessions.db` on your host machine
- Data persists even when containers are stopped/restarted
- You can backup your sessions by copying the `data` folder

## DockerHub Deployment

The application is also available as a pre-built Docker image on DockerHub.

### Pull and run from DockerHub:

```bash
# Pull the latest image
docker pull subrata055/lofi-focus-hub:latest

# Run with volume mounting for data persistence
docker run -p 5000:5000 -v $(pwd)/data:/app/data subrata055/lofi-focus-hub:latest

# Or use the production docker-compose file
docker-compose -f docker-compose.prod.yml up -d
```

### Jenkins CI/CD Pipeline

The project includes two Jenkins pipeline files:

- `Jenkinsfile` - Basic pipeline for local deployment
- `Jenkinsfile2` - Extended pipeline that builds and pushes to DockerHub

**Jenkins Setup Requirements:**
1. Configure DockerHub credentials in Jenkins with ID: `dockerhub-credentials`
2. Ensure Jenkins agent has Docker and docker-compose installed
3. Configure SonarQube server (optional, currently commented out)

**Pipeline Features:**
- Automated Docker image building
- Push to DockerHub with build number tagging
- Automatic deployment after successful build
- Proper cleanup and error handling