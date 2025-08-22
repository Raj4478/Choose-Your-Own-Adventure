from typing import Optional
from DateTime import datetime
from pydantic import BaseModel


class StoryJobBase(BaseModel):
    theme: str


class StoryJobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    story_id: int
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryJobCreate(StoryJobBase):
    pass