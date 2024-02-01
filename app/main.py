import uvicorn
from fastapi import FastAPI, File, UploadFile
from typing import Union
import shutil
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello! TAPE!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    a = os.getcwd()
    a2 = len(q)
    return {"item_id": item_id, "q": q, "current_path":a, "length":a2}



#@app.post("/files/")
#async def file(file: bytes = File(...)):
#    content = file.decode('utf-8')
#    formatfile = content.split('\n')
#    return {'filedetail': formatfile}

#@app.post("/files/")
#def create_file(file: Annotated[bytes | None, File()] = None):
#    if not file:
#        return {"message": "No file sent"}
#    else:
#        return {"file_size": len(file)}
    

#@app.post("/files/")
#async def create_file(file: bytes = File(...)):
#    return {"file_size": len(file)}


#@app.post("/uploadfile/")
#async def create_upload_file(file: UploadFile = File(...)):
#    return {"filename": file.filename}