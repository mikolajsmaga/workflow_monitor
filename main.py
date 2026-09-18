from workflow_monitor.api.models.status_history import StatusHistoryResponse
from workflow_monitor.engine.flow_builder import build_executed_flow
from workflow_monitor.mappers.status_history_mapper import map_status_history_entry
from workflow_monitor.utils.flow_formatter import format_executed_flow


def main() -> None:
    """
    Run a local executed-flow example using a sample status history payload.
    """
    payload = {
        "list": [
            {
                "id": 22935,
                "statusId": 30026,
                "statusName": "[INV] PDF do SR",
                "statusShortName": "[INV] PDF do SR",
                "statusDescription": "[INV] PDF do SR",
                "changedAtUtc": "2026-09-18T14:28:57.084961Z",
                "previousStatusName": "[GDC] PA / FV",
                "previousStatusId": 30024,
                "changedBy": "Mikołaj Smaga Support SR",
            },
            {
                "id": 22934,
                "statusId": 30024,
                "statusName": "[GDC] PA / FV",
                "statusShortName": "[GDC] PA / FV",
                "statusDescription": "[GDC] PA / FV",
                "changedAtUtc": "2026-09-18T14:28:06.841781Z",
                "previousStatusName": "Nowe zamówienia",
                "previousStatusId": 30017,
                "changedBy": "Mikołaj Smaga Support SR",
            },
            {
                "id": 22771,
                "statusId": 30017,
                "statusName": "Nowe zamówienia",
                "statusShortName": "Nowe zamówienia",
                "statusDescription": "Nowe zamówienia",
                "changedAtUtc": "2026-09-17T07:45:06.843728Z",
                "previousStatusName": None,
                "previousStatusId": None,
                "changedBy": "mediator",
            },
        ],
        "pageNumber": 0,
        "total": 3,
    }

    response = StatusHistoryResponse.model_validate(payload)

    events = [
        map_status_history_entry("4391", entry)
        for entry in response.items
    ]

    flow = build_executed_flow(events)

    print(format_executed_flow("4391", flow))


if __name__ == "__main__":
    main()