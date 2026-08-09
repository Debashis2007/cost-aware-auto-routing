"""Cost-Aware Auto-Routing — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Cost-Aware Auto-Routing"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


class RouteIn(BaseModel):
    prompt: str
    pin: Optional[str] = None

@app.post("/route")
async def route(body: RouteIn):
    if body.pin:
        model = body.pin
    else:
        model = "mock-small" if len(body.prompt) < 40 else "mock-frontier"
    text = await MockLLM(model=model).complete(body.prompt, max_tokens=12)
    return {"chosen_model": model, "transparent": True, "text": text}
