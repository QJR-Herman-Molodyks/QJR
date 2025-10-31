def openBrowser():
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
    import requests
    from bs4 import BeautifulSoup

    def fetch_website():
        url = entry.get().strip()
        if not url.startswith("http"):
            url = "http://" + url  # якщо користувач не написав http/https

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # перевірка на помилки
            soup = BeautifulSoup(response.text, "html.parser")

            # Отримуємо тільки текст сторінки (без HTML тегів)
            page_text = soup.get_text(separator="\n", strip=True)

            text_area.delete(1.0, tk.END)  # очищення поля
            text_area.insert(tk.END, page_text)  # вставка вмісту

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити сайт:\n{e}")

    # --- GUI ---
    root = tk.Tk()
    root.title("Міні WebBrowser")
    root.geometry("800x600")

    # Поле вводу для URL
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Введіть URL:").pack(side=tk.LEFT, padx=5)
    entry = tk.Entry(frame, width=50)
    entry.pack(side=tk.LEFT, padx=5)
    btn = tk.Button(frame, text="Завантажити", command=fetch_website)
    btn.pack(side=tk.LEFT, padx=5)

    # Текстове поле для відображення даних
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11))
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    root.mainloop()
