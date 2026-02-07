# Calculator Web App

A simple Python calculator web application built with Flask.

## Features
- Add, subtract, multiply, divide, power, and modulo operations
- Beautiful web interface
- RESTful API backend
- Docker support

## Running Locally

### Prerequisites
- Python 3.11+
- pip

### Setup
```bash
pip install -r requirements.txt
python app.py
```

The app will run on `http://localhost:5000`

## Running with Docker

### Build the image
```bash
docker build -t calculator-app .
```

### Run the container
```bash
docker run -p 5000:5000 calculator-app
```

The app will be accessible at `http://localhost:5000`

## API Endpoint

POST `/calculate`

Request body:
```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

Operations: `add`, `subtract`, `multiply`, `divide`, `power`, `modulo`

Response:
```json
{
  "result": 15,
  "success": true
}
```
