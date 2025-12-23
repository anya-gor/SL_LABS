import requests
import json
import os

os.makedirs('flags', exist_ok=True)

def get_countries_by_language(language, min_area=100000):
    """
    Получает страны, говорящие на указанном языке, с площадью больше min_area
    """
    base_url = "https://restcountries.com/v3.1/lang"
    
    fields = "name,capital,area,population,flags,languages"

    url = f"{base_url}/{language}?fields={fields}"
    
    print(f"Запрос данных для языка: {language}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        countries = response.json()

        filtered_countries = [
            country for country in countries 
            if 'area' in country and country['area'] > min_area
        ]
        
        print(f"Найдено стран: {len(countries)}, после фильтрации: {len(filtered_countries)}\n")
        return filtered_countries
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных для {language}: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка при разборе JSON для {language}: {e}")
        return []

def save_country_data(countries_data, filename="results.json"):
    """
    Сохраняет данные о странах в JSON файл
    """
    data_to_save = {}
    
    for language, countries in countries_data.items():
        data_to_save[language] = []
        for country in countries:
            country_info = {
                'name': country['name']['common'],
                'capital': country['capital'][0] if country.get('capital') else 'N/A',
                'area': country.get('area', 0),
                'population': country.get('population', 0)
            }
            data_to_save[language].append(country_info)
 
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=2)
    
    print(f"Данные сохранены в файл: {filename}")
    return data_to_save

def find_country_with_max_area(countries_data):
    """
    Находит страну с максимальной площадью для каждого языка
    """
    max_area_countries = {}
    
    for language, countries in countries_data.items():
        if countries:
            max_area_country = max(countries, key=lambda x: x.get('area', 0))
            max_area_countries[language] = max_area_country
    
    return max_area_countries

def download_flags(max_area_countries):
    """
    Скачивает флаги стран с максимальной площадью для каждого языка
    """
    for language, country in max_area_countries.items():
        if country and 'flags' in country and 'png' in country['flags']:
            flag_url = country['flags']['png']
            country_name = country['name']['common'].replace(' ', '_')
            filename = f"flags/{language}_{country_name}_flag.png"
            
            try:
                response = requests.get(flag_url, timeout=10)
                response.raise_for_status()
                
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                print(f"Флаг сохранен: {filename}")
                
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при загрузке флага для {country_name}: {e}")

def print_max_area_countries(max_area_countries):
    """
    Выводит в консоль страны с максимальной площадью для каждого языка
    """
    print("\n" + "="*50)
    print("СТРАНЫ С НАИБОЛЬШЕЙ ПЛОЩАДЬЮ:")
    print("="*50)
    
    for language, country in max_area_countries.items():
        if country:
            print(f"\nЯзык: {language.upper()}")
            print(f"Страна: {country['name']['common']}")
            print(f"Столица: {country['capital'][0] if country.get('capital') else 'N/A'}")
            print(f"Площадь: {country.get('area', 0):,.0f} км²")
            print(f"Население: {country.get('population', 0):,.0f} чел.")
    print("="*50)

def main():
    """
    Основная функция выполнения задания
    """
    languages = ['spanish', 'portuguese', 'german']
    min_area = 100000
    
    print("Начинаем выполнение задания...\n")
    
    countries_data = {}
    for language in languages:
        countries = get_countries_by_language(language, min_area)
        countries_data[language] = countries

    save_country_data(countries_data)
    
    max_area_countries = find_country_with_max_area(countries_data)
    
    print_max_area_countries(max_area_countries)

    print("\nЗагрузка флагов...")
    download_flags(max_area_countries)
    
    print("\n" + "="*50)
    print("Задание выполнено успешно!")

if __name__ == "__main__":
    main()