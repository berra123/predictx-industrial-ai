from database.connection import get_connection


def get_last_20_events():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM events
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return list(reversed(rows))