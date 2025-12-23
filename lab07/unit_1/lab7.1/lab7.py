import pickle
import shelve
import json
from typing import Dict, List, Tuple


def create_shops_dict() -> Dict:
    """Создание исходного словаря с данными магазинов"""
    shops = {
        "Пятерочка": {
            "Понедельник": 120000, "Вторник": 135000, "Среда": 128000,
            "Четверг": 142000, "Пятница": 185000, "Суббота": 210000,
            "Воскресенье": 195000
        },
        "Магнит": {
            "Понедельник": 98000, "Вторник": 105000, "Среда": 92000,
            "Четверг": 110000, "Пятница": 145000, "Суббота": 168000,
            "Воскресенье": 155000
        },
        "Лента": {
            "Понедельник": 150000, "Вторник": 140000, "Среда": 135000,
            "Четверг": 160000, "Пятница": 220000, "Суббота": 250000,
            "Воскресенье": 230000
        },
        "Перекресток": {
            "Понедельник": 85000, "Вторник": 90000, "Среда": 82000,
            "Четверг": 95000, "Пятница": 130000, "Суббота": 150000,
            "Воскресенье": 140000
        },
        "Ашан": {
            "Понедельник": 200000, "Вторник": 190000, "Среда": 185000,
            "Четверг": 210000, "Пятница": 280000, "Суббота": 310000,
            "Воскресенье": 290000
        },
        "Дикси": {
            "Понедельник": 75000, "Вторник": 80000, "Среда": 72000,
            "Четверг": 85000, "Пятница": 110000, "Суббота": 125000,
            "Воскресенье": 115000
        },
        "ВкусВилл": {
            "Понедельник": 95000, "Вторник": 100000, "Среда": 98000,
            "Четверг": 105000, "Пятница": 140000, "Суббота": 160000,
            "Воскресенье": 155000
        }
    }
    return shops


def calculate_average_revenue(shops: Dict) -> Dict:
    """Вычисление средней выручки для каждого магазина"""
    averages = {}
    for shop_name, days in shops.items():
        total = sum(days.values())
        avg = total / len(days)
        averages[shop_name] = round(avg, 2)
    return averages


def print_shops_with_averages(shops: Dict, averages: Dict):
    """Вывод списка магазинов с их средней выручкой"""
    print("=" * 70)
    print("СПИСОК ВСЕХ МАГАЗИНОВ И ИХ СРЕДНЯЯ ВЫРУЧКА")
    print("=" * 70)
    
    for shop_name, avg in averages.items():
        print(f"• {shop_name:15} | Средняя выручка: {avg:10.2f} руб.")
    
    print()


def find_extreme_shops(averages: Dict) -> Tuple[str, str]:
    """Поиск магазинов с максимальной и минимальной средней выручкой"""
    max_shop = max(averages, key=averages.get)
    min_shop = min(averages, key=averages.get)
    return max_shop, min_shop


def print_extreme_shops(max_shop: str, min_shop: str, averages: Dict):
    """Вывод магазинов с экстремальными значениями"""
    print("=" * 70)
    print("МАГАЗИНЫ С МАКСИМАЛЬНОЙ И МИНИМАЛЬНОЙ СРЕДНЕЙ ВЫРУЧКОЙ")
    print("=" * 70)
    print(f"✓ Максимальная: {max_shop} - {averages[max_shop]:.2f} руб.")
    print(f"✓ Минимальная:  {min_shop} - {averages[min_shop]:.2f} руб.")
    print()


def find_worst_days(shops: Dict):
    """Поиск наиболее неблагоприятных дней для каждого магазина"""
    print("=" * 70)
    print("НАИБОЛЕЕ НЕБЛАГОПРИЯТНЫЙ ДЕНЬ ДЛЯ КАЖДОГО МАГАЗИНА")
    print("=" * 70)
    
    for shop_name, days in shops.items():
        worst_day = min(days, key=days.get)
        worst_revenue = days[worst_day]
        print(f"• {shop_name:15} | {worst_day:12}: {worst_revenue:8} руб.")
    
    print()


def find_shops_with_high_sunday_revenue(shops: Dict, averages: Dict) -> List[str]:
    """Поиск магазинов с выручкой в воскресенье > средней на 20%"""
    print("=" * 70)
    print("МАГАЗИНЫ, ГДЕ ВЫРУЧКА В ВОСКРЕСЕНЬЕ > СРЕДНЕЙ НА 20%")
    print("=" * 70)
    
    selected_shops = []
    
    for shop_name, days in shops.items():
        sunday_revenue = days["Воскресенье"]
        avg_revenue = averages[shop_name]
        percentage = (sunday_revenue / avg_revenue - 1) * 100
        
        if sunday_revenue > avg_revenue * 1.2:
            selected_shops.append(shop_name)
            print(f"✓ {shop_name:15} | Воскресенье: {sunday_revenue:8} руб.")
            print(f"  {' ' * 15} | Средняя:     {avg_revenue:8.2f} руб.")
            print(f"  {' ' * 15} | Превышение:  {percentage:8.1f}%")
            print()
    
    if not selected_shops:
        print("Нет магазинов, удовлетворяющих условию")
        print()
    
    return selected_shops


