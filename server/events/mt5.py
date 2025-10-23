import platform
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown of MetaTrader5 connection."""
    mt5 = None

    # Startup logic
    if platform.system() == "Windows":
        try:
            import MetaTrader5
            mt5 = MetaTrader5
            if not mt5.initialize():
                raise RuntimeError(f"MetaTrader5 initialization failed: {mt5.last_error()}")
            app.state.mt5 = mt5
        except Exception as exc:
            raise RuntimeError(f"Failed to import MetaTrader5 on startup: {exc}")

    yield

    # Shutdown logic
    if mt5 is not None:
        try:
            mt5.shutdown()
        except Exception:
            pass