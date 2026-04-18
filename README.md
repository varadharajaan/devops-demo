# Flask Elastic Beanstalk Demo

A simple Flask app with HTML, structured logging, and the minimum files needed to deploy from GitHub through AWS CodePipeline to Elastic Beanstalk.

## Project structure

```text
flask-eb-demo/
├── .ebextensions/
│   └── 01_environment.config
├── templates/
│   └── index.html
├── app.py
├── Procfile
├── requirements.txt
├── runtime.txt
└── README.md
```

## What this demo shows

- A basic Flask app with one HTML page
- `/health` endpoint for health checks
- `/error` endpoint to generate a sample error log
- Logging to stdout and to `/var/log/webapp/application.log`
- Elastic Beanstalk environment settings via `.ebextensions`
- CloudWatch log streaming enabled

## Run locally

### 1) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Start the app

```bash
python app.py
```

Open `http://127.0.0.1:5000`

## Push to GitHub

Create an empty GitHub repository first, then run:

```bash
git init
git add .
git commit -m "Initial Flask Elastic Beanstalk demo"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Elastic Beanstalk setup

### Option A: Create the Elastic Beanstalk app in the console

1. Open AWS Elastic Beanstalk.
2. Create application.
3. Platform: **Python**.
4. Upload the source code from this repository or let CodePipeline deploy it later.
5. Create the environment.

### Option B: Let CodePipeline deploy to an existing Elastic Beanstalk environment

Before creating the pipeline, create an Elastic Beanstalk application and environment:

- Application name: `flask-eb-demo`
- Environment name: `flask-eb-demo-prod`
- Platform: Python 3.11

## CodePipeline setup

1. Open AWS CodePipeline.
2. Create pipeline.
3. Source provider: **GitHub (via AWS connection)**.
4. Create or select the GitHub connection.
5. Choose your repository and branch.
6. Skip the build stage for this simple demo.
7. Deploy provider: **Elastic Beanstalk**.
8. Select the Elastic Beanstalk application and environment.
9. Create pipeline.

When you push to `main`, the pipeline should deploy the app to Elastic Beanstalk.

## Logging

The app logs:

- request path and method
- health endpoint access
- intentional errors from `/error`
- unhandled exceptions

### Where to see logs

- Elastic Beanstalk console → your environment → Logs
- CloudWatch Logs if log streaming is enabled
- application file log on the instance: `/var/log/webapp/application.log`

## Useful demo flow

1. Open home page.
2. Open `/health`.
3. Open `/error`.
4. Show Elastic Beanstalk logs.
5. Make a small code change in GitHub.
6. Push.
7. Show CodePipeline execution.
8. Refresh the Elastic Beanstalk URL.

## Useful commands

```bash
# local run
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py

# git
git status
git add .
git commit -m "change message"
git push

# optional: zip bundle for manual upload
zip -r app.zip . -x "*.git*" "*.venv*"
```

## Notes

- For a real production app, add tests, secrets management, and stronger environment separation.
- For this demo, the source bundle is deployed directly without a build stage.
