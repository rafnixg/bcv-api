# BCV Exchange Rate API [WIP]

https://bcv-api.rafnixg.dev

## Documentation

- Swagger UI: https://bcv-api.rafnixg.dev/docs
- OpenAPI: https://bcv-api.rafnixg.dev/openapi.json

## Description
This API is used to get the exchange rate of the BCV (Central Bank of Venezuela).
This API is a simple REST API that returns the exchange rate of the BCV in JSON format.

## Installation
1. Clone the repository
```bash
git clone https://github.com/rafnixg/bcv-api.git
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
