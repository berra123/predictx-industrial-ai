import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="aws-1-ap-northeast-2.pooler.supabase.com",
        port=6543,
        database="postgres",
        user="postgres.fqrwsgyxxedgnyqropif",
        password="Berraculha2004",
        sslmode="require"
    )

    return connection