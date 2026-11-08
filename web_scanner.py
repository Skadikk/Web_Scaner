import requests
import concurrent.futures

paths = ["admin", "login", "backup", "config", "wp-admin", "secret", "robots.txt"]
url = input("Введите ссылку: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def check_path(url, path):
    full_url = f"{url}/{path}"
    try:
        response = requests.get(full_url, headers=headers, timeout=3)
        if response.status_code in [200, 403]:
            print(f"Найдено: {full_url}")
            with open("records.txt", "a") as file:
                file.write(f"{full_url}\n")
                print(f"Найдено: {full_url} (записано в records.txt)")
    except requests.exceptions.RequestException:
        pass

if __name__ == "__main__":
    print(f"Сканирую {url}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_path, url, path) for path in paths]
        for future in concurrent.futures.as_completed(futures):
            pass
            
    print("Готово")
