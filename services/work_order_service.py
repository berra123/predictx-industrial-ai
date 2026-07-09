from datetime import datetime

from database.work_order_repository import (
    insert_work_order
)


def create_work_order(
    machine,
    alarm
):

    order_no = (
        f"PM-"
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    insert_work_order(
        order_no,
        machine,
        alarm["level"],
        "Mechanical Maintenance Team",
        "OPEN",
        alarm["description"]
    )

    return order_no