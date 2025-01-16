class SplitParameters:
    CHUNK_SIZE = 2000
    CHUNK_OVERLAP = 100

class Models:
    LLM_MODEL = 'gpt-4o'
    EMBEDDING_MODEL = 'text-embedding-3-large'

class ErrorMessages:
    PROCESSING_ERROR = "An error occurred while processing your question. Please try again."
    GENERIC_ERROR = "An unexpected error occurred. Please try again later."
    DOCUMENT_UPLOAD_ERROR = "The document could not be uploaded. Please try again."