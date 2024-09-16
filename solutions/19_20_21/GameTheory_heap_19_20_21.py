class Exercise:
    end = 0
    operations = []
    condition = lambda x: x % 2 == 0

    def __init__(self, operations=[], condition=None, end = 0, heaps=1):
        self.operations = operations
        self.condition = condition
        self.end = end
        self.heaps = heaps

    def f(self, heaps, operations, p, end, cond):
        if any(h >= end for h in heaps):
            return p % 2 == 0
        if p == 0:
            return 0
        mas = []
        for op in operations:
            new_heaps = op(heaps)
            mas.append(self.f(new_heaps, operations, p - 1, end, cond))
        return any(mas) if cond(p) else all(mas)

    def sol(self, heaps, p):
        return self.f(heaps, self.operations, p, self.end, self.condition)