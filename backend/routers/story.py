import uuid
from typing import Optional
from datetime import DateTime
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Cookie, StoryJobResponse
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story, StoryNode
from backend.models.job import StoryJob
from backend.schemas.story import (
    CompleteStoryResponse,
    CompleteStoryNodeResponse,
    CreateStoryRequest
)
from backend.schemas.job import (
    StoryJobResponse
)

router = APIRouter()
