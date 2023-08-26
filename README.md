# Scrap
Scrap, a simple voice assistant for Windows developed using Python. 

Make sure the internet and microphone are connected and working properly else the program will throw errors. 

While using the program for the first time, make sure to run the Train.py first. It will TrainData.pth. Do not delete it. Then run Scrap.py and it will start working.

You can add your own custom commands using intents.json and Task.py

Make sure to delete the TrainData.pth and run the Train.py again after making any changes.

#Adding new commands like opening an application 
To open an application add this code in Task.py :
 
    elif "open chrome" in query:
         gcpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
         os.startfile(gcpath)

  Here,
  "open chrome" part is the command you want to use for opening the application
  "gcpath" is the application's location in your device, you can use any variable name you want.

  After adding this in Task.py, also update it in intents.json and run the Train.py (delete the old TrainData.pth)

