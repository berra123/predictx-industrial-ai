from collections import deque

# Son 100 telemetri kaydını hafızada tutar
history = deque(maxlen=100)


def add_record(record):
    """
    Yeni telemetri kaydını hafızaya ekler.
    """
    history.append(record)


def get_history():
    """
    Son telemetri kayıtlarını döndürür.
    """
    return list(history)


def clear_history():
    """
    Hafızadaki tüm kayıtları temizler.
    """
    history.clear()