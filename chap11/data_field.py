
from dataclasses import dataclass, field


@dataclass
class Person:
    firstname: str
    lastname: str
    age: int = field(default=0, compare=False)


if __name__ == '__main__':
    p1 = Person('太郎', '山田', 58)
    p2 = Person('太郎', '山田', 11)
    print(p1 == p2)
