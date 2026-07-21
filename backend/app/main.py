from fastapi import FastAPI

app = FastAPI(
    title="Migration Policy Radar",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "name": "Migration Policy Radar",
        "version": "0.1.0",
        "status": "running"
    }