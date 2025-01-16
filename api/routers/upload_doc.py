from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from api.services.upload_service import upload_docs_to_vectordb, load_documents
from api.configs.constants import ErrorMessages
from fastapi import FastAPI, Depends

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "API is running"}

@router.post("/upload")
async def upload_docs(file: UploadFile = File(...), request: Request = None):
    try:
        doc = load_documents(file.file)
        counts = upload_docs_to_vectordb(doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail={'message': ErrorMessages.DOCUMENT_UPLOAD_ERROR})