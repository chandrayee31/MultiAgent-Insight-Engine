from pydantic import BaseModel
from typing import Dict, Any


class MultiAgentResponse(BaseModel):
    plan: Dict[str, Any]
    analysis: Dict[str, Any]
    answer: str