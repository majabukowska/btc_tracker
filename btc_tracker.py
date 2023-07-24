from datetime import datetime
from common import btc_api
from verify_data import is_btc_api_available
import requests
from tkinter import *


def get_json_btc_tracker(api):
    if is_btc_api_available(api):
        r = requests.get(api).json()
        time = datetime.now().strftime("%H:%M:%S")
        return r, time
    else:
        return is_btc_api_available(api)


def create_window(api):
    response, time = get_json_btc_tracker(api)
    window = Tk()
    window.geometry("500x400")
    icon = PhotoImage(file='Bitcoin.png')
    window.iconphoto(True, icon)
    window.title("Bitcoin Current Price")
    window.config(background="black")

    label = Label(window, text="Bitcoin Current Price", font=("Rockwell", 24, "bold"), bg="black", fg="white")
    label.pack(pady=20)

    for key, value in response.items():
        label_text = f"{key}: " + str(value)
        label = Label(window, text=label_text, font=("Rockwell", 20), bg="black", fg="white")
        label.pack(pady=20)

    label = Label(window, text="Updated at: " + str(time), font=("Rockwell", 20), bg="black", fg="white")
    label.pack(pady=20)
    window.mainloop()


if __name__ == '__main__':
    create_window(btc_api)
