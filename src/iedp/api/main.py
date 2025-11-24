"""FastAPI application for IEDP REST API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.iedp.config import get_settings
from src.iedp.logging_config import setup_logging, get_logger

settings = get_settings()
setup_logging(log_level=settings.log_level)
logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="REST API for Intelligent Enterprise Document Analysis",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "IEDP API is running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    """Detailed health check endpoint."""
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "debug": settings.debug,
    }


@app.post("/analyze")
async def analyze_document(document_id: str, query: str = ""):
    """
    Analyze a document.

    Args:
        document_id: ID of the document to analyze
        query: Optional query for analysis

    Returns:
        Analysis results
    """
    logger.info(f"Analyzing document: {document_id}")
    return {
        "document_id": document_id,
        "query": query,
        "status": "processing",
        "message": "Document analysis feature coming soon",
    }


@app.post("/retrieve")
async def retrieve_documents(query: str, limit: int = 5):
    """
    Retrieve relevant documents.

    Args:
        query: Search query
        limit: Maximum number of results

    Returns:
        List of retrieved documents
    """
    logger.info(f"Retrieving documents for query: {query}")
    return {
        "query": query,
        "limit": limit,
        "results": [],
        "status": "success",
        "message": "Retrieval feature coming soon",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.iedp.api.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
