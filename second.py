# Створення тестового файлу з даними
with open('cats.txt', 'w') as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    fh.write("60b90c2413067a15887e1ae2,Vika,1\n")
    fh.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    fh.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    fh.write("60b90c4613067a15887e1ae5,Tessi,5\n")

# Основна функція
def get_cats_info(path):
    cats = []  # список, який збиратиме інформацію про котиків
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age  
                    })
    except FileNotFoundError:
        print("❌ Файл не знайдено.")
    except Exception as e:
        print(f"❌ Помилка при читанні файлу: {e}")
    return cats

# Виклик функції з правильним шляхом
cats_info = get_cats_info("cats.txt")
print(cats_info)
