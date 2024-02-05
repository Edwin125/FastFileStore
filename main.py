from fastapi import FastAPI, UploadFile, File
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hi There"}

@app.post("/upload")
async def upload(file:UploadFile = File(...)):
    file_ext = file.filename.split(".").pop()
    file_name = datetime.now().strftime("%m-%d-%Y-%H-%M")
    file_path = f"{file_name}.{file_ext}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"success": True, "file_path:": file_path, "message":"File uploaded successfully"}


