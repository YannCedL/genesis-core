# contradiction preserved, never deleted
"""
Contradiction and Preserved Claim models.
Ensures conflicting claims from multiple sources are preserved, never silently deleted.
"""

from typing import Any, List, Optional
from pydantic import BaseModel, Field
from .epistemology import EpistemicStatus

class Claim(BaseModel):
    claim_id: str = Field(..., description="Unique claim identifier")
    subject: str = Field(..., description="Subject of the claim")
    predicate: str = Field(..., description="Attribute being claimed")
    value: Any = Field(..., description="Value claimed")
    source: str = Field(..., description="Source of the claim")
    timestamp: str = Field(..., description="Observation timestamp")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    status: EpistemicStatus = Field(default=EpistemicStatus.OBSERVATION)

class PreservedContradiction(BaseModel):
    contradiction_id: str = Field(..., description="Unique contradiction identifier")
    subject: str = Field(..., description="Subject with conflicting data")
    predicate: str = Field(..., description="Attribute in dispute")
    claims: List[Claim] = Field(..., min_length=2, description="List of conflicting claims")
    resolved: bool = Field(default=False, description="Whether contradiction has been resolved")
    resolution_notes: Optional[str] = Field(None, description="Explanation if resolved")


