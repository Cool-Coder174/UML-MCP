"""Pydantic models for the domain JSON."""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class Attribute(BaseModel):
    vis: str
    name: str
    type: str

class Method(BaseModel):
    sig: str

class Class(BaseModel):
    name: str
    abstract: Optional[bool] = False
    extends: Optional[str] = None
    attributes: List[Attribute]
    methods: List[Method]

class Relationship(BaseModel):
    from_: str = Field(..., alias='from')
    to: str
    type: str
    multFrom: str
    multTo: str
    label: Optional[str] = None

class Message(BaseModel):
    from_: str = Field(..., alias='from')
    to: str
    label: str
    dashed: Optional[bool] = False

class AltBlock(BaseModel):
    alt: str
    else_: List[str] = Field(..., alias='else')

class Sequence(BaseModel):
    scenario: str
    actors: List[str]
    participants: List[str]
    messages: List[Dict[str, Any]]

class DomainModel(BaseModel):
    classes: List[Class]
    relationships: List[Relationship]
    sequence: Sequence
