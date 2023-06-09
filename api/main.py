from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from database.query import query_get, query_put, query_update
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from hero import HeroModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
    "http://localhost:19006"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/heroes/", response_model=list[HeroModel])
def read_heroes():
    heros = query_get("""
        SELECT  
            *
        FROM Hero
        """, ())
    return JSONResponse(status_code=200, content=jsonable_encoder(heros))


@app.get("/heroes/{name}/{secret_name}")
def read_hero_age(name: str, secret_name: str):
    hero = query_get("""
        SELECT age 
        FROM Hero 
        WHERE name = %s AND secret_name = %s
        """, (name, secret_name))

    if hero:
        return JSONResponse(status_code=200, content=jsonable_encoder(hero))
    else:
        return JSONResponse(status_code=404, content="Hero not found")
