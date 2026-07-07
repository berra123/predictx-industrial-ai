from database.alarm_repository import insert_alarm


def create_alarm(machine, alarm):
    """
    Alarmı işler ve veritabanına kaydeder.
    """

    if alarm["level"] == "NORMAL":
        return

    insert_alarm(machine, alarm)