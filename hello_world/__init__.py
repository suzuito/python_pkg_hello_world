from .person import Person


def hello(p: Person):
    print('{}: {}'.format(p.name, p.say()))
