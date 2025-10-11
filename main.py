from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins — feel free to lock this down later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price-engine")
async def generate_price_tiers():
    # Static response for now, can be replaced with ML or rule-based logic
    return {
        "tiers": [
            {"name": "Starter", "price": 29},
            {"name": "Growth", "price": 79},
            {"name": "Scale", "price": 199}
        ],
        "strategy": "anchoring + decoy",
        "model": "price-engine-v1.0.0"
    }
