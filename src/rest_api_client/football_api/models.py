from typing import Optional, List, Dict, Any

from pydantic import BaseModel


class Area(BaseModel):
    id: int
    name: str
    countryCode: str
    flag: Optional[str] = None
    parentAreaId: Optional[int] = None
    parentArea: Optional[str] = None

class AreasResponse(BaseModel):
    count: int
    filters: Dict[str, Any]
    areas: List[Area]


class CompetitionArea(BaseModel):
    id: int
    name: str
    code: str
    flag: Optional[str] = None

class Competition(BaseModel):
    id: int
    name: str
    code: Optional[str] = None
    type: str
    emblem: Optional[str] = None
    area: CompetitionArea

class CompetitionsResponse(BaseModel):
    count: int
    filters: Dict[str, Any]
    competitions: List[Competition]
