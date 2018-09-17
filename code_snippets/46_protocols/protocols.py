from typing_extensions import Protocol


class Duck(Protocol):
    def quack(self) -> str: ...
    def fly(self) -> str: ...


def duck_things(duck: Duck) -> None:
    duck.quack()
    duck.swim()


class PharaohDuck:
    def quack(self) -> str:
        return "quaaack"
    def swim(self) -> str:
        return "🦆"


class GeckoDuck:
    def quack(self) -> str:
        return "quack??"
    def swim(self) -> str:
        return "Gecko doesn't swim"


duck_things(PharaohDuck())
