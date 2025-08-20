# BCV Exchange Rate API

[BCV API DEMO](https://bcv-api.rafnixg.dev/)

## Swagger UI Documentation

[https://bcv-api.rafnixg.dev/docs](https://bcv-api.rafnixg.dev/docs)

## Description
This API is used to get the exchange rate of the BCV (Central Bank of Venezuela).
This API is a simple REST API that returns the exchange rate of the BCV in JSON format.

## API Endpoints

### Exchange Rates

#### Get Latest Rate
- **GET** `/rates/` - Get the latest exchange rate for USD
- **Response**: `{"dollar": 36.5, "date": "2025-08-20"}`

#### Get Rate by Date
- **GET** `/rates/{date}` - Get the exchange rate for a specific date
- **Parameters**: 
  - `date` (path): Date in YYYY-MM-DD format
- **Response**: `{"dollar": 36.5, "date": "2025-08-20"}`

#### Get Rate History
- **GET** `/rates/history` - Get exchange rate history within a date range
- **Parameters**: 
  - `start_date` (query, optional): Start date in YYYY-MM-DD format
  - `end_date` (query, optional): End date in YYYY-MM-DD format
- **Default behavior**: If no dates provided, returns last 30 days
- **Example**: `/rates/history?start_date=2025-02-15&end_date=2025-03-15`
- **Response**: 
```json
{
  "start_date": "2025-02-15",
  "end_date": "2025-03-15", 
  "rates": [
    {"dollar": 36.5, "date": "2025-03-15"},
    {"dollar": 36.4, "date": "2025-03-14"}
  ]
}
```

#### Create New Rate (Authenticated)
- **POST** `/rates/` - Create a new rate using the BCV API
- **Authentication**: Bearer token required
- **Response**: `{"dollar": 36.5, "date": "2025-08-20", "id": 1}`

### User Management

#### Login
- **POST** `/users/token` - Get access token
- **Parameters**: username/password form data
- **Response**: `{"access_token": "...", "token_type": "bearer"}`

#### Get Current User
- **GET** `/users/me` - Get current user information (authenticated)

#### Create User
- **POST** `/users/` - Register a new user

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
