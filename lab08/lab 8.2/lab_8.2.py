import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://worldathletics.org/records/toplists/jumps/{event}/all/{gender}/senior/{year}"

events = ["high-jump", "pole-vault", "long-jump", "triple-jump"]
genders = ["men", "women"]
years = range(2001, 2025)

results = []
print("Начинаем сбор данных для лабораторной...")

with open("top_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Gender", "Event", "Athlete", "Country", "Result", "Date"])
    
    for year in years:
        for gender in genders:
            for event in events:
                try:
                    url = BASE_URL.format(event=event, gender=gender, year=year)
                    
                    print(f"Запрос: {year} {gender} {event}")
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code != 200:
                        print(f"  Пропускаем (статус {response.status_code})")
                        continue
                    
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    table = soup.find('table', class_='records-table')
                    
                    if not table:
                        print("  Таблица не найдена")
                        continue
                    
                    tbody = table.find('tbody')
                    if not tbody:
                        print("  Нет данных в таблице")
                        continue
                    
                    first_row = tbody.find('tr')
                    if not first_row:
                        print("  Нет строк данных")
                        continue
                    
                    mark = first_row.find('td', {'data-th': 'Mark'})
                    competitor = first_row.find('td', {'data-th': 'Competitor'})
                    nat = first_row.find('td', {'data-th': 'Nat'})
                    date = first_row.find('td', {'data-th': 'Date'})
                    
                    if mark and competitor:
                        event_name = event.replace('-', ' ').title()
                        gender_name = "Men" if gender == "men" else "Women"
                        
                        writer.writerow([
                            year,
                            gender_name,
                            event_name,
                            competitor.text.strip(),
                            nat.text.strip() if nat else '',
                            mark.text.strip(),
                            date.text.strip() if date else ''
                        ])
                        
                        print(f"   Добавлено: {competitor.text.strip()} - {mark.text.strip()}")
                        results.append(1)
                    
                    else:
                        print("  Нет данных о результате")
                    
                    time.sleep(0.5)
                    
                except Exception as e:
                    print(f"  Ошибка: {e}")
                    continue

print(f"\n{'='*50}")
print(f"ГОТОВО! Собрано {len(results)} записей.")
print(f"Файл: top_results.csv")
print(f"{'='*50}")