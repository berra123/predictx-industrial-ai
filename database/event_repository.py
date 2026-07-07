from database.connection import get_connection


def insert_event(event_type, title, description):

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO events
    (
        timestamp,
        event_type,
        title,
        description
    )
    VALUES
    (
        NOW(),
        %s,
        %s,
        %s
    )
    """

    cursor.execute(
        sql,
        (
            event_type,
            title,
            description
        )
    )

    conn.commit()

    cursor.close()
    conn.close()