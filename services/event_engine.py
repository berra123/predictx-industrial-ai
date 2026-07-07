from database.event_repository import insert_event


def log_event(event_type, title, description):

    insert_event(
        event_type,
        title,
        description
    )