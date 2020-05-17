import requests
import tkinter as tk
# from tkinter import *

# number="9958132007"
# message="This is a test message 49"
#
# url="https://www.fast2sms.com/dev/bulk"
# params={"authorization":"5TuB8WFh2Y7cCxsmJiPMXQlHtRd3bNOy6AZLprjUqnkzgGwDSExI8Vl3Z7ONdUTh1CmaebzAqgjpXk0c",
#         "sender_id":"FSTSMS",
#         "message":message,
#         "language":"english",
#         "route":"p",
#         "numbers":number}
#
# response = requests.get(url,params)
# # response = requests.get("https://www.hackerrank.com/")
# print(response)
#
# dic=response.json()
# print(dic["return"])

#creating GUI

root=tk.Tk()                  #creading main window
root.title("Hello TK")       #assign TITLE
root.geometry("300x500")    #assign Window dimensions

font=("Helvetica",22,"bold")
textbox_num = tk.Entry(root,font=font)
textbox_num.pack(fill=tk.X ,pady=20)
# textbox_num.pack(pady=20)

textbox1 = tk.Entry(root)  # Create Textbox
textbox1.pack()         #

root.mainloop()              #Run the GUI Window


