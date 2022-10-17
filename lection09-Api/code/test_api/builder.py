from dataclasses import dataclass

import faker

faker = faker.Faker()


class Builder:
    @staticmethod
    def topic(text=None, title=None):
        @dataclass
        class Topic:
            title: str
            text: str
            id: None = None

        if title is None:
            title = faker.lexify('?? ??? ???? ???')

        if text is None:
            text = faker.bothify('?? ?#?? ?##????##? ??#?')

        return Topic(title=title, text=text)
