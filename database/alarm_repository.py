from database.connection import get_connection


def insert_alarm(machine, alarm):

    if alarm["level"] == "NORMAL":
        return

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO alarms
    (
        timestamp,
        machine,
        alarm_level,
        alarm_type,
        description
    )
    VALUES
    (NOW(), %s, %s, %s, %s)
    """

    values = (

        machine,
        alarm["level"],
        alarm["type"],
        alarm["description"]

    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()
