# Path parameter
from fastapi import FastAPI
app = FastAPI()


# 01
@app.get("/courses/{course}")
def actice_courses(course):
    return {"Active course is ": course}

#Run this url : http://127.0.0.1:8000/courses/typescript
#output:  {"Active course is ":"typescript"}


# 02 nested

@app.get("/courses/{course}/{course_id}")
def  get_courses(course, course_id):
    return {"current course is: ": course, "Course id is ": course_id}
#Run this url : http://127.0.0.1:8000/courses/typescript/12
#output:  {"current course is: ":"typescript","Course id is ":"12"}


