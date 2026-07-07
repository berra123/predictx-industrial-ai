from database.connection import get_connection


def insert_telemetry(data):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO telemetry
    (
        timestamp,
        machine,
        status,
        current,
        temperature,
        vibration,
        torque,
        speed
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (

        data["timestamp"],
        data["machine"],
        data["status"],
        data["current"],
        data["temperature"],
        data["vibration"],
        data["torque"],
        data["speed"]

    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()