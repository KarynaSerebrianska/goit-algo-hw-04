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
