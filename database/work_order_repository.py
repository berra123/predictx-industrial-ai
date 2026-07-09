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
        VALUES
        (%s,%s,%s,%s,%s,%s)
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


def get_work_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM work_orders
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    columns = [
        desc[0]
        for desc in cursor.description
    ]

    data = [
        dict(zip(columns, row))
        for row in rows
    ]

    cursor.close()
    conn.close()

    return data