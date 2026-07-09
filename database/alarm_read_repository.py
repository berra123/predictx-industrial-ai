from database.connection import get_connection
from psycopg2.extras import RealDictCursor


def get_last_100_alarms():

    conn = get_connection()

    cursor = conn.cursor(
        cursor_factory=RealDictCursor
    )

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