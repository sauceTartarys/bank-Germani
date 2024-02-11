import requests
import tkinter as tk


def get_currency_rates():

    api_url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:
        response = requests.get(api_url)
        data = response.json()


        currency_rates = data.get("rates", {})
        return currency_rates
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def update_rates():
    rates = get_currency_rates()


    text.delete(1.0, tk.END)
    for currency, rate in rates.items():
        text.insert(tk.END, f"{currency}: {rate}\n")



root = tk.Tk()
root.title("Курси валют")


update_button = tk.Button(root, text="Оновити курси", command=update_rates)
update_button.pack(pady=10)


text = tk.Text(root, height=20, width=40)
text.pack()


update_rates()


root.mainloop()