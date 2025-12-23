import csv
import json
from typing import Dict, List, Any


def analyze_csv_file():
    """Анализ CSV файла 7.csv"""
    print("=" * 70)
    print("1. АНАЛИЗ CSV ФАЙЛА (7.csv)")
    print("=" * 70)
    
    try:
        with open('7.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)
        
        print(f" Файл прочитан. Записей: {len(data)}")
        
        print("\nПервые 3 записи в формате 'Ключ → Значение':")
        print("-" * 40)
        for i, row in enumerate(data[:3], 1):
            print(f"\nЗапись #{i}:")
            for key, value in row.items():
                print(f"  {key} → {value}")
        
        temperatures = [int(row['Temperature']) for row in data]
        min_temp = min(temperatures)
        max_temp = max(temperatures)
        
        print(f"\nСамая низкая температура: {min_temp}°C")
        print(f"Самая высокая температура: {max_temp}°C")
        
        high_humidity_count = sum(1 for row in data if int(row['Humidity']) > 80)
        print(f"\nДней с влажностью выше 80%: {high_humidity_count}")
        
        avg_pressure = sum(int(row['Pressure']) for row in data) / len(data)
        print(f"Среднее атмосферное давление: {avg_pressure:.2f} hPa")
        
        print("\nСредние показатели по городам:")
        print("-" * 40)
        
        city_data = {}
        for row in data:
            city = row['City']
            if city not in city_data:
                city_data[city] = {
                    'temperatures': [],
                    'humidities': [],
                    'pressures': [],
                    'wind_speeds': []
                }
            
            city_data[city]['temperatures'].append(int(row['Temperature']))
            city_data[city]['humidities'].append(int(row['Humidity']))
            city_data[city]['pressures'].append(int(row['Pressure']))
            city_data[city]['wind_speeds'].append(int(row['Wind_Speed']))
        
        for city, values in city_data.items():
            avg_temp = sum(values['temperatures']) / len(values['temperatures'])
            avg_hum = sum(values['humidities']) / len(values['humidities'])
            avg_press = sum(values['pressures']) / len(values['pressures'])
            avg_wind = sum(values['wind_speeds']) / len(values['wind_speeds'])
            
            print(f"\n{city}:")
            print(f"  • Средняя температура: {avg_temp:.1f}°C")
            print(f"  • Средняя влажность: {avg_hum:.1f}%")
            print(f"  • Среднее давление: {avg_press:.1f} hPa")
            print(f"  • Средняя скорость ветра: {avg_wind:.1f} м/с")
        
        return data
        
    except FileNotFoundError:
        print(" Ошибка: Файл 7.csv не найден!")
        print("  Убедитесь, что файл находится в той же папке")
        return None
    except Exception as e:
        print(f" Ошибка при работе с CSV: {e}")
        return None


def analyze_json_file():
    """Анализ JSON файла 7.json"""
    print("\n" + "=" * 70)
    print("2. АНАЛИЗ JSON ФАЙЛА (7.json)")
    print("=" * 70)
    
    try:
        with open('7.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        accounts = data.get('accounts', [])
        print(f" Файл прочитан. Аккаунтов: {len(accounts)}")
        
        print("\nПоиск аккаунтов по шаблону ID:")
        print("-" * 40)
        
        patterns = ['acc', 'acc_xyz', 'acc_abc']
        for pattern in patterns:
            found_accounts = [
                acc for acc in accounts 
                if acc['account_id'].startswith(pattern)
            ]
            print(f"  Шаблон '{pattern}': найдено {len(found_accounts)} аккаунтов")
        
        print("\nКоличество аккаунтов по статусам:")
        print("-" * 40)
        
        status_counts = {}
        for account in accounts:
            status = account['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        for status, count in status_counts.items():
            print(f"  • {status}: {count} аккаунт(ов)")
        
        avg_storage = sum(acc['storage_used'] for acc in accounts) / len(accounts)
        print(f"\nСредний используемый объем хранилища: {avg_storage:.2f} GB")
        
        print("\nСохранение отфильтрованных данных:")
        print("-" * 40)

        filtered_accounts = [
            acc for acc in accounts 
            if acc['status'] == 'active' and acc['storage_used'] > 1.0
        ]
        
        filtered_data = {
            "filtered_accounts": filtered_accounts,
            "filter_criteria": {
                "status": "active",
                "min_storage_used": 1.0
            },
            "total_count": len(filtered_accounts),
            "original_count": len(accounts)
        }
        
        with open('out.json', 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=2)
        
        print(f"✓ Сохранено {len(filtered_accounts)} аккаунтов в out.json")
        
        if filtered_accounts:
            print("\nОтфильтрованные аккаунты:")
            for i, acc in enumerate(filtered_accounts, 1):
                print(f"\n  Аккаунт #{i}:")
                print(f"    • ID: {acc['account_id']}")
                print(f"    • Имя: {acc['username']}")
                print(f"    • Email: {acc['email']}")
                print(f"    • Хранилище: {acc['storage_used']} GB")
        
        return data
        
    except FileNotFoundError:
        print(" Ошибка: Файл 7.json не найден!")
        print("  Убедитесь, что файл находится в той же папке")
        return None
    except Exception as e:
        print(f" Ошибка при работе с JSON: {e}")
        return None


def main():
    """Главная функция"""
    print("\n" + "=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА: РАБОТА С CSV И JSON ФАЙЛАМИ")
    print("=" * 70)
    
    csv_result = analyze_csv_file()
     
    json_result = analyze_json_file()
    
    print("\n" + "=" * 70)
    print("ИТОГИ ВЫПОЛНЕНИЯ:")
    print("=" * 70)
    
    if csv_result:
        print(" CSV файл успешно проанализирован")
    else:
        print(" Ошибка при анализе CSV файла")
    
    if json_result:
        print(" JSON файл успешно проанализирован")
        print(" Создан файл out.json с отфильтрованными данными")
    else:
        print(" Ошибка при анализе JSON файла")
    
    print("\nСозданные файлы в папке:")
    print("  1. analyze_files.py - программа")
    print("  2. 7.csv - исходные данные погоды")
    print("  3. 7.json - исходные данные аккаунтов")
    print("  4. out.json - отфильтрованные данные (создастся автоматически)")

if __name__ == "__main__":
    main()