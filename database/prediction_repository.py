from database.connection import get_connection


def insert_prediction(machine, prediction):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO predictions
    (
        timestamp,
        machine,
        ai_risk,
        predicted_failure,
        remaining_life,
        confidence,
        recommendation
    )
    VALUES
    (NOW(), %s, %s, %s, %s, %s, %s)
    """

    values = (

        machine,
        prediction["risk"],
        prediction["failure"],
        prediction["remaining_life"],
        prediction["confidence"],
        prediction["recommendation"]

    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()