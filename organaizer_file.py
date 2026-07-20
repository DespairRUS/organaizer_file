from pathlib import Path
import os
import shutil

def get_extensions(filename):
    return Path(filename).suffix

FILE_TYPES = {
    "Изображения": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", 
        ".svg", ".tiff", ".tif", ".ico", ".webp", 
        ".heic", ".raw", ".psd"
    ],
    "Документы": [
        ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", 
        ".pptx", ".ppt", ".odt", ".ods", ".odp", ".rtf", 
        ".csv", ".tsv", ".log", ".md", ".tex", ".wpd"
    ],
    "Архивы": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", 
        ".xz", ".iso", ".img", ".cab", ".msi", ".pkg"
    ],
    "Программы": [
        ".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", 
        ".sh", ".bash", ".zsh", ".app", ".apk", ".jar", 
        ".py", ".js", ".exe"
    ],
    "Музыка": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", 
        ".m4a", ".opus", ".amr", ".aiff", ".alac"
    ],
    "Видео": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", 
        ".webm", ".m4v", ".mpg", ".mpeg", ".3gp", ".ogv"
    ],
    "Web": [
        ".html", ".htm", ".css", ".js", ".json", ".xml", 
        ".php", ".asp", ".jsp", ".erb", ".ts", ".jsx", ".tsx"
    ],
    "Книги": [
        ".epub", ".mobi", ".azw3", ".fb2", ".djvu", 
        ".chm", ".lit", ".lrf"
    ],
    "Базы данных": [
        ".db", ".sqlite", ".sql", ".mdb", ".accdb", 
        ".dbf", ".csv"
    ],
    "Остальное": []

}

def get_category(filename):
    ext = get_extensions(filename)
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Остальное"

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Ошибка: Папка '{folder_path}' не найдена!")
        return
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            continue
        
        category = get_category(item)
        dest_folder = os.path.join(folder_path, category)
        os.makedirs(dest_folder, exist_ok=True)
        
        dest_path = os.path.join(dest_folder, item)
        shutil.move(item_path, dest_path)
        print(f"Перемещён: {item} -> {category}/")
    
    print("Готово!")

if __name__ == "__main__":
    test_folder = r"C:\Users\DespairRUS\Downloads"  # ИЗМЕНИ ПУТЬ!
    organize_files(test_folder)