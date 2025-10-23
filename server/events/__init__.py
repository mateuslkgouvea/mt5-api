from contextlib import AsyncExitStack, asynccontextmanager
from fastapi import FastAPI

from server.events.mt5 import lifespan as mt5_lifespan

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        await stack.enter_async_context(mt5_lifespan(app))
        yield