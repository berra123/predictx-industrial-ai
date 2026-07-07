from connection import get_connection

try:
    conn = get_connection()
    print("✅ MySQL bağlantısı başarılı!")
    conn.close()

except Exception as e:
    print(e)