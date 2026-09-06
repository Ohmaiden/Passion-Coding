# Ben 10 Alien Database API

A FastAPI backend and Python client for browsing Ben 10 aliens across the franchise: Classic Series, Alien Force, Ultimate Alien, and Omniverse.

Built as a learning project to practice API design, data modeling, and consuming an API from a separate client.

## Features

- 52 aliens across 4 series
- Filter by series
- Search across name, species, home planet, and powers
- Sort results alphabetically by name or series
- Pagination with `skip` and `limit`
- Nested "Ultimate Form" data for aliens with an Ultimatrix evolution
- Alternate names support (e.g. Blitzwolfer / Benwolf)
- Command line client with a menu, connects to the API over HTTP
- Automatic interactive docs via Swagger UI
- Pytest test suite covering all endpoints and query logic

## Tech Stack

- **Backend:** FastAPI, Pydantic
- **Server:** Uvicorn
- **Client:** Python, Requests
- **Testing:** Pytest, HTTPX

## Project Structure

    ben10-alien-api/
    ├── backend/
    │   ├── main.py          # FastAPI app and endpoints
    │   ├── models.py        # Pydantic data models
    │   ├── test_main.py     # Pytest test suite
    │   └── data/
    │       └── aliens.json  # Alien dataset
    ├── client/
    │   └── client.py        # CLI client, consumes the API
    └── README.md

## Setup

Clone the repo, then from the project root:

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install fastapi uvicorn requests pytest httpx

## Running the API

    cd backend
    python -m uvicorn main:app --reload

Interactive docs available at `http://127.0.0.1:8000/docs`

## Running the Client

In a separate terminal, with the API running and the venv active:

    cd client
    python -m client

## Running Tests

    cd backend
    python -m pytest

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/aliens` | List all aliens. Supports `series`, `search`, `sort_by`, `skip`, `limit` query params |
| GET | `/aliens/random` | Get one random alien |
| GET | `/aliens/{name}` | Get one alien by name or alternate name |

## Disclaimer

This is an unofficial, fan made educational project. Ben 10 and all associated aliens, names, and characters are property of Cartoon Network / Warner Bros. Discovery. This project is not affiliated with or endorsed by the rights holders, and exists purely to practice API development.
