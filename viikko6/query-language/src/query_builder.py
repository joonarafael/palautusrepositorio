from matchers import PlaysIn, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = []

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *matchers):
        return oneOfOperator(*matchers)

    def build(self):
        return And(*self._matchers)

class oneOfOperator:
    def __init__(self, *matchers):
        self._matchers = matchers

    def build(self):
        return Or(*self._matchers)