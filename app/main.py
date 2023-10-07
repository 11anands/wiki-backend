import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_sqlalchemy import DBSessionMiddleware
from app.config import settings
from .routers.v1 import drugs
from starlette.responses import RedirectResponse
from fastapi_profiler import PyInstrumentProfilerMiddleware

# Entry point of application
app = FastAPI()

# Creating a database middleware
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)


# Locating static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# Adding Profiler middleware
app.add_middleware(PyInstrumentProfilerMiddleware)


# Establish and manage various routes
app.include_router(drugs.router)


# Redirect to "/search" incase users enter "/"
@app.get("/")
async def redirect():
    url = app.url_path_for("get_search")
    response = RedirectResponse(url=url)
    return response


# Start logging on app initialization
@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"))
    f_handler = logging.FileHandler('file.log')
    f_handler.setFormatter(logging.Formatter(
        "%(name)s :: %(levelname)-8s :: %(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
