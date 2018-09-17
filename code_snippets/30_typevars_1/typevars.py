from typing import Type


class BaseClass:
    pass


class DerivedClass(BaseClass):
    pass


def factory(clazz: Type[BaseClass]) -> BaseClass:
    return clazz()


base = factory(BaseClass)  # BaseClass
derived = factory(DerivedClass)  # BaseClass
