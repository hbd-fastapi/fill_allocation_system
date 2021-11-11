"""
    Position server

    - receive report from controller at 10 second intervals
    - prints out new positions/values

"""

import uvicorn

from fastapi import FastAPI



app = FastAPI()



@app.post("/fill/")
async def positions():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8002)
