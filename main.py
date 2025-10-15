from ops_instrumentation import attach_ops
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
attach_ops(app)

@app.get("/price-engine")
async def price_engine():
    return {
        "model": "price-engine-v1.0.0",
        "status": "online",
        "lastUpdated": str(datetime.utcnow().date()),
        "data": {
            "tier1_price": 9.99,
            "tier2_price": 19.99,
            "tier3_price": 29.99,
            "recommended_tier": "tier2"
        }
    }
