from workflow_monitor.models.flow_event import FlowEvent


def format_executed_flow(order_id: str, events: list[FlowEvent]) -> str:
    """
    Format executed flow events into a readable terminal representation.

    The output is intended for quick L2 diagnostics and debugging.
    """
    lines = [f"Order {order_id}", ""]

    for event in events:
        timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        transition = f"{event.status_from_id} -> {event.status_to_id}"

        lines.append(
            f"{timestamp} | {event.actor.type.value:<8} | "
            f"{event.actor.display_name:<30} | {transition}"
        )

    return "\n".join(lines)