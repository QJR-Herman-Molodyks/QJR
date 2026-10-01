import requests

def gethtmlbyurl():
    while True:

        url = input("Enter URL: ").strip()
        if not url.startswith("http"):
            url = "http://" + url  # якщо користувач не написав http/https
        if url == "exit":
            break
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # перевірка на помилки
            print(response.text)
        except requests.exceptions.RequestException as e:
            return f"Error fetching the URL: {e}"

gethtmlbyurl()