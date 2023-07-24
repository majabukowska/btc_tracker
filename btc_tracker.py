
from common import btc_api
from verify_data import is_btc_api_available
import requests
from tkinter import *


def get_json_btc_tracker(api):
    if is_btc_api_available(api):
        r = requests.get(api).json()
        return r
    else:
        return is_btc_api_available(api)


def create_window(api):
    window = Tk()
    window.geometry("500x500")
    icon = PhotoImage(file='Bitcoin.png')
    window.iconphoto(True, icon)
    window.title("Bitcoin Current Price")
    window.config(background="black")

    label = Label(window, text="Bitcoin Current Price", font=("Rockwell", 24, "bold"), bg="black", fg="white")
    label.pack(pady=20)

    for key, value in get_json_btc_tracker(api).items():
        label_text = f"{key}:" + str(value)
        label = Label(window, text=label_text, font=("Rockwell", 20), bg="black", fg="white")
        label.pack(pady=20)

    window.mainloop()


create_window(btc_api)
