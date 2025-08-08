from fastapi import FastAPI
app = FastAPI(title="lottery-predict")

@app.get("/health")
def health():
    return {"status": "ok"}
