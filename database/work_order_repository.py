from database.connection import get_connection


def insert_work_order(
    order_no,
    machine,
    priority,
    assigned_team,
    status,
    description
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO work_orders
        (
            order_no,
            machine,
            priority,
            assigned_team,
            status,
            description
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            order_no,
            machine,
            priority,
            assigned_team,
            status,
            description
        )
    )

    conn.commit()
    cursor.close()
    conn.close()