from typing import Annotated, Any
from fastapi import FastAPI, Depends
from server.dependencies import get_mt5
from server.events import lifespan


app = FastAPI(lifespan = lifespan)

@app.get("/")
def root():
    return {"message": "Metatrader 5 API running"}

@app.get("/status")
def check_mt5_status(mt5: Annotated[Any, Depends(get_mt5)]):
    """Check if MT5 connection is working"""
    return {
        "connected": True,
        "terminal_info": mt5.terminal_info()._asdict(),
        "version": mt5.__version__,
    }