from datetime import datetime

DATE_FORMAT_PATTERNS = [
    "%Y.%m.%d %H:%M:%S", 
    "%Y.%m.%d",
    "%d-%m-%Y %H:%M:%S",
    "%d-%m-%Y",
    "%d/%m/%Y %H:%M:%S", 
    "%d/%m/%Y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",  
    "%d.%m.%Y %H:%M:%S",
    "%d.%m.%Y",
    "%m/%d/%Y %H:%M:%S",
    "%m/%d/%Y",  
    "%m-%d-%Y %H:%M:%S",
    "%m-%d-%Y"  
]

def display_current_datetime():
    now = datetime.now()
    print(f"Текущее время: {now.strftime('%H:%M:%S')}")
    print(f"Текущая дата: {now.strftime('%Y-%m-%d')}")

def calculate_date_difference(first_date, second_date, unit="default"):
    time_difference = first_date - second_date
    if unit == "default":
        return time_difference
    seconds = time_difference.total_seconds()
    units_map = {
        "second": seconds,
        "minute": seconds / 60,
        "hour": seconds / 3600,
        "day": seconds / 86400,
        "year": seconds / 31536000
    }
    return units_map.get(unit, "Invalid unit")

def parse_date_from_string(date_text):
    for pattern in DATE_FORMAT_PATTERNS:
        try:
            return datetime.strptime(date_text, pattern)
        except ValueError:
            continue
    print(f"Не удалось разобрать дату из строки: {date_text}")
    return None

display_current_datetime()

date1 = parse_date_from_string("2024.06.21 18:25:30")
date2 = parse_date_from_string("16/05/2023 08:21:10")
if date1 and date2:
    days_diff = calculate_date_difference(date1, date2, "day")
    print(f"Разница между датами в днях: {days_diff}")
