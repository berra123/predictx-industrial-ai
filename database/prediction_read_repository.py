from database.connection import get_connection
from psycopg2.extras import RealDictCursor


def get_last_100_predictions():

    conn = get_connection()

    cursor = conn.cursor(
        cursor_factory=RealDictCursor
    )

    sql = """
    SELECT *
    FROM predictions
    ORDER BY id DESC
    LIMIT 100
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return list(reversed(rows))