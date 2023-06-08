import tkinter
import pyshorteners
import webbrowser


window= tkinter.Tk()
window.title("Url Sorter")
window.geometry("400x500")
window.resizable(0,0) # restrict user to resize window
label=tkinter.Label(window,text="URL Shorterner" ,font="Helvetica").pack(pady=20)
l2=tkinter.Label(window,text="Enter URL").pack(pady=20)



inputBox=tkinter.Text(window, height=1, width=40)
inputBox.pack() #we use pack in next line because get()[used in getIn is method of text,not pack()]

def web(url):
    webbrowser.open_new(url)
    

def getIn():
    url=inputBox.get("1.0","end-1c")
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    l4=tkinter.Label(window,text="Your Shorter Url is").pack()
    try:
        l3=tkinter.Label(window,text=short_url,fg="blue")
        l3.pack()
        l3.bind("<Button-2>",lambda e:web(short_url))
    except ValueError:
        l4=tkinter.Label(window,text="Please Enter valid URL").pack()

    
    

    print(short_url)
    
btn=tkinter.Button(text="Click",bg="Black",fg="white",command=getIn).pack(pady=10)

window.mainloop()


