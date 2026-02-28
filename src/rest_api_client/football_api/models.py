from typing import Any

from pydantic import BaseModel


class Area(BaseModel):
    id: int
    name: str
    countryCode: str
    flag: str | None = None
    parentAreaId: int | None = None
    parentArea: str | None = None


class AreasResponse(BaseModel):
    count: int
    filters: dict[str, Any]
    areas: list[Area]


class CompetitionArea(BaseModel):
    id: int
    name: str
    code: str
    flag: str | None = None


class Competition(BaseModel):
    id: int
    name: str
    code: str | None = None
    type: str
    emblem: str | None = None
    area: CompetitionArea


class CompetitionsResponse(BaseModel):
    count: int
    filters: dict[str, Any]
    competitions: list[Competition]
