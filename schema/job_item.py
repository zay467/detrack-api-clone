from typing import Optional
from pydantic import BaseModel

class JobItem(BaseModel):
    sku : str
    description : str
    quantity : int
    reject : Optional[int]
    reason : Optional[str]