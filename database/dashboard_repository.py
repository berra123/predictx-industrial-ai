from database.connection import get_connection


def get_dashboard_statistics():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Toplam telemetri
    cursor.execute("SELECT COUNT(*) AS total FROM telemetry")
    telemetry_count = cursor.fetchone()["total"]

    # Farklı makine sayısı
    cursor.execute("""
        SELECT COUNT(DISTINCT machine) AS machines
        FROM telemetry
    """)
    machine_count = cursor.fetchone()["machines"]

    # Toplam alarm
    cursor.execute("""
        SELECT COUNT(*) AS alarms
        FROM alarms
    """)
    alarm_count = cursor.fetchone()["alarms"]

    # Ortalama AI Risk
    cursor.execute("""
        SELECT AVG(ai_risk) AS avg_risk
        FROM predictions
    """)

    result = cursor.fetchone()

    avg_risk = result["avg_risk"] or 0

    cursor.close()
    conn.close()

    return {
        "telemetry": telemetry_count,
        "machines": machine_count,
        "alarms": alarm_count,
        "avg_risk": round(avg_risk, 1)
    }