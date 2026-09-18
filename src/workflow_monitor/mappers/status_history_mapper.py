from workflow_monitor.api.models.status_history import StatusHistoryEntry
from workflow_monitor.models.flow_event import ActorRef, ActorType, FlowEvent


def map_status_history_entry(
    order_id: str,
    entry: StatusHistoryEntry,
) -> FlowEvent:
    actor_type = (
        ActorType.MEDIATOR
        if entry.changed_by.lower() == "mediator"
        else ActorType.UNKNOWN
    )

    actor = ActorRef(
        raw=entry.changed_by,
        type=actor_type,
        display_name=entry.changed_by,
    )

    return FlowEvent(
        order_id=order_id,
        timestamp=entry.changed_at_utc,
        status_from_id=entry.previous_status_id,
        status_to_id=entry.status_id,
        actor=actor,
        source="statusHistory",
    )