def save_with_pickle(data: Dict, filename: str = "data.pickle"):
    """Сохранение данных с использованием pickle"""
    print("=" * 70)
    print("СЕРИАЛИЗАЦИЯ С ИСПОЛЬЗОВАНИЕМ PICKLE")
    print("=" * 70)
    
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
        print(f"✓ Данные успешно сохранены в файл: {filename}")
        print(f"  Размер словаря: {len(data)} магазинов")
    except Exception as e:
        print(f"✗ Ошибка при сохранении: {e}")
    
    print()


def load_with_pickle(filename: str = "data.pickle") -> Dict:
    """Загрузка данных с использованием pickle"""
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        print(f"✓ Данные успешно загружены из файла: {filename}")
        return data
    except FileNotFoundError:
        print(f"✗ Файл {filename} не найден")
        return {}
    except Exception as e:
        print(f"✗ Ошибка при загрузке: {e}")
        return {}


def save_with_shelve(data: Dict, dbname: str = "shops_shelf"):
    """Сохранение данных с использованием shelve"""
    print("=" * 70)
    print("СЕРИАЛИЗАЦИЯ С ИСПОЛЬЗОВАНИЕМ SHELVE")
    print("=" * 70)
    
    try:
        with shelve.open(dbname) as db:
            db['shops'] = data
            db['timestamp'] = '2024'
            
        print(f"✓ Данные сохранены в shelve базу: {dbname}")
        print(f"  Созданы файлы: {dbname}.dat, {dbname}.dir, {dbname}.bak")
    except Exception as e:
        print(f"✗ Ошибка при работе с shelve: {e}")
    
    print()


def load_with_shelve(dbname: str = "shops_shelf") -> Dict:
    """Загрузка данных с использованием shelve"""
    try:
        with shelve.open(dbname) as db:
            data = db['shops']
        print(f"✓ Данные загружены из shelve базы: {dbname}")
        return data
    except Exception as e:
        print(f"✗ Ошибка при загрузке из shelve: {e}")
        return {}


def save_to_json(data: Dict, filename: str = "shops_backup.json"):
    """Создание JSON резервной копии (дополнительно)"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ Создана JSON резервная копия: {filename}")
    except Exception as e:
        print(f"✗ Ошибка при создании JSON: {e}")


def main():
    """Основная функция программы"""
    print("\n" + "=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА: РАБОТА СО СЛОВАРЯМИ И СЕРИАЛИЗАЦИЯ")
    print("=" * 70 + "\n")
    
    shops = create_shops_dict()
    print("1. Создан словарь с данными 7 магазинов")
    
    averages = calculate_average_revenue(shops)
    
    print_shops_with_averages(shops, averages)
    
    max_shop, min_shop = find_extreme_shops(averages)
    print_extreme_shops(max_shop, min_shop, averages)
    
    find_worst_days(shops)
    
    selected_shops = find_shops_with_high_sunday_revenue(shops, averages)
    
    save_with_pickle(shops)
    
    loaded_shops = load_with_pickle()
    if loaded_shops:
        print("  Сравнение с оригиналом: ", 
              "совпадает" if shops == loaded_shops else "различается")
    print()
    
    save_with_shelve(shops)
    
    shelve_shops = load_with_shelve()
    if shelve_shops:
        print("  Загружено магазинов из shelve:", len(shelve_shops))
    print()
    
    save_to_json(shops)
    
    print("\n" + "=" * 70)
    print("ИТОГОВАЯ СТАТИСТИКА")
    print("=" * 70)
    
    total_weekly = sum(sum(days.values()) for days in shops.values())
    print(f"Общая выручка всех магазинов: {total_weekly:,} руб.")
    print(f"Средняя выручка на магазин:   {total_weekly/len(shops):,.2f} руб.")
    print(f"Магазинов отобрано по критерию: {len(selected_shops)}")
    
    print("\n" + "=" * 70)
    print("Созданные файлы:")
    print("=" * 70)
    print("1. data.pickle - основной бинарный файл с данными")
    print("2. shops_shelf.dat/.dir/.bak - база данных shelve")
    print("3. shops_backup.json - резервная копия в JSON формате")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()