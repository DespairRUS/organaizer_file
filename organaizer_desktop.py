import os
import shutil

def get_first_letter(name):
    if not name:
        return '#'
    
    first_char = name[0].upper()
    if first_char.isalpha():
        return first_char
    else:
        return '#'

def organize_desktop_by_letters():
    desktop_path = os.path.expanduser('~/Desktop')

    if not os.path.exists(desktop_path):
        print(f"Ошибка: Папка '{desktop_path}' не найдена!")
        return

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        print(f"Объект: {item}")
        if os.path.isdir(item_path):
            print(f"  - Это папка, пропускаем")
            continue
        
        if item.endswith('.lnk'):
            print(f"  - Это ярлык, пытаемся переместить")

        letter = get_first_letter(item)
        print(f"  - Первая буква: {letter}")
        letter_folder = os.path.join(desktop_path, letter)
        os.makedirs(letter_folder, exist_ok=True)

        dest_path = os.path.join(letter_folder, item)
        try:
            shutil.move(item_path, dest_path)
            print(f"Перемещён: {item} -> {letter}/")
        except Exception as e:
            print(f"  - ОШИБКА при перемещении {item}: {e}")

if __name__ == "__main__":
    organize_desktop_by_letters()