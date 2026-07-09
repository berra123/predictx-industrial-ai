from datetime import datetime

from database.work_order_repository import (
    insert_work_order
)


def create_work_order(machine, alarm):

    order_no = (
        f"PM-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    if alarm["level"] == "MEDIUM":
        assigned_team = "Predictive Maintenance Team"

    elif alarm["level"] == "HIGH":
        assigned_team = "Mechanical Maintenance Team"

    else:
        assigned_team = "Emergency Response Team"

    insert_work_order(
        order_no,
        machine,
        alarm["level"],
        assigned_team,
        "OPEN",
        alarm["description"]
    )

    return order_no