from workflow_monitor.models.flow_event import FlowEvent


def build_executed_flow(events: list[FlowEvent]) -> list[FlowEvent]:
    return sorted(
        events,
        key=lambda event: event.timestamp,
    )