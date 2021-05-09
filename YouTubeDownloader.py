import self as self
from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from threading import Thread
import PIL
import tkinter as tk
file_size = 0


def progress(stream=None, chunk=None,  remaining=None):
    file_downloaded = (file_size-remaining)
    per = round((file_downloaded/file_size)*100, 1)
    dBtn.config(text=f'{per}% downloaded')


def startDownload():
    global file_size
    try:
        URL = urlField.get()
        dBtn.config(text='Please wait...', activeforeground='#FFF')
        dBtn.config(state=DISABLED)
        path_save = askdirectory()
        if path_save is None:
            return
        ob = YouTube(URL, on_progress_callback=progress)
        strm = ob.streams[0]
        x = ob.description.split("|")
        file_size = strm.filesize
        dfile_size = file_size
        dfile_size /= 1000000
        dfile_size = round(dfile_size, 2)
        label.config(text='Size: ' + str(dfile_size) + ' MB')
        label.pack(side=TOP, pady=10)
        desc.config(text=ob.title + '\n\n' + 'Label: ' + ob.author + '\n\n' + 'length: ' + str(round(ob.length/60, 1)) + ' mins\n\n'
                    'Views: ' + str(round(ob.views/1000000, 2)) + 'M')
        desc.pack(side=TOP, pady=10)
        strm.download(path_save, strm.title)
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", 'Downloaded Successfully')
        urlField.delete(0, END)
        label.pack_forget()
        desc.pack_forget()
        dBtn.config(text='Start Download')

    except Exception as e:
        print(e)
        print('Error!!')


def startDownloadthread():
    thread = Thread(target=startDownload)
    thread.start()


main = Tk()

main.title("YouTube Downloader")
main.config(bg='#FFF', padx=10)

main.iconbitmap('C:\\Users\\Darshita\\Desktop\\Sem 6\\SGP\\Friday\\images\\youtube-ios-app.ico')

main.geometry("500x600")

# root = tk.Tk()
# file = PhotoImage(file='C:\\Users\\Darshita\\Desktop\\Sem 6\\SGP\\18ce113\\images\\photo.png', master=root)
# # BTC_img = PIL.ImageTk.PhotoImage(file)
# # BTC_img_label = tk.Label(self, image=BTC_img)
# # BTC_img_label.image = BTC_img
# # BTC_img_label.grid(row=2, column=0)
# headingIcon = Label(root, image=file)
# headingIcon.pack(side=TOP)

urlField = Entry(main, font=("Courier", 18), bg='#C0C0C0', justify=CENTER)

urlField.pack(side=TOP, fill=X, padx=10, pady=15)

dBtn = Button(main, text="Start Download", font=(
    "Courier", 18), relief='ridge', bg='#5C85FB', activeforeground='red', command=startDownloadthread)
dBtn.pack(side=TOP)
label = Label(main, text='')
desc = Label(main, text='')
main.mainloop()