<div align="center">

# FastAPI Boilerplate Generator

**Generate a complete FastAPI backend from a JSON schema — in seconds.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/CrestXcode/API-BOILERPLATE-GENERATOR?style=for-the-badge&color=orange)](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/stargazers)

<br/>

> Stop writing the same FastAPI setup over and over.  
> Define your models in JSON → get a fully working backend instantly.

<br/>

[![Demo](https://img.shields.io/badge/▶%20Watch%20Demo-Click%20Here-blueviolet?style=for-the-badge)](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/blob/main/demo.mp4)

</div>

---

## The Problem

Every new FastAPI project starts the same way — setting up folders, writing SQLAlchemy models, wiring CRUD routes, configuring the database, writing `main.py`... It's tedious. It's repetitive. And it adds up.

## The Solution

**One JSON file. One command. A complete, runnable FastAPI backend.**

```bash
python -m generator.cli myapp --json schema.json --db --install --run
```

That's it. Your API is live at `http://127.0.0.1:8000/docs`.

---

## What Gets Generated

Given a simple schema like this:

```json
{
  "models": {
    "User": { "id": "int", "name": "str", "email": "str" },
    "Item": { "id": "int", "name": "str", "price": "float" }
  },
  "routes": ["User", "Item"]
}
```

The CLI automatically produces:

| Output | Description |
|--------|-------------|
|  `app/models.py` | SQLAlchemy ORM models |
|  `app/routes/` | Full CRUD routes for every model |
|  `app/database.py` | Database config & session setup |
|  `app/main.py` | Ready-to-run FastAPI app |
|  `requirements.txt` | All dependencies listed |

---

## Installation

```bash
git clone https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR.git
cd API-BOILERPLATE-GENERATOR
```

No extra setup — just Python 3.8+.

---

## Usage

### Basic

```bash
python -m generator.cli myapp --json schema.json
```

### Full Power Mode

```bash
python -m generator.cli myapp --json schema.json --db --install --run
```

| Flag | What it does |
|------|--------------|
| `--json` | Path to your schema JSON file |
| `--db` | Initializes the SQLite database |
| `--install` | Installs all required dependencies |
| `--run` | Starts the FastAPI server immediately |

---

## Try It Right Now

1. Clone the repo
2. Run the command above with the included `schema.json`
3. Open `http://127.0.0.1:8000/docs` — your API is ready

---

## Generated Project Structure

```
myapp/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # DB engine & session
│   ├── models.py        # SQLAlchemy models
│   └── routes/
│       ├── user.py      # CRUD for User
│       └── item.py      # CRUD for Item
└── requirements.txt
```

---

## Roadmap

- [x] JSON to SQLAlchemy model generation
- [x] Auto CRUD route generation
- [x] One-command database setup
- [x] Auto dependency installation
- [ ] Pydantic schema generation
- [ ] JWT authentication support
- [ ] Docker / docker-compose output
- [ ] PostgreSQL & MySQL support
- [ ] PyPI package (`pip install fastapi-boilerplate-gen`)

---

## Contributing

Contributions are welcome! If you'd like to add a feature, fix a bug, or improve the docs:

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-idea`)
3. Commit your changes
4. Open a Pull Request

Ideas and feedback via [Issues](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/issues) are also very welcome.

---

## Show Your Support

If this saved you time, a star goes a long way — it helps other developers find this tool.

[![Star this repo](https://img.shields.io/github/stars/CrestXcode/API-BOILERPLATE-GENERATOR?style=social)](https://github.com/CrestXcode/API-BOILERPLATE-GENERATOR/stargazers)

---

## License

MIT © [CrestXcode](https://github.com/CrestXcode)