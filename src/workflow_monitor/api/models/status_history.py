from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class StatusHistoryEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        frozen=True,
    )

    id: int
    status_id: int = Field(alias="statusId")
    status_name: str = Field(alias="statusName")
    status_short_name: str = Field(alias="statusShortName")
    status_description: str = Field(alias="statusDescription")
    changed_at_utc: datetime = Field(alias="changedAtUtc")
    previous_status_name: str | None = Field(
        default=None,
        alias="previousStatusName",
    )
    previous_status_id: int | None = Field(
        default=None,
        alias="previousStatusId",
    )
    changed_by: str = Field(alias="changedBy")


class StatusHistoryResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        frozen=True,
    )

    items: list[StatusHistoryEntry] = Field(alias="list")
    page_number: int = Field(alias="pageNumber")
    total: int