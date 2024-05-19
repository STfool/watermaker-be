from fastapi import FastAPI

app  = FastAPI(title="Reduce img file")

app.include_router()

@app.get("/")
def read_root():
    return {"message": "ok"}