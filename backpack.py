

items = {'зажигалка': 1, 'топор': 4, 'веревка': 2, 'спальник': 3, 'дрова': 7, 'котелок': 5, 'еда': 4}
max_weight = 12

backpack = {}
total_weight = 0

for item in sorted(items.items(), key=lambda x: x[1]):
    if total_weight + item[1] <= max_weight:
        backpack[item[0]] = item[1]
        total_weight += item[1]

print(backpack)