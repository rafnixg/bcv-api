# Installation Guide

## Local Installation

1. Clone the repository and create a `.env` file in the root of the project, use `.env.example` as a template
    Remember to replace the values of the variables with your own values.
```bash
git clone https://github.com/rafnixg/bcv-api.git
cd bcv-api
cp .env.example .env
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
```bash
# Windows
venv\Scripts\activate
# Linux
source venv/bin/activate
```

4. Install the dependencies
```bash
pip install -r requirements.txt
```

5. Run the API
```bash
uvicorn bcv_api.main:app --reload
```

6. Open your browser and go to http://localhost:8000

## Using Docker

1. Clone the repository and create a `.env` file in the root of the project, use `.env.example` as a template
    Remember to replace the values of the variables with your own values.
```bash
git clone https://github.com/rafnixg/bcv-api.git
cd bcv-api
cp .env.example .env
```

2. Build the image with the Dockerfile, select the Dockerfile.newrelic file if you want to monitor the application with NewRelic
```bash
# Without newrelic monitoring
docker build -t bcv-api .

# With newrelic monitoring
docker build -t bcv-api -f Dockerfile.newrelic .
```

3. Run the container
```bash
docker run -d --name bcv-api -p 8000:8000 --env-file .env bcv-api:latest
```

4. Open your browser and go to http://localhost:8000