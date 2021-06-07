import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from tkinter import messagebox
window = tk.Tk()
window.config(bg="#FF6FAE")
window.geometry("600x500")
window.title("Currency Converter")

# defining a function


def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = 'http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1'

    if amount == '':
        messagebox.showerror("Exchange Rate", "Please Fill the Amount")
    elif to_currency == '':
        messagebox.showerror("Exchange Rate", "Please Choose the Currency")

    else:
        data = requests.get(url).json()
        currency = from_currency.strip()+to_currency.strip()
        amount = int(amount)
        cc = data['quotes'][currency]
        cur_conv = cc*amount
        E2.insert(0, cur_conv)

        text.insert('end', f'{amount} United State Dollar Equals {cur_conv} {to_currency} \n\n '
                           f'Last Time Update --- \t {datetime.now()}')

# defining function for clear button


def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')

#  Labeling the Sub-title and putting other labels


l1 = Label(window, text="Exchange Rates", font=('sans serif', '10', 'bold'), borderwidth=5)
l1.place(x=250, y=10)

amt = Label(window, text="Amount", font=('sans serif', 10, 'bold'))
amt.place(x=50, y=15)
E1 = Entry(window, width=20, borderwidth=5, font=('sans serif', 10, 'bold'))
E1.place(x=20, y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()
currency_choose1 = ttk.Combobox(window, width=20, textvariable=c1, state='readonly', font=('sans serif', 10, 'bold'))

# Adding combobox drop down list
currency_choose1['values'] = (
                          ' USD',
                          )

currency_choose1.place(x=300, y=40)
currency_choose1.current(0)


E2 = Entry(window, width=20, borderwidth=5, font=('sans serif', 10, 'bold'))
E2.place(x=20, y=80)


currency_choose2 = ttk.Combobox(window, width=20, textvariable=c2, state='readonly', font=('sans serif', '10', 'bold'))

# Adding combobox drop down list to choose currency of a country
currency_choose2['values'] = ('ALL',
                              'AFN',
                              'ARS',
                              'AWG',
                              'AUD',
                              'AZN',
                              'BSD',
                              'BBD',
                              'BYN',
                              'BZD',
                              'BMD',
                              'BOB',
                              'BAM',
                              'BWP',
                              'BGN',
                              'BND',
                              'KHR',
                              'CAD',
                              'KYD',
                              'CLP',
                              'CNY',
                              'COP',
                              'CRC',
                              'HRK',
                              'CUP',
                              'CZK',
                              'DKK',
                              'DOP',
                              'XCD',
                              'EGP',
                              'SVC',
                              'EUR',
                              'FKP',
                              'FJD',
                              'GHS',
                              'GIP',
                              'GTQ',
                              'GGP',
                              'GYD',
                              'HNL',
                              'HKD',
                              'HUF',
                              'ISK',
                              'INR',
                              'IDR',
                              'IRR',
                              'IMP',
                              'ILS',
                              'JMD',
                              'JPY',
                              'KZT',
                              'KPW',
                              'KRW',
                              'KGS',
                              'LAK',
                              'LBP',
                              'LRD',
                              'MKD',
                              'MYR',
                              'MUR',
                              'MXN',
                              'MNT',
                              'MZN',
                              'NAD',
                              'NPR',
                              'ANG',
                              'NZD',
                              'NIO',
                              'NGN',
                              'NOK',
                              'OMR',
                              'PKR',
                              'PAB',
                              'PYG',
                              'PEN',
                              'PHP',
                              'PLN',
                              'QAR',
                              'RON',
                              'RUB',
                              'SHP',
                              'SAR',
                              'RSD',
                              'SCR',
                              'SGD',
                              'SBD',
                              'SOS',
                              'ZAR',
                              'LKR',
                              'SEK ',
                              'CHF',
                              'SRD',
                              'SYP',
                              'TWD',
                              'THB',
                              'TTD',
                              'TRY',
                              'TVD',
                              'UAH',
                              'GBP',
                              'UYU',
                              'UZS',
                              'VEF',
                              'VND',
                              'YER',
                              'ZWD',)

currency_choose2.place(x=300, y=80)
currency_choose2.current()

# Creating a block to display the information
text = Text(window, height=8, width=40, font=('sans serif', '10', 'bold'))
text.place(x=100, y=120)
# Buttons
B = Button(window, text="Convert", command=show_data, font=('sans serif', '10', 'bold'),
           borderwidth=3, bg="#FF6FAE", fg="white")
B.place(x=10, y=130)

clear = Button(window, text="Clear", command=clear, font=('verdana', '10', 'bold'),
               borderwidth=5, bg="#FF6FAE", fg="white")
clear.place(x=20, y=200)

window.mainloop()
