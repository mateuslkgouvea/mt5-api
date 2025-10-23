from fastapi import Request, HTTPException

def get_mt5(request: Request):
    mt5 = getattr(request.app.state, "mt5", None)
    if mt5 is None:
        raise HTTPException(
            status_code=500,
            detail="MetaTrader5 is not initialized or not supported on this platform",
        )
    return mt5