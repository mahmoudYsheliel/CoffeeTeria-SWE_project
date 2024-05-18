from pydantic import BaseModel
from typing import Optional

class Info(BaseModel):
    id:Optional[str]=''
    title:str
    type:str
    description:str