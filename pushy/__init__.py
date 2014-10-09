from models import PushNotification
from tasks import create_push_notification_groups


def send_push_notification(title, body):
    push_notification = PushNotification(title=title,
                                         body=body,
                                         active=PushNotification.PUSH_ACTIVE,
                                         sent=PushNotification.PUSH_NOT_SENT)
    push_notification.save()

    create_push_notification_groups.delay(notification_id=push_notification.id)