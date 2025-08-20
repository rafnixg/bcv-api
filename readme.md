# BCV Exchange Rate API
[![Publish Docker Image](https://github.com/rafnixg/bcv-api/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/rafnixg/bcv-api/actions/workflows/docker-image.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/rafnixg/bcv-api)
## Documentation

[https://rafnixg.github.io/bcv-api/](https://rafnixg.github.io/bcv-api/)

## Description
This API is used to get the exchange rate of the BCV (Central Bank of Venezuela).
This API is a simple REST API that returns the exchange rate of the BCV in JSON format.

## Quick Usage

### Get Latest Rate
```bash
curl https://bcv-api.rafnixg.dev/rates/
```

### Get Rate for Specific Date
```bash
curl https://bcv-api.rafnixg.dev/rates/2025-08-20
```

### Get Rate History (Last 30 Days)
```bash
curl https://bcv-api.rafnixg.dev/rates/history
```

### Get Rate History for Date Range
```bash
curl "https://bcv-api.rafnixg.dev/rates/history?start_date=2025-02-15&end_date=2025-03-15"
```

For complete API documentation visit: [https://bcv-api.rafnixg.dev/docs](https://bcv-api.rafnixg.dev/docs)

## Installation
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
git clone
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

## Built With
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Requests](https://docs.python-requests.org/en/master/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Author
- **Rafnix Guzmán** - [rafnixg](https://links.rafnixg.dev?ref=bcv-api)


## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
