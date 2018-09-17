from typing import Type, TypeVar


class BaseClass:
    pass


class DerivedClass(BaseClass):
    pass


T = TypeVar("T", bound=BaseClass)


def factory(clazz: Type[T]) -> T:
    return clazz()


base = factory(BaseClass)  # BaseClass
derived = factory(DerivedClass)  # DerivedClass
