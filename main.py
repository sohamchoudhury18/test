from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
from sql_app import database as db
from sql_app import models as models
from sql_app import crud
from fastapi.encoders import jsonable_encoder


app = FastAPI()
# templates = Jinja2Templates(directory="templates")

html = '''
<!doctype html>
<head>
    <title> STAGE 1 </title>
</head>
<body>

    <h1> you made it here </h1>
    <form action="/read"  method="get" target="_self">
        longitude here : <input name="longitude" type = "decimal"><br>
        latitude here : <input name="latitude" type = "decimal"><br>
        <input type="submit" value="submit info">
    </form>
</body>
'''

@app.get("/")
async def root():
    return {"root":"page"}


@app.get("/index")
async def root():
    return HTMLResponse(html)

@app.get("/get_location")
async def get_location(latitude: float = 0.0,longitude: float = 0.0):
    print("you are here!")
    data = crud.get_info(latitude=latitude ,longitude= longitude)
    print(data)
    json_data = jsonable_encoder(data)
    print(json_data)
    return JSONResponse(content=json_data)


# get_location(latitude=77.1667,longitude=28.7556)
