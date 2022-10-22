from tkinter import *
import requests
import json

root = Tk()
root.title("News Widget")
root.geometry("600x500")
root.overrideredirect(True)

newsupdate = Label(root,text = "BBC News Update",font = "arial 15 bold",)
newsupdate.place(relx = 0.5,rely = 0.1,anchor = CENTER)

news1 = Label(root,font = "arial 10 bold",fg = "red",wraplength = 500,justify = LEFT)
news1.place(relx = 0.1,rely = 0.18,anchor = W)
news_desc1 = Label(root,font = "arial 10 bold",fg = "black",wraplength = 500,justify = LEFT)
news_desc1.place(relx = 0.1,rely = 0.26,anchor = W)

news2 = Label(root,font = "arial 10 bold",fg = "red",wraplength = 500,justify = LEFT)
news2.place(relx = 0.1,rely = 0.34,anchor = W)
news_desc2 = Label(root,font = "arial 10 bold",fg = "black",wraplength = 500,justify = LEFT)
news_desc2.place(relx = 0.1,rely = 0.42,anchor = W)

news3 = Label(root,font = "arial 10 bold",fg = "red",wraplength = 500,justify = LEFT)
news3.place(relx = 0.1,rely = 0.5,anchor = W)
news_desc3 = Label(root,font = "arial 10 bold",fg = "black",wraplength = 500,justify = LEFT)
news_desc3.place(relx = 0.1,rely = 0.58,anchor = W)

news4 = Label(root,font = "arial 10 bold",fg = "red",wraplength = 500,justify = LEFT)
news4.place(relx = 0.1,rely = 0.66,anchor = W)
news_desc4 = Label(root,font = "arial 10 bold",fg = "black",wraplength = 500,justify = LEFT)
news_desc4.place(relx = 0.1,rely = 0.74,anchor = W)

news5 = Label(root,font = "arial 10 bold",fg = "red",wraplength = 500,justify = LEFT)
news5.place(relx = 0.1,rely = 0.82,anchor = W)
news_desc5 = Label(root,font = "arial 10 bold",fg = "black",wraplength = 500,justify = LEFT)
news_desc5.place(relx = 0.1,rely = 0.9,anchor = W)

api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=8587a4a355f147d7915733fad619dc99")
open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page["articles"][0]["title"]
desc1 = open_bbc_page["articles"][0]["description"]

title2 = open_bbc_page["articles"][1]["title"]
desc2 = open_bbc_page["articles"][1]["description"]

title3 = open_bbc_page["articles"][2]["title"]
desc3 = open_bbc_page["articles"][2]["description"]

title4 = open_bbc_page["articles"][3]["title"]
desc4 = open_bbc_page["articles"][3]["description"]

title5 = open_bbc_page["articles"][4]["title"]
desc5 = open_bbc_page["articles"][4]["description"]

news1["text"] = "Title 1: " + title1
news_desc1["text"] = "Description: " + desc1

news2["text"] = "Title 2: " + title2
news_desc2["text"] = "Description: " + desc2

news3["text"] = "Title 3: " + title3
news_desc3["text"] = "Description: " + desc3

news4["text"] = "Title 4: " + title4
news_desc4["text"] = "Description: " + desc4

news5["text"] = "Title 5: " + title5
news_desc5["text"] = "Description: " + desc5

root.mainloop()
