from typing import Union


def get_by_id(id: int) -> Union[User, Page, None]:
    pass


luka: User = get_by_id(1451268501)
pycon_jp: Page = get_by_id(663926337003460)
probably_none = get_by_id(-1)
