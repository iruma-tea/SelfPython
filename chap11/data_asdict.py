from dataclasses import asdict, astuple, dataclass


@dataclass()
class Person:
    firstname: str
    lastname: str


if __name__ == '__main__':
    p = Person('次郎', '山田')
    print(asdict(p))
    print(astuple(p))
