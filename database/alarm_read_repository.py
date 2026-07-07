from database.connection import get_connection


def get_last_100_alarms():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM alarms
        ORDER BY id DESC
        LIMIT 100
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows