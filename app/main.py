from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"{add(1,5)}"}


def add(a: int, b: int) -> str:
    return f"result: {a + b}"
