from fastapi import APIRouter, Form, Request, HTTPException, status
from fastapi_sqlalchemy import db
from app.dependency import paginate
from models.models import Drugs, History
from models.schema import DrugsSchema, HistorySchema
import json
from starlette.templating import Jinja2Templates


# Defining the common routing for Drugs API section
router = APIRouter()


# Initializing Jinja Templates
templates = Jinja2Templates(directory="templates")


# Saving data from "drugs.json" dataset to data variable
with open("constants/drugs.json") as f:
    data = json.load(f)
data_length = len(data)


@router.get("/drugs", tags=["Drugs List"], response_model=list[DrugsSchema], status_code=status.HTTP_200_OK)
async def drugs_list(request: Request, page_num: int = 1, page_size: int = 10):
    """
    API Category: GET \n
    API Endpoint: /drugs \n
    API Description: This api endpoint provides the list of drugs data \n
    """
    try:
        response = paginate(page_num, page_size, data=data, data_length=data_length, url="drugs")
        return templates.TemplateResponse("drug-list.html", {"request": request, "response": response})
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail=error)


@router.get("/search", tags=["Search Page"], status_code=status.HTTP_200_OK)
async def get_search(request: Request):
    """
    API Category: GET \n
    API Endpoint: / \n
    API Description: This api endpoint provides the homepage with search functionality \n
    """
    try:
        return templates.TemplateResponse("home.html", {"request": request})
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail=error)


@router.post("/search", tags=["Search Page"], response_model=list[DrugsSchema], status_code=status.HTTP_200_OK)
async def post_search(request: Request, search_value: str = Form(...), page_num: int = 1, page_size: int = 10):
    """
    API Category: POST \n
    API Endpoint: /search \n
    API Description: This API endpoint posts the search query into the backend system to filter out that particular 
        search value from the given dataset
    """
    try:
        result = [x for x in data if search_value.lower().strip() in x['name'].lower() or search_value.lower().strip() in '\t'.join(x['diseases'])]
        history = History(name=search_value)
        db.session.add(history)
        db.session.commit()
        return templates.TemplateResponse("result.html", {"request": request, "result": result})
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail=error)


@router.get("/drugs-v2/", tags=["Drugs Database API"], response_model=list[DrugsSchema], status_code=status.HTTP_200_OK)
async def get_drugs_v2(request: Request):
    """
    API Category: POST \n
    API Endpoint: /drugs-v2 \n
    API Description: This api endpoint provides the list of all the drugs from the database
    """
    try:
        drugs_result = db.session.query(Drugs).all()
        return drugs_result
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail=error)


@router.get("/history/", tags=["History Searches Database API"], response_model=list[HistorySchema], status_code=status.HTTP_200_OK)
async def get_history(request: Request, page_num: int = 1, page_size: int = 10):
    """
    API Category: POST \n
    API Endpoint: /history \n
    API Description: This api endpoint provides the list of all the searches from the database
    """
    try:
        history = db.session.query(History).all()
        response = paginate(page_num, page_size, data=history, data_length=len(history), url="history")
        return templates.TemplateResponse("history.html", {"request": request, "response": response})
        return response(response, status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail=error)
