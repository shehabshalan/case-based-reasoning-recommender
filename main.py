from fastapi import FastAPI, File, UploadFile, staticfiles
from fastapi.middleware.cors import CORSMiddleware
import similarity
import cases
from fastapi.exceptions import HTTPException

app = FastAPI()
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )


@app.get("/health")
async def health():
    return ({"ok"})

# /Cases is on cases.py
app.include_router(cases.router)

# /recommendation is on similarity.py
app.include_router(similarity.router)

# serve client app from client/dist folder
client_app = staticfiles.StaticFiles(directory="client/dist", html=True)
app.mount("/", client_app, name="client")


# @app.post("/upload")
# def upload_bulk_cases(file: UploadFile = File(...)):
#     if file.content_type != "text/csv":
#         raise HTTPException(400, detail="Invalid document type")
#     file_location = f"data/{file.filename}"
#     try:
#         contents = file.file.read()
#         with open(file_location, 'wb') as f:
#             f.write(contents)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         # add_cases_csv(file_location)
#         file.file.close()

#     return {"message": f"Successfully uploaded {file.filename}"}
