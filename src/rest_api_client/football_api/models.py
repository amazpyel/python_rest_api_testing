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
