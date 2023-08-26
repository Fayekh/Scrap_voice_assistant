import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


Name = "Scrap"

from Listen import Listen
from Speak import Say
from Task import InputExecution
from Task import NonInputExecution
from Task import wishMe


def Main():

    sentence = Listen()
    result = str(sentence)

    if "bye" in sentence or "turn off yourself" in sentence or "goodbye" in sentence or "you can sleep" in sentence:
        Say("Good Bye...")
        exit()

    sentence = tokenize(sentence)

    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)
                elif "open camera" in reply:
                    NonInputExecution(reply)
                elif "close camera" in reply:
                    NonInputExecution(reply)
                elif "take photo" in reply:
                    NonInputExecution(reply)
                elif "move mouse up" in reply:
                    NonInputExecution(reply)
                elif "move mouse down" in reply:
                    NonInputExecution(reply)
                elif "move mouse right" in reply:
                    NonInputExecution(reply)
                elif "move mouse left" in reply:
                    NonInputExecution(reply)
                elif "move mouse top left" in reply:
                    NonInputExecution(reply)
                elif "move mouse top right" in reply:
                    NonInputExecution(reply)
                elif "move mouse bottom left" in reply:
                    NonInputExecution(reply)
                elif "move mouse bottom right" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "calculation" in reply:
                    InputExecution(reply, result)
                elif "day" in reply:
                    NonInputExecution(reply)
                elif "open notepad" in reply:
                    NonInputExecution(reply)
                elif "close notepad" in reply:
                    NonInputExecution(reply)
                elif "activate voice typing" in reply:
                    InputExecution(reply, result)
                elif "open youtube" in reply:
                    NonInputExecution(reply)
                elif "pause" in reply:
                    NonInputExecution(reply)
                elif "play" in reply:
                    NonInputExecution(reply)
                elif "exit full screen" in reply:
                    NonInputExecution(reply)
                elif "full screen" in reply:
                    NonInputExecution(reply)
                elif "restart video" in reply: 
                    NonInputExecution(reply)
                # elif "wikipedia" in reply:
                    # InputExecution(reply, result)
                elif "open google" in reply:
                    InputExecution(reply, result)
                elif"open chrome" in reply:
                    NonInputExecution(reply)
                elif "close chrome" in reply:
                    NonInputExecution(reply)
                elif "play music" in reply:
                    NonInputExecution(reply)
                elif "close music" in reply:
                    NonInputExecution(reply)
                elif "meaning" in reply:
                    InputExecution(reply, result)
                elif "information" in reply:
                    InputExecution(reply, result)
                elif "increase brightness" in reply:
                    NonInputExecution(reply)
                elif "decrease brightness" in reply:
                    NonInputExecution(reply)
                elif "volume up" in reply:
                    NonInputExecution(reply)
                elif "volume down" in reply:
                    NonInputExecution(reply)
                elif "press enter" in reply:
                    NonInputExecution(reply)
                elif "mute" in reply:
                    NonInputExecution(reply)
                elif "open word" in reply:
                    NonInputExecution(reply)
                elif "close word" in reply:
                    NonInputExecution(reply)
                elif "screenshot" in reply:
                    InputExecution(reply, result)
                elif "copy" in reply:
                    NonInputExecution(reply)
                elif "paste" in reply:
                    NonInputExecution(reply)
                elif "save" in reply:
                    NonInputExecution(reply)
                elif "mouse click" in reply:
                    NonInputExecution(reply)
                elif "mouse double click" in reply:
                    NonInputExecution(reply)
                elif "mouse right click" in reply:
                    NonInputExecution(reply)
                elif "shutdown" in reply:
                    NonInputExecution(reply)
                elif "restart computer" in reply:
                    NonInputExecution(reply)
                elif "sleep computer" in reply:
                    NonInputExecution(reply)
                elif "set alarm" in reply:
                    InputExecution(reply, result)
                elif "ip address" in reply:
                    NonInputExecution(reply)
                else:
                    Say(reply)


if __name__ == "__main__":
    wishMe()
    while True:
        Main()
