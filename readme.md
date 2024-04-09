# BCV Exchange Rate API

https://bcv-api.rafnixg.dev

## Description
This API is used to get the exchange rate of the BCV (Central Bank of Venezuela).
This API is a simple REST API that returns the exchange rate of the BCV in JSON format.

## Endpoints
- `/` [GET]: Returns the exchange rate of the BCV in JSON format for today.
- `/<date>` [GET]: Returns the exchange rate of the BCV in JSON format for the specified date. The date must be in the format `YYYY-MM-DD`.
- `/` [POST]: Returns the exchange rate of the BCV in JSON format for today.

## Example
```json
{
    "date": "2021-08-10",
    "dollar": 32.12
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
