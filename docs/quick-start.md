# Quick Start

## Basic Usage

### Get Latest Rate
```bash
curl https://bcv-api.rafnixg.dev/rates/
```

**Response:**
```json
{
  "dollar": 36.5,
  "date": "2025-08-20"
}
```

### Get Rate for Specific Date
```bash
curl https://bcv-api.rafnixg.dev/rates/2025-08-20
```

**Response:**
```json
{
  "dollar": 36.5,
  "date": "2025-08-20"
}
```

### Get Rate History (Last 30 Days)
```bash
curl https://bcv-api.rafnixg.dev/rates/history
```

### Get Rate History for Date Range
```bash
curl "https://bcv-api.rafnixg.dev/rates/history?start_date=2025-02-15&end_date=2025-03-15"
```

**Response:**
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

For complete API documentation visit: [https://bcv-api.rafnixg.dev/docs](https://bcv-api.rafnixg.dev/docs)