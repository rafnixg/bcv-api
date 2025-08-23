# API Reference

## Exchange Rates

### Get Latest Rate
- **GET** `/rates/` - Get the latest exchange rate for USD
- **Response**: `{"dollar": 36.5, "date": "2025-08-20"}`

### Get Rate by Date
- **GET** `/rates/{date}` - Get the exchange rate for a specific date
- **Parameters**: 
  - `date` (path): Date in YYYY-MM-DD format
- **Response**: `{"dollar": 36.5, "date": "2025-08-20"}`

### Get Rate History
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

### Create New Rate (Authenticated)
- **POST** `/rates/` - Create a new rate using the BCV API
- **Authentication**: Bearer token required
- **Response**: `{"dollar": 36.5, "date": "2025-08-20", "id": 1}`

## User Management

### Login
- **POST** `/users/token` - Get access token
- **Parameters**: username/password form data
- **Response**: `{"access_token": "...", "token_type": "bearer"}`

### Get Current User
- **GET** `/users/me` - Get current user information (authenticated)

### Create User
- **POST** `/users/` - Register a new user