import datetime
import time
from Speak import Say
import wikipedia
import pywhatkit
import pyautogui
import subprocess
import os
from Listen import Listen
import random
import wolframalpha
import screen_brightness_control as sbc
#from PyDictionary import PyDictionary
import alarm
from requests import get
from pynput.mouse import Controller


mouse = Controller()
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)


def Date():
    date = datetime.date.today()
    Say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour<12:
        Say("Good Morning! ")
    elif hour >= 12 and hour<15:
        Say("Good Noon!")
    elif hour >= 15 and hour <18:
        Say("Good Afternoon!")
    elif hour >= 18 and hour <19:
        Say("Good Evening!")
    else:
        Say("Hi there")
    Say("What can I do for you?")


def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()
    elif "open camera" in query:
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif "take photo" in query:
        pyautogui.press('enter')
    elif "press enter" in query:
        pyautogui.press('enter')
    elif "move mouse up" in query:
        mouse.move(0, -40)
    elif "move mouse down" in query:
        mouse.move(0, 40)
    elif "move mouse right" in query:
        mouse.move(40, 0)
    elif "move mouse left" in query:
        mouse.move(-40, 0)
    elif "move mouse top right" in query:
        mouse.move(40, -40)
    elif "move mouse top left" in query:
        mouse.move(-40, -40)
    elif "move mouse bottom left" in query:
        mouse.move(-40, 40)
    elif "move mouse bottom right" in query:
        mouse.move(40, 40)
    elif "date" in query:
        Date()
    elif "close camera" in query:
        subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    elif "day" in query:
        Day()
    elif "open chrome" in query:
        gcpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(gcpath)
    elif "close chrome" in query:
        Say("Closing")
        os.system("taskkill /f /im chrome.exe")
    elif "open youtube" in query:
        Say("What should I play on youtube?")
        ym = Listen().lower()
        pywhatkit.playonyt(f"{ym}")
    elif "play music" in query:
        Say("What should I play?")
        ym = Listen().lower()
        pywhatkit.playonyt(f"{ym}")
    # if you want to play music from your local drive, comment the previous "play music" command's code and uncomment the below. No worries, you will still be able to use the Youtube command.
    # elif "play music" in query:
    #     music_dir = "(your musics directory path)"
    #     songs = os.listdir(music_dir)
    #     mn = random.randint(0, 40)
    #     os.startfile(os.path.join(music_dir, songs[mn]))
    # elif "close music" in query:
    #     Say("Closing")
    #     os.system("taskkill /f /im wmplayer.exe")
    elif "open notepad" in query:
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)
    elif "close notepad" in query:
        Say("Closing")
        os.system("taskkill /f /im notepad.exe")
    elif "increase brightness" in query:
        sbc.set_brightness('+10')
    elif "decrease brightness" in query:
        sbc.set_brightness('-10')
    elif "volume up" in query:
        pyautogui.press("volumeup")
    elif "volume down" in query:
        pyautogui.press("volumedown")
    elif "mute" in query:
        pyautogui.press("volumemute")
    elif "pause" in query:
        pyautogui.press("k")
    elif "exit full screen" in query:
        pyautogui.press('esc')
    elif "play" in query:
        pyautogui.press("space")
    elif "full screen" in query:
        pyautogui.press("f")
    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        Say(f"your IP address is {ip}")
    elif "restart video" in query:
        pyautogui.press("0")
    elif "open word" in query:
        mswpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(mswpath)
    elif "close word" in query:
        Say("closing...")
        os.system("taskkill /f /im WINWORD.EXE")
    elif "copy" in query:
        with pyautogui.hold('ctrl'):
            pyautogui.press(['c'])
            Say('Copied')
    elif "paste" in query:
        with pyautogui.hold('ctrl'):
            pyautogui.press(['v'])
    elif "save" in query:
        with pyautogui.hold('ctrl'):
            pyautogui.press(['s'])
    elif "mouse click" in query:
        pyautogui.click()
    elif "mouse right click" in query:
        pyautogui.click(button='right')
    elif "mouse double click" in query:
        pyautogui.doubleClick()
    elif "shutdown" in query:
        pywhatkit.shutdown(10)
        Say("Your computer is going to be shutdown within, 8 seconds.")
    elif "restart computer" in query:
        Say("Restarting")
        os.system("shutdown /r")
    elif "sleep computer" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who", "").replace("wikipedia", "").replace("what", "").replace("is", "").replace("tell", "").replace("me", "").replace("about", "").replace("from", "")
        result = wikipedia.summary(name)
        Say(result)
    elif "open google" in tag:
        Say("What should I search?")
        result = Listen()
        pywhatkit.search(result)
    elif "activate voice typing" in tag:
        Say("Voice typing activated. To deactivate it, just say deactivate voice typing")
        writings = Listen().lower()
        while writings != "deactivate voice typing":
            pyautogui.typewrite(writings)
            pyautogui.press('space')
            writings = Listen().lower()
        Say("Voice typing deactivated")
        # agreement = Listen().lower()
        # if "yes" in agreement or "save" in agreement or "yeah" in agreement:
           # with pyautogui.hold('ctrl'):
               # pyautogui.press(['s'])
            #Say("Tell me a name for the file")
           # filename = Listen().lower()
            # pyautogui.typewrite(filename)
            # pyautogui.press("enter")
        # else:
            #Say("Okay, voice typing deactivated")
    elif "calculation" in tag:
        Say("Calculation mode activated. To deactivate it, just say deactivate calculation")
        math = Listen().lower()
        while math != "deactivate calculation":
            if math != "deactivate calculation":
                try:
                    app_id = "6UXUHA-27VPL5W6QU"
                    client = wolframalpha.Client(app_id)
                    res = client.query(math)
                    answer = next(res.results).text
                    Say(answer)
                except:
                    Say("I can not calculate. It maybe your pronunciation mistake, or syntax problem.")
            math = Listen().lower()
        Say("Calculation mode deactivated")
    elif "information" in tag:
        Say("Information activated. To deactivate it, just say deactivate information")
        info = Listen().lower()
        while info != "deactivate information":
            if info != "deactivate information":
                try:
                    app_id = "6UXUHA-27VPL5W6QU"
                    client = wolframalpha.Client(app_id)
                    res = client.query(info)
                    ansinfo = next(res.results).text
                    Say(ansinfo)
                except:
                    Say("Sorry, I don't know")
            info = Listen().lower()
        Say("Information mode deactivated")
    # elif "meaning" in tag:
    #     word = str(query).replace("meaning of", "").replace("what is the ", "").replace("tell me the", "")
    #     meaning = PyDictionary.meaning(word)
    #     Say(meaning)

    elif "screenshot" in tag:
        Say("Tell me the name for this screenshot")
        name = Listen().lower()
        time.sleep(2)
        ss = pyautogui.screenshot()
        ss.save(f"{name}.png")
        Say("It has been saved in our main folder.")
    elif "set alarm" in tag:
        try:
            Say("Tell me the time to set the alarm. For example, set alarm at 4:30 pm")
            alarmTime = Listen()
            alarmTime = alarmTime.replace("set alarm at ", "")
            alarmTime = alarmTime.replace(".", "")
            alarmTime = alarmTime.upper()
            alarm.alarm(alarmTime)
            Say("Alarm has been set")

        except:
            Say("Sorry I failed to set the alarm")
