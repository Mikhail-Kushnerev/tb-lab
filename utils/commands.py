from asgiref.sync import sync_to_async

from adminpanel.panel.models import Info


@sync_to_async
def add_item(user_id: int, domen: str) -> None:
    Info.objects.create(
        user_id=user_id,
        domen=domen
    )
