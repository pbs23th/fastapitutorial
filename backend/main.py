#main.py
import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from db.session import engine  # new
from db.base_class import Base  # new
from db.base import Base


def include_router(app):
    app.include_router(general_pages_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():  # new
    print("create_tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()  # new
    return app


app = start_application()


if __name__ == "__main__":
	uvicorn.run('main:app', reload=True)