class Exercise:
    end = 0
    operations = []
    condition = lambda x: x % 2 == 0

    def __init__(self, operations=[], condition=None, end=0):
        if condition:
            self.condition = condition
        self.operations = operations
        self.end = end

    def f(self, x, operations, p, end, cond=(lambda x: x % 2 == 0)):
        if x >= end:
            return p % 2 == 0
        if p == 0:
            return 0
        mas = []
        for op in operations:
            mas.append(self.f(op(x), operations, p - 1, end, cond))
        return any(mas) if cond(p) else all(mas)

    def sol(self, x, p):
        return self.f(x, self.operations, p, self.end, self.condition)

