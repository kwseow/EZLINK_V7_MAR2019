import tkinter
import tkinter.messagebox
import tkinter.filedialog
 
window = tkinter.Tk()

#set the window's size
window.geometry("300x300")

def displayFileDialog():
  filename =  tkinter.filedialog.askopenfilename(\
    initialdir = "/",title = "Select file",\
    filetypes = (("jpeg files","*.jpg"),\
                 ("all files","*.*")))
  print (filename)
  return
  
#Add a button
button = tkinter.Button(window, text="File...", bg="gray", command=displayFileDialog)
button.config(font=("Courier", 30))
button.pack(side="top", expand=tkinter.YES)

window.mainloop()





