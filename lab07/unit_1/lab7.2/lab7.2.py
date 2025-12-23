import pickle
import shelve

# Читаем и сортируем
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]
lines.sort(key=lambda x: len(x.split()))

# Записываем результат
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

# Сериализуем результат
data = {'sorted_lines': lines}
with open('sorted.pickle', 'wb') as f:
    pickle.dump(data, f)

with shelve.open('sorted_db') as db:
    db['data'] = data

print("Задание 2 готово!")