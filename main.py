from fastapi import FastAPI
from starlette.responses import HTMLResponse



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
        PINCODE here : <input name="pin" type = "number"><br>
        PLACE here : <input name="place" type = "text"><br>
        PHONE here : <input name="phone" type = "number"><br>
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

@app.get("/read")
async def ss(pin: int = 0,place: str = None , phone: int = None):
    print("we are here")
    return {"PINCODE":pin,"place": place,"phone":phone}
