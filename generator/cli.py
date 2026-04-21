import os
import json
import typer
import subprocess
import sys

app = typer.Typer()


def create_folder_structure(name):
    os.makedirs(name, exist_ok=True)
    os.makedirs(f"{name}/app/models", exist_ok=True)
    os.makedirs(f"{name}/app/routes", exist_ok=True)
    os.makedirs(f"{name}/app/schemas", exist_ok=True)

    # create __init__.py everywhere
    for path in ["app", "app/models", "app/routes", "app/schemas"]:
        open(f"{name}/{path}/__init__.py", "w").close()


def create_requirements(name):
    with open(f"{name}/requirements.txt", "w") as f:
        f.write("fastapi\nuvicorn\npydantic\nsqlalchemy\n")


def create_database(name):
    with open(f"{name}/app/database.py", "w") as f:
        f.write("""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""")


def generate_models(name, models):
    type_mapping = {
        "str": "String",
        "int": "Integer",
        "float": "Float"
    }

    for model_name, fields in models.items():
        file = f"{name}/app/models/{model_name.lower()}.py"

        with open(file, "w") as f:
            f.write("from sqlalchemy import Column, Integer, String, Float\n")
            f.write("from app.database import Base\n\n")

            f.write(f"class {model_name}(Base):\n")
            f.write(f"    __tablename__ = '{model_name.lower()}s'\n")
            f.write("    id = Column(Integer, primary_key=True, index=True)\n")

            for field, field_type in fields.items():
                if field == "id":
                    continue
                sql_type = type_mapping.get(field_type, "String")
                f.write(f"    {field} = Column({sql_type})\n")


def generate_schemas(name, models):
    py_map = {"str": "str", "int": "int", "float": "float"}

    for model_name, fields in models.items():
        file = f"{name}/app/schemas/{model_name.lower()}.py"

        with open(file, "w") as f:
            f.write("from pydantic import BaseModel\n\n")

            # Base
            f.write(f"class {model_name}Base(BaseModel):\n")
            for field, field_type in fields.items():
                if field == "id":
                    continue
                f.write(f"    {field}: {py_map.get(field_type, 'str')}\n")

            # Create
            f.write(f"\nclass {model_name}Create({model_name}Base):\n    pass\n")

            # Response
            f.write(f"\nclass {model_name}Response({model_name}Base):\n")
            f.write("    id: int\n\n")
            f.write("    class Config:\n")
            f.write("        from_attributes = True\n")


def generate_routes(name, models):
    for model_name in models.keys():
        file = f"{name}/app/routes/{model_name.lower()}.py"

        with open(file, "w") as f:
            f.write("from fastapi import APIRouter, Depends\n")
            f.write("from sqlalchemy.orm import Session\n")
            f.write(f"from app.models.{model_name.lower()} import {model_name}\n")
            f.write(f"from app.schemas.{model_name.lower()} import {model_name}Create, {model_name}Response\n")
            f.write("from app.database import get_db\n\n")

            f.write(f"router = APIRouter(prefix='/{model_name.lower()}s', tags=['{model_name}'])\n\n")

            # CREATE
            f.write("@router.post('/', response_model={0}Response)\n".format(model_name))
            f.write(f"def create(item: {model_name}Create, db: Session = Depends(get_db)):\n")
            f.write(f"    db_item = {model_name}(**item.dict())\n")
            f.write("    db.add(db_item)\n    db.commit()\n    db.refresh(db_item)\n    return db_item\n\n")

            # READ
            f.write("@router.get('/', response_model=list[{0}Response])\n".format(model_name))
            f.write(f"def get_all(db: Session = Depends(get_db)):\n")
            f.write(f"    return db.query({model_name}).all()\n")


def create_main(name, models, db):
    file = f"{name}/app/main.py"

    with open(file, "w") as f:
        f.write("from fastapi import FastAPI\n")

        if db:
            f.write("from app.database import Base, engine\n")

        for model in models.keys():
            f.write(f"from app.routes import {model.lower()}\n")

        f.write("\napp = FastAPI()\n\n")

        if db:
            f.write("Base.metadata.create_all(bind=engine)\n\n")

        for model in models.keys():
            f.write(f"app.include_router({model.lower()}.router)\n")


@app.command()
def create(
    name: str,
    json_schema: str = typer.Option(None, "--json"),
    db: bool = typer.Option(False, "--db"),
    install: bool = typer.Option(False, "--install"),
    run: bool = typer.Option(False, "--run"),
):
    create_folder_structure(name)
    create_requirements(name)

    if db:
        create_database(name)

    models = {}
    if json_schema:
        with open(json_schema) as f:
            models = json.load(f).get("models", {})

    if db and models:
        generate_models(name, models)
        generate_schemas(name, models)
        generate_routes(name, models)

    create_main(name, models, db)

    if install:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", f"{name}/requirements.txt"])

    if run:
        subprocess.run(["uvicorn", "app.main:app", "--reload"], cwd=name)

    typer.echo(f"Project '{name}' ready!")


if __name__ == "__main__":
    app()