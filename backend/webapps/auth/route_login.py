from apis.version1.route_login import login_for_access_token
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from core.config import settings
from fastapi import HTTPException
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from webapps.auth.forms import LoginForm
from fastapi_login import LoginManager

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

manager = LoginManager(settings.SECRET_KEY, token_url='/token')

@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
async def login(request: Request, db: Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            # response = templates.TemplateResponse("general_pages/homepage.html", form.__dict__)
            response = responses.RedirectResponse(
                "/?msg=Successfully-login", status_code=status.HTTP_302_FOUND
            )
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)

