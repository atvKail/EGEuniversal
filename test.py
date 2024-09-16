class Exercise:
    def __init__(self, operations, condition, end, heaps=1):
        self.operations = operations  # Операции над кучками
        self.condition = condition  # Условие для победы
        self.end = end  # Конечное значение для игры
        self.heaps = heaps  # Количество кучек

    def f(self, heaps, operations, p, end, cond):
        if any(h >= end for h in heaps):  # Если хотя бы одна кучка достигла конечного состояния
            return p % 2 == 0
        if p == 0:
            return 0
        mas = []
        for op in operations:  # Применение операций ко всем кучкам
            new_heaps = op(heaps)  # Применение операции
            mas.append(self.f(new_heaps, operations, p - 1, end, cond))  # Рекурсивный вызов
        return any(mas) if cond(p) else all(mas)

    def sol(self, heaps, p):
        return self.f(heaps, self.operations, p, self.end, self.condition)


# Пример для одной кучки:
operations = [
    lambda heaps: [heaps[0] + 1],  # Увеличение первой кучки
    lambda heaps: [heaps[0] + 2],
    lambda heaps: [heaps[0] * 2]
]
condition = lambda x: x % 2 != 0
end = 44
ex = Exercise(operations=operations, condition=condition, end=end, heaps=1)

print("19: 11")
print("20:")
for x in range(44):
    if ex.sol([x], 1) == 0 and ex.sol([x], 3) == 1:
        print(x)

# Пример для двух кучек:
operations = [
    lambda heaps: [heaps[0] + 1, heaps[1]],  # Увеличение первой кучки
    lambda heaps: [heaps[0], heaps[1] + 1],  # Увеличение второй кучки
    lambda heaps: [heaps[0] * 2, heaps[1]],
    lambda heaps: [heaps[0], heaps[1] * 2]
]
condition = lambda x: x % 2 != 0
end = 44
ex2 = Exercise(operations=operations, condition=condition, end=end, heaps=2)

print("21:")
for x in range(44):
    if ex2.sol([x, x], 2) == 0 and ex2.sol([x, x], 4) == 1:
        print(x)
        break