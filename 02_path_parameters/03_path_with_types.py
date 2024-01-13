from fastapi import FastAPI

app = FastAPI()


# 01: with string type 
@app.get("/students/{country}")
def get_student(country:str): # type str declared
    return{"These are the  students from":country}

# url : http://127.0.0.1:8000/students/Pakistan
# output: {"These are th  students from":"Pakistan"}


# Data conversion  
# url : http://127.0.0.1:8000/students/123
# output: {"These are th  students from":"123"} : note you will see 123 in string format





# 02: with int type as well 

@app.get("/students/{country}/id/{id}")
def get_student_id(country:str, id:int):
    return{"These are the students from":country, "Id no ":id}

# url : http://127.0.0.1:8000/students/Pakistan/id/2233
# output: {"These are th  students from":"Pakistan","Id no ":2233} : note you will see 2233 in int format

# Data validation
# note : what happen if we pass id as string or other type than int ??? ERROR

# url :http://127.0.0.1:8000/students/Pakistan/id/pak
# output error: {"detail":[{"type":"int_parsing","loc":["path","id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"pak","url":"https://errors.pydantic.dev/2.5/v/int_parsing"}]}





# run file:   uvicorn 03_path_with_types:app --reload

