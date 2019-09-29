from typing import List

from fastapi import Depends, FastAPI , HTTPException
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response ,HTMLResponse
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from sql_app import database as db
from sql_app import models as models
from sql_app import crud as crud
from sql_app import schemas as schemas


html = '''
    <!doctype html>
    <head>
        <title> STAGE 1 </title>
    </head>
    <body>
        <div align='center'>
        <h3> PLEASE INPUT LAT AND LONG FOR DATA  </h3>
        <div >
        <form action="/get_location"  method="get" target="_self">
            longitude here : <input name="longitude" type = "decimal"><br>
            latitude here : <input name="latitude" type = "decimal"><br>
            <input type="submit" value="submit info">
        </form>
        </div>
        </div>
    </body>
    '''


app = FastAPI()
# templates = Jinja2Templates(directory="templates")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.sess = db.SessionLocal()
        response = await call_next(request)
    finally:
        request.state.sess.close()
    return response

def get_sess(request: Request):
    return request.state.sess

@app.get("/")
async def root():
    return {"root":"page"}


@app.get("/index")
async def root():
    return HTMLResponse(html)


@app.get("/get_pin")
async def get_pin(pin: str = None, sess: Session = Depends(get_sess)):
    temp = crud.getby_pin(sess,pin)
    return {"pin": temp}

# @app.get_like("/get_like")
# async def get_like(longitude: float = None , latitude: float = None , sess):


@app.get("/get_location")
async def get_location(latitude: float = 0.0,longitude: float = 0.0 , sess: Session = Depends(get_sess)):
    data = crud.getby_longlang(sess = sess, latitude=latitude ,longitude= longitude)
    json_data = jsonable_encoder(data)
    if(json_data !=[]):
        return JSONResponse(content=json_data)
    else:
        return HTMLResponse("<div align='center'> NO DATA FOR THE GIVEN LAT AND LONG FOUND PLEASE TRY AGAIN")


@app.post("/post_location" , response_model = schemas.PinRow)
async def post_location(info: schemas.PinRow,sess: Session = Depends(get_sess)):
    # pin_data = crud
    return crud.create_info(sess, info)
