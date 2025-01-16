from fastapi import APIRouter, HTTPException, Request
from requests import Session
from api.services.chat_service import get_answer
from api.configs.constants import ErrorMessages, OperationNames, StatusCodes
from api.models.schemas.question_request import QuestionRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: QuestionRequest, fastapi_request: Request):
    try:
        question = request.question
        session_id = request.session_id

        result = get_answer(question, session_id)
        return {
            "answer": result["answer"],
            'retrieved_contents': result["retrieved_documents"],
            "session_id": session_id,
            'status_code': StatusCodes.SUCCESS
        }
    except Exception as e:
        raise HTTPException(
            status_code=StatusCodes.INTERNAL_SERVER_ERROR,
            detail={
                'message', ErrorMessages.PROCESSING_ERROR
            }
        )