import requests
import tkinter as tk
# from tkinter import *

def messagesender(num,msg):
    number=num
    message=msg
    API_KEY ="8TuB8WFh2Y7cCxsmJiPMXQlHtRd3bNOy6AZLprjUqnkzgGwDSExI8Vl3Z7ONdUTh1CmaebzAqgjpXk0c"

    url="https://www.fast2sms.com/dev/bulk"
    params={"authorization":API_KEY,
            "sender_id":"FSTSMS",
            "message":message,
            "language":"english",
            "route":"p",
            "numbers":number}

    response = requests.get(url,params)
    print(response)

    dic=response.json()
    print(dic["return"])
    return dic["return"]

def submit():
    # print(tb_msg.get("1.0",tk.END))
    status=messagesender(tb_num.get(),tb_msg.get("1.0",tk.END))
    if status == True :
        # txt.set("Message Send : "+str(status))
        txt.set("Message Send")
    else:
        txt.set("Message Failed")

# #creating GUI

root=tk.Tk()
root.title("Message Sender")
root.geometry("300x390")

photo = tk.PhotoImage(file = "msg-icon.png")
root.iconphoto(False,photo )

font1=("Arial",9,"bold")
font2=("Helvetica",12,"bold")

## Number Input  ---------------------------------------------
lb_num=tk.Label(root,text="To Mobile : ",font=font1)
lb_num.grid(row=0,columnspan=2,padx=5,pady=5,sticky=tk.W)

tb_num = tk.Entry(root,font=font2,width=31)
tb_num.grid(row=1,columnspan=2,padx=5,pady=5,sticky=tk.W,ipady=3,ipadx=3)

lb_ex=tk.Label(root,text="Ex: 9999999991,09999999991,919999999991 ... ",fg="green",font=("arial",8,))
lb_ex.grid(row=2,columnspan=2,padx=5,pady=5,sticky=tk.W)

## Message Input-----------------------------------------------
lb_msg=tk.Label(root,text="Text MSG: ",font=font1)
lb_msg.grid(row=3,columnspan=2,padx=5,pady=5,sticky=tk.W)

tb_msg = tk.Text(root,font=font2,width=31,height=10)
tb_msg.grid(row=4,columnspan=2,padx=5,pady=5,sticky=tk.W,ipady=3,ipadx=3)

## Submit -----------------------------------------------

btn=tk.Button(root,text="Send SMS",fg="WHite",bg="#0073b7",command=submit)
btn.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

txt=tk.StringVar()
txt.set("ONLINE")
lb_status=tk.Label(root,textvariable=txt,fg="green",font=("arial",8,"bold"))
lb_status.grid(row=5,column=1,padx=5,pady=5,sticky=tk.E)

root.mainloop()


##  ------------  Adding Email ----------------------------

