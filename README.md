<div align="center">

# FastAPI Boilerplate Generator

**Generate a complete, runnable FastAPI backend from a JSON schema — in one command.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CrestXcode/API-BOILERPLATE-GENERATOR?style=for-the-badge&color=orange)](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/stargazers)

<br/>

> Stop writing the same FastAPI setup over and over.  
> Define your models in JSON → get a fully working backend instantly.

</div>

---

## The Problem

Every new FastAPI project starts the same way — setting up folders, writing SQLAlchemy models, wiring CRUD routes, configuring the database, writing `main.py`... It's tedious, repetitive, and eats time you could spend building actual features.

## The Solution

**One JSON file. One command. A complete, runnable FastAPI backend.**

```bash
python -m generator.cli myapp --json schema.json --db --install --run
```

Your API is live at `http://127.0.0.1:8000/docs`. Done.

---

## Demo

[![Demo](https://asciinema.org/a/CEoY84prkbHqUadv.svg)](https://asciinema.org/a/CEoY84prkbHqUadv)

---

## Features

- **CLI-based** — one command scaffolds an entire project
- **JSON → SQLAlchemy models** — no manual ORM writing
- **Auto CRUD routes** — GET, POST, PUT, DELETE for every model, zero boilerplate
- **Database auto-setup** — SQLite configured and initialized out of the box
- **Dependency installation** — `--install` flag handles `pip install` automatically
- **One-command server start** — `--run` gets you to live interactive docs immediately
- **Clean project structure** — ready to extend, not a mess to untangle

---

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the repo

```bash
git clone https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR.git
cd API-BOILERPLATE-GENERATOR
```

### 2. Define your schema

Edit `schema.json` (one is already included so you can try it right away):

```json
{
  "models": {
    "User": { "id": "int", "name": "str", "email": "str" },
    "Item": { "id": "int", "name": "str", "price": "float" }
  },
  "routes": ["User", "Item"]
}
```

### 3. Generate your backend

```bash
python -m generator.cli myapp --json schema.json --db --install --run
```

### 4. Open your interactive API docs

```
http://127.0.0.1:8000/docs
```

That's it — full CRUD API with database, live in seconds.

---

## CLI Reference

```
python -m generator.cli <project_name> --json <schema_file> [options]
```

| Flag | Description |
|------|-------------|
| `<project_name>` | Name of the output folder to generate |
| `--json` | Path to your JSON schema file |
| `--db` | Initialize the SQLite database |
| `--install` | Auto-install all required Python dependencies |
| `--run` | Start the FastAPI development server after generation |

---

## Generated Project Structure

```
myapp/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # DB engine & session config
│   ├── models.py        # SQLAlchemy ORM models
│   └── routes/
│       ├── user.py      # Full CRUD for User
│       └── item.py      # Full CRUD for Item
└── requirements.txt
```

---

## What Gets Generated

| File | What it contains |
|------|-----------------|
| `app/models.py` | SQLAlchemy ORM classes for each model in your schema |
| `app/routes/*.py` | GET, POST, PUT, DELETE endpoints per model |
| `app/database.py` | SQLite engine, Base declaration, and session factory |
| `app/main.py` | FastAPI app with all routers registered and ready |
| `requirements.txt` | All dependencies: fastapi, uvicorn, sqlalchemy, etc. |

---

## Running Manually

If you skipped `--run`, start the server yourself:

```bash
cd myapp
uvicorn app.main:app --reload
```

Then open: `http://127.0.0.1:8000/docs`

---

## Roadmap

- [x] JSON → SQLAlchemy model generation
- [x] Auto CRUD route generation
- [x] Database auto-setup
- [x] One-command dependency install & server start
- [ ] Pydantic v2 schema generation (request/response models)
- [ ] JWT authentication support
- [ ] PostgreSQL & MySQL support
- [ ] Docker / docker-compose output
- [ ] Interactive CLI mode (no JSON file needed)
- [ ] PyPI package — `pip install fastapi-boilerplate-gen`

---

## Contributing

Contributions are very welcome! Here's how:

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-idea`
3. Commit your changes
4. Open a Pull Request

Bug reports and ideas via [Issues](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/issues) are just as appreciated.

---

## Show Your Support

If this saved you time, a star helps other developers find it.

[![Star this repo](https://img.shields.io/github/stars/CrestXcode/API-BOILERPLATE-GENERATOR?style=social)](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/stargazers)

---

## License

MIT © [CrestXcode](https://github.com/CrestXcode)