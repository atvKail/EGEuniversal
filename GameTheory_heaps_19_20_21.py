class Exercise:
    operations = []
    condition = lambda x: x % 2 == 0

    def __init__(self, operations, condition=None):
        if condition:
            self.condition = condition
        operations = operations

    def f(self, x, operations, p, end, cond=(lambda x: x % 2 == 0)):
        if x >= end:
            return p % 2 == 0
        if p == 0:
            return 0
        mas = []
        for op in operations:
            mas.append(self.f(op(x), operations, p - 1, end, cond))
        # print(x, p, mas, cond(p))
        return any(mas) if cond(p) else all(mas)


operations = [lambda x: x + 2, lambda x: x * 2]
condition  = lambda x: x % 2 != 0