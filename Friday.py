from Libraries import *

numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
a = {'name': 'your email'}


#for text to speech
engine = pyttsx3.init('sapi5') #sapi5 is a microsoft speech api
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #voice Id to "0" is for Male voice and "1" for female voice

window = Tk() #GUI

global var
global var1

var = StringVar()
var1 = StringVar()


#recognizes your voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def _getints(self, string):
    """Internal function."""
    if string:
        return tuple(map(self.tk.getint, self.tk.splitlist(string)))

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Darshita\\Desktop\\SEM 6\\SGP\\js.png")
    speak("screenshot taken")

def TakeHindi():
    command = sr.Recognizer() #sr to access audio from system's microphone
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.......")
            query = command.recognize_google(audio,language="hi")
            print(f"You said : {query}")

        except Exception as e:
            print(e)
            return 'None'

        return query.lower()
def Trans():
    speak("Tell me the line!")
    line = TakeHindi()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(Text)
    print(Text)

def cpu():
    usage = str(psutil.cpu_percent())
    print("CPU is at", usage, "%")
    speak("CPU is at"+usage+ "%")

    battery = psutil.sensors_battery()
    print("battery is at", battery.percent, "%")
    speak("battery is at")
    speak(battery.percent)
    speak("%")

#Greets us according to the time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        var.set("Good Morning sir")
        window.update()
        speak("Good Morning sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon sir!")
        window.update()
        speak("Good Afternoon sir!")
    else:
        var.set("Good Evening sir")
        window.update()
        speak("Good Evening sir!")
    speak("I am Friday! How may I help you ?")  #Assistant name


#takes command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing...")
        queryy = r.recognize_google(audio, language='en-US')
        print(f"User : {queryy}\n")
    except Exception as ee:
        print("can't recognize say that again...")
        print(ee)
        return "None"
        #takeCommand()
    return queryy

#GUI - format
def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wishme()
    while True:
        btn1.configure(bg='orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        #dynamic search on wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #give command like search for Marvel on Wikipedia
            results = wikipedia.summary(query, 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #answers any computational or geographical questions
        elif 'question' in query:
            speak('Ask any computational or geographical question')
            question = takeCommand()
            app_id = "75T4VE-U49LKHAVJJ"
            client = wolframalpha.Client('75T4VE-U49LKHAVJJ') #Python API Wrapper
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        #opens the course era website
        elif 'open course era' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.get('chrome').open("coursera.com")

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        #tells us the joke
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #plays music stored in your folder
        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C:\\Users\\Darshita\\Desktop\\Sem 6\\SGP\\18ce113\\songs'  # Enter the Path of Music Library
            songs = os.listdir(music_dir)
            n = random.randint(0, 27)
            os.startfile(os.path.join(music_dir, songs[n]))

        #tells us the current time
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        #tells us the current date
        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'how old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        #opens windows media player
        elif 'open windows media player' in query:
            var.set("opening windows media Player")
            window.update()
            speak("opening windows media player")
            path = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"  #Enter the correct Path according to your system
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Friday Sir")
            window.update()
            speak('myself Friday sir')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Friday')
            window.update()
            speak('Hello Everyone! My self Friday')

        #converts any text to speech
        elif 'text to speech' in query:
            text = input("Enter something:")
            speak(text)

        #translates hindi into english
        elif "translate" in query:
            Trans()

        #opens youtube
        elif 'open youtube' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("youtube.com")

        #searches someting in youtube
        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())

        #opens google
        elif 'open google' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("google.com")

        #opens stack overflow website
        elif 'open stack overflow' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("stackoverflow.com")

        #opens notepad in the system
        elif 'open notepad' in query:
            os.system('notepad')
            speak('Done for you!')

        #open microsoft word
        elif 'open word' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"
            os.startfile(appPath)

        #opens microsoft powerpoint
        elif 'open powerpoint' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE"
            os.startfile(appPath)

        #opens microsoft excel
        elif 'open excel' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE"
            os.startfile(appPath)

        #takes the screenshot of full screen
        elif "screenshot" in query:
            screenshot()

        #tells the cpu usage and battery percentage
        elif 'cpu' in query:
            cpu()

        #tells us the current temperature
        elif "temperature" in query:
            search = "temprature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print("current", search, "is", temp)

        #tells some of the top headlines of news
        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    'https://newsapi.org/v2/top-headlines?country=in&apiKey=e23cd72a75964e39a02b2f8be9186388')
                data = json.load(jsonObj)
                i = 1
                speak("here are some top news from Times of India")
                print("==========TIMES OF INDIA==========")

                for item in data['articles']:
                    print(str(i) + '-' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '-' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        #sends an email with or without an attachment
        elif 'email' in query:
            speak("what you want to do?")
            workToDo = takeCommand().lower()

            try:
                if 'file' in workToDo:
                    emailattach()
                    speak("Email has been sent !")
                    print("Email has been sent !")

                elif 'text' in workToDo:
                    speak("what should i sent???")
                    content = takeCommand()
                    to = "darshitashah45@gmail.com"
                    sendMessageEmail(to, content)
                    speak("Email has been sent !")
                    print("Email has been sent !")

            except Exception as e:
                print(e)
                speak("Sorry ,i am not able to send this email!")

        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile(
                'C:\\Users\\Darshita\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit)')  #Enter the correct Path according to your system

        elif 'open code blocks' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile(
                "C:\\Program Files\\CodeBlocks\\codeblocks.exe")  #Enter the correct Path according to your system

        elif 'open anaconda prompt' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile(
                "C:\\Users\\Darshita\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Prompt (Miniconda3)")  #Enter the correct Path according to your system

        #tells the information regarding our weather and location
        elif 'weather' in query:
            weather()

        #performs an addition
        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result' + str(sum))
                    window.update()
                    speak('here is result' + str(sum))
                    print(str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit

        #sets the alarm of a particular time
        elif 'alarm' in query:
            speak("Enter the time")
            time = input("Enter the time : ")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir")
                    playsound('C:\\Users\\Darshita\\Downloads\\abc.mp3')
                    speak("alarm closed")
                elif now > time:
                    break

        #checks the internet speed
        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            print("sir we have", dl, "bit per second downloading speed and", up, "bit per second uploading speed")
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        #remembers something for you
        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember" + rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        #changes his voice
        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        #says the meaning of a given word stored in a json file
        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        #captures an image
        elif 'click photo' in query:
            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cam = camera
            count = 0

            while True:
                ret, img = cam.read()
                cv2.imshow("Test", img)
                if not ret:
                    break
                k = cv2.waitKey(1)
                if k % 256 == 27:
                    # For Esc key
                    print("Close")
                    break
                elif k % 256 == 32:
                    # For Space key
                    print("Image " + str(count) + "saved")
                    file = 'C:/Users/Darshita/Desktop/images/img' + str(count) + '.jpg'
                    cv2.imwrite(file, img)
                    count += 1
            cam.release
            cv2.destroyAllWindows

        elif 'record a video' in query:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            rec = cv2.VideoWriter("C:\\Users\\Darshita\\Desktop\\videos\\Video.mp4", fourcc, 17, (640, 480))

            while(cap.isOpened()):
                ret, frame=cap.read()
                if(ret==True):
                    rec.write(frame)
                    cv2.imshow('output', frame)
                    if(cv2.waitKey(6) & 0xFF == ord('q')):
                        break
                else:
                    break

            cap.release()
            cv2.destroyAllWindows()

        #opens the camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cap(captureDevice) = camera
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(10)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        #sends whatsapp messages to a person commanded by a user
        elif 'send message to abc' in query:
            speak("what should i say?")
            say = takeCommand()
            speak("tell me the number")
            no = takeCommand()
            print(type(no))
            no = no.replace(" ", "")
            no = "+91" + no
            print(no)
            speak("set the time")
            speak("tell me the hours")
            hr = takeCommand()
            speak("tell me the minutes")
            min = takeCommand()
            w.sendwhatmsg(f"{no}", f"{say}", int(hr), int(min))
            speak(("message sent"))

        #shutdowns the machine
        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        #seaches a particular command in google
        else:
            search = 'https://www.google.com/search?q=' + query
            webbrowser.open(search)


#GUI structure
def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i)) for i in range(100)]
window.title('FRIDAY')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='WISH ME', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='PLAY', width=20, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()