from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fetch_from_source_a():
    await asyncio.sleep(1)
    return "Dados da Fonte A"

async def fetch_from_source_b():
    await asyncio.sleep(2)
    return "Dados da Fonte B"

@app.get("/dados-paralelos")
async def get_parallel_data():
    resultado_a, resultado_b = await asyncio.gather(
        fetch_from_source_a(),
        fetch_from_source_b()
    )
    return {
        "fonte_a": resultado_a,
        "fonte_b": resultado_b
    }
