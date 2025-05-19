with open('path.txt', 'w') as fh:
    fh.write("Alex Korp,3000\n")
    fh.write("Nikita Borisenko,2000\n")
    fh.write("Sitarama Raju,1000\n")

def calculate_salaries(file_path):
    try:
        total_salary = 0
        developer_count = 0

        with open(file_path, "r", encoding="utf-8") as fh:
            for line in fh:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, salary_str = parts
                    try:
                        salary = int(salary_str)
                        total_salary += salary
                        developer_count += 1
                    except ValueError:
                        print(f"⚠️ Помилка: зарплата '{salary_str}' у {name} не є числом.")
        
        if developer_count == 0:
            print("⚠️ Дані відсутні або некоректні.")
            return

        average_salary = total_salary / developer_count
        print(f"Загальна сума зарплат: {total_salary}")
        print(f"Середня зарплата: {average_salary:.2f}")

    except FileNotFoundError:
        print("❌ Помилка: файл не знайдено.")
    except Exception as e:
        print(f"❌ Сталася невідома помилка: {e}")

# Виклик функції
calculate_salaries("path.txt")
