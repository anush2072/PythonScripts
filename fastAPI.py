from email.policy import default
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def liveness_probe():
    return JSONResponse(status_code=200, content={"message": "serving-service is ALIVE"})

@app.get("/ready")
async def readiness_probe():
    x = True
    if x:
        return JSONResponse(status_code=200, content={"message": "serving-service is READY"})
    else:
        return JSONResponse(status_code=503, content={"message": "serving-service is OUT_OF_SERVICE"})

# Version 2 of returning status code other than default
# @app.get("/health")
# async def liveness_probe(response: Response):
#     x = False
#     here = ""
#     if x:
#         here = "why?"
#         response.status_code = 200
#     else:
#         here = "that's why"
#         response.status_code = 503
#     return {"message": "serving-service is ALIVE"}, here