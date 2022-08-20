from asgiref.sync import sync_to_async

from adminpanel.panel.models import Info


@sync_to_async
def add_item(user_id, domen):
    a = Info.objects.create(
        user_id=user_id,
        domen=domen
    )
    return a
