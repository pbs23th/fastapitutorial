#main.py
import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.base import api_router
from db.session import engine  # new
from db.base import Base
from webapps.base import api_router as web_app_router
from db.utils import check_db_connected,check_db_disconnected



def include_router(app):
    app.include_router(api_router)


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

@app.on_event("startup")              #new
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")     #new
async def app_shutdown():
    await check_db_disconnected()



if __name__ == "__main__":
	uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)