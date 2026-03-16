from fastapi import FastAPI

from app.models.request_models import QuestionRequest
from app.models.response_models import MultiAgentResponse
from app.workflows.agent_graph import run_multiagent_workflow
from app.utils.logger import logger


app = FastAPI(title="MultiAgent Insight Engine")


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}


@app.post("/analyze", response_model=MultiAgentResponse)
def analyze_question(request: QuestionRequest):
    logger.info(f"Received analyze request: {request.question}")

    result = run_multiagent_workflow(request.question)

    logger.info("Returning multi-agent response")

    return MultiAgentResponse(
        plan=result["plan"],
        analysis=result["analysis"],
        answer=result["answer"]
    )