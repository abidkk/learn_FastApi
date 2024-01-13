# Paths are also known as "routes " or "endpoints"

from fastapi import FastAPI
app = FastAPI()

# 01
@app.get("/courses")
def root():
    return {"active course": "Python and FastAPI"}

# url : http://127.0.0.1:8000/courses
# ouutput : {"active course":"Python and FastAPI"}



# 02
@app.get("/courses/upcoming")
def upcomming_course():
    return {"Upcoming course": "Javacript crash course"}

# url : http://127.0.0.1:8000/courses/upcoming
# ouutput : {"Upcoming course":"Javacript crash course"}











#  uvicorn 01_static_path:app --reload