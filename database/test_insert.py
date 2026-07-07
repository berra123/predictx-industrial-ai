from connection import get_connection
from datetime import datetime

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
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
""", (
    datetime.now(),
    "Pulper-03",
    "Running",
    120,
    65,
    3.2,
    410,
    1475
))

conn.commit()

print("Kayıt eklendi.")

cursor.close()
conn.close()