from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime



# shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# this will be used to validate data while creating a Job
class JobCreate(JobBase):
    title: str
    description: str


# this will be used to format the response to not to have id,owner_id etc
class ShowJob(JobBase):
    title: str
    description: Optional[str]
    username: str
    owner_id: str
    date_posted: date

    class Config():  # to convert non dict obj to json
        orm_mode = True