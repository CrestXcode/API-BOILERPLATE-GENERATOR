# FastAPI Boilerplate Generator CLI

> A simple CLI to generate FastAPI backends from JSON schema in seconds.

---

## Features

* CLI-based backend generator
* JSON to SQLAlchemy model generation
* Automatic database setup
* Auto-generated CRUD routes
* Ready-to-run FastAPI application
* Clean project structure

---

## Installation

```bash
git clone https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR.git
cd API-BOILERPLATE-GENERATOR
```

---

## Usage

```bash
python -m generator.cli myapp --json schema.json --db --install --run
```

---

## Example schema.json

```json
{
  "models": {
    "User": {"id": "int", "name": "str", "email": "str"},
    "Item": {"id": "int", "name": "str", "price": "float"}
  }
}
```

---

## Output

The CLI automatically generates:

* SQLAlchemy models
* CRUD API routes
* Database configuration
* FastAPI application setup

---

## Run Manually

```bash
cd myapp
uvicorn app.main:app --reload
```

---

## API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Demo

<p align="center">
  <img src="demo.gif" alt="Demo" width="800"/>
</p>

---

## Why this tool

Setting up FastAPI projects repeatedly is time-consuming.
This CLI removes boilerplate and lets you focus on building features.

---

## Support

If you find this useful, consider giving it a star.
