from database.connection import get_connection
from psycopg2.extras import RealDictCursor


def get_last_20_events():

    conn = get_connection()

    cursor = conn.cursor(
        cursor_factory=RealDictCursor
    )

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