
from dataclasses import dataclass, fields


@dataclass()
class Person:
    fistname: str
    lastname: str


if __name__ == '__main__':
    for f in fields(Person):
        print(f)
