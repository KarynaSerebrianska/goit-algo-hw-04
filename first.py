with open('path.txt', 'w') as fh:
    fh.write("Alex Korp,3000\n")
    fh.write("Nikita Borisenko,2000\n")
    fh.write("Sitarama Raju,1000\n")

def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name, salary_str = parts
                    try:
                        salary = int(salary_str)
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"⚠️ Некоректна зарплата у {name}: {salary_str}")

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("❌ Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"❌ Помилка: {e}")
        return (0, 0)
total, average = total_salary("path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
