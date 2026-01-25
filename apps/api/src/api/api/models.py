from pydantic import BaseModel, Field
from typing import Optional


class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to be used in the RAG pipeline")

class RAGUsedContext(BaseModel):
    description: str = Field(..., description="Short description of the item used to answer the question")
    image_url: str = Field(None, description="URL of the image of the item used to answer the question")
    price: Optional[float] = Field(..., description="Price of the item used to answer the question")

class RAGResponse(BaseModel):
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")
    used_context: list[RAGUsedContext] = Field(..., description="Information about the context items used to generate the answer")