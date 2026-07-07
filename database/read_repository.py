from database.connection import get_connection


def get_last_100_telemetry():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT *
    FROM telemetry
    ORDER BY id DESC
    LIMIT 100
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return list(reversed(rows))