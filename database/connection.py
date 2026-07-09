import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="db.fqrwsgyxxedgnyqropif.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="Berraculha2004"
    )

    return connection