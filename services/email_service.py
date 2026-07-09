def send_email_notification(machine, alarm):

    print(
        f"""
========================================
EMAIL NOTIFICATION SENT
========================================
To: maintenance@predictx.ai
Subject: {alarm['level']} Alarm - {machine}

Machine: {machine}
Alarm Type: {alarm['type']}
Description: {alarm['description']}
========================================
"""
    )

    return True