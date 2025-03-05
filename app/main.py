from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from starlette.formparsers import MultiPartParser
import tempfile, shutil, os

from reader.parser import parse

MultiPartParser.max_part_size = 100 * 1024*1024 #10 мб максимум для хранения в памяти

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/upload")
async def endpoint(uploaded_file: UploadFile):
    print("File: ", uploaded_file.file)
    print("In memory? ",uploaded_file._in_memory)

    with tempfile.NamedTemporaryFile(mode='wb', prefix = 'temp_', suffix='.txt', delete = False, dir = './tmp') as temp_file:
        print("Created file is:", temp_file)
        print("Name of the file is:", temp_file.name)

        shutil.copyfileobj(uploaded_file.file, temp_file)
        print("Copied")

    json_path = parse(temp_file.name)
    print("Parsed")
    #os.remove(temp_file.name)

    return FileResponse(path=json_path, filename='json.json', media_type='application/octet-stream')
