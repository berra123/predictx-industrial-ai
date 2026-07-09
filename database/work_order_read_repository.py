from database.connection import get_connection


def get_all_work_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            created_at,
            order_no,
            machine,
            priority,
            assigned_team,
            status,
            description
        FROM work_orders
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    work_orders = []

    for row in rows:
        work_orders.append({
            "id": row[0],
            "created_at": row[1],
            "order_no": row[2],
            "machine": row[3],
            "priority": row[4],
            "assigned_team": row[5],
            "status": row[6],
            "description": row[7]
        })

    return work_orders