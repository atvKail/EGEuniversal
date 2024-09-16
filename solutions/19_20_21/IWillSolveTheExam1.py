from GameTheory_heap_19_20_21 import Exercise


operations = [
    lambda heaps: [heaps[0] + 1],
    lambda heaps: [heaps[0] + 2],
    lambda heaps: [heaps[0] * 2]
]
condition  = lambda x: x % 2 != 0
end = 44
ex = Exercise(operations=operations, condition=condition, end=end)

#19, 28074
print("19: 11")
# Не нужен код ответ 11
#20, 28075
c = 0
print("20:")
for x in range(44):
    if ex.sol([x], 1) == 0 and ex.sol([x], 3) == 1 and c < 2:
        print(x)
        c += 1
#21, 28076
print("21:")
for x in range(44):
    if ex.sol([x], 2) == 0 and ex.sol([x], 4) == 1:
        print(x)
        break


# Для двух кучек, пример:

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