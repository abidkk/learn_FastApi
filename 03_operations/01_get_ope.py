# here we use http request method get 

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def getOpe():
    return {"message": "Hello World I am get method"}


# uvicorn 01_get_ope:app --reload  