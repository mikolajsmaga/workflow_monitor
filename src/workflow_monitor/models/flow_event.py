from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class ActorType(str, Enum):
    USER = "USER"
    AJS = "AJS"
    MEDIATOR = "MEDIATOR"
    CONNECTOR = "CONNECTOR"
    SYSTEM = "SYSTEM"
    UNKNOWN = "UNKNOWN"


class ActorRef(BaseModel):
    raw: str
    type: ActorType
    id: str | None = None
    display_name: str


class FlowEvent(BaseModel):
    order_id: str
    timestamp: datetime
    status_from_id: int | None = None
    status_to_id: int
    actor: ActorRef
    source: str