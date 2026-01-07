from fastapi import FastAPI

app = FastAPI(title="python-fastapi-test-api")


@app.get("/health")
def health():
    return {"status": "ok", "service": "python-fastapi-test-api running"}
