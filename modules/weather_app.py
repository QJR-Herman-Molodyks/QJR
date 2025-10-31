from tkinter import *

def openWeather():
    # from tkinter import *
    import requests
    from PIL import Image
    import io
    import datetime
    from CTkMessagebox import CTkMessagebox
    from customtkinter import CTk, CTkToplevel, CTkLabel, CTkEntry, CTkButton, CTkImage

    API_KEY = "fcf3d71235f8302c4a3b645843faa5b5"

    def weather(window):
        def show():
            city_name = city.get().strip()
            if not city_name:
                return

            link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ua"
            response = requests.get(link)
            data = response.json()

            if data.get("cod") != 200:
                CTkMessagebox(title="Увага!", message="❌ Місто не знайдено!", icon="warning", option_1="Ок")
                return

            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_max = data["main"]["temp_max"]
            temp_min = data["main"]["temp_min"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"].capitalize()
            icon_code = data["weather"][0]["icon"]

            sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
            sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")

            caption = (
                f"📍 Місто: {city_name}\n\n"
                f"🌡 Температура: {temp}°C\n\n"
                f"🥶 Відчувається як: {feels_like}°C\n\n"
                f"🔼 Макс: {temp_max}°C  🔽 Мін: {temp_min}°C\n\n"
                f"💧 Вологість: {humidity}%\n\n"
                f"💨 Вітер: {wind_speed} м/с\n\n"
                f"🌀 Тиск: {pressure} гПа\n\n"
                f"🌅 Схід: {sunrise}  🌇 Захід: {sunset}\n\n"
                f"📖 Опис: {description}"
            )
            weather_info.configure(text=caption, fg_color="#242424")

            icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            img_data = icon_response.content
            image = Image.open(io.BytesIO(img_data))

            weather_icon.image = CTkImage(light_image=image, dark_image=image, size=(100, 100))
            weather_icon.configure(image=weather_icon.image)

        window_weather = Toplevel(window)
        window_weather.geometry("500x500")
        window_weather.title("🌤 Погода")

        city = CTkEntry(window_weather, placeholder_text="Введіть місто", width=250)
        city.place(x=50, y=20)

        search = CTkButton(window_weather, text="🔍 Показати", width=100, command=show)
        search.place(x=320, y=20)

        weather_icon = CTkLabel(window_weather, text="")
        weather_icon.place(x=200, y=70)

        weather_info = CTkLabel(
            window_weather,
            text="",
            font=("Consolas", 13),
            wraplength=450,
        )
        weather_info.place(x=120, y=180)

        window_weather.lift()
        window_weather.after(100, lambda: window_weather.lift())

    # if __name__ == "__main__":
    app = Tk()
    app.geometry("600x400")
    weather(app)
    # app.bgcolor("#1e1e1e")
    app.mainloop()
    #     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     time_label.configure(text=f"Поточний час: {now}")
    #     window.after(1000, update_time)
    #
