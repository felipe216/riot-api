from pydantic import BaseModel


class RiotId(BaseModel):
    name: str
    tag: str


class Puuid(BaseModel):
    puuid: str