from dataclasses import dataclass, field


@dataclass
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list = field(default_factory=list)


if __name__ == '__main__':
    p = Person('太郎', '山田', 58, ['married', 'AB'])
    p.memos.append('dog')
    print(p)

    # ms = ['married', 'AB']
    # p = Person('太郎', '山田', 58, ms)
    # ms.append('dog')
    # print(p)
