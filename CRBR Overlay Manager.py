import dolphin_memory_engine as dolphin
import tkinter as tk
from tkinter import ttk
from os import path
from configparser import ConfigParser
import shutil
from pathlib import Path
import pandas as pd
import datetime

vanillaParts = [
    {
        0: "Ray 01",
        1: "Splendor",
        2: "Glory",
        3: "Milky Way",
        4: "Earth",
        5: "Sol",
        6: "Metal Ape",
        7: "Metal Bear",
        8: "Metal Ox",
        9: "Swift",
        10: "Shrike",
        11: "Peregrine",
        12: "Javelin",
        13: "Glaive",
        14: "Halberd",
        15: "Criminal",
        16: "Buggy",
        17: "Juggler",
        18: "Defender",
        19: "Seeker",
        20: "Breaker",
        21: "Seal Head",
        22: "Dour Head",
        23: "Tank Head",
        24: "Rakansen",
        25: "Ruhiel",
        26: "Athena",
        27: "Ray Legend",
        28: "Ray Warrior",
        29: "Oil Can",
        30: "Rahu I",
        31: "Rahu II",
        32: "Rahu III",
        33: "Chickenheart"
    },
    {
        0: "Basic",
        1: "3-Way",
        2: "Gatling",
        3: "Vertical",
        4: "Sniper",
        5: "Stun",
        6: "Hornet",
        7: "Flame",
        8: "Dragon",
        9: "Splash",
        10: "Left Arc",
        11: "Right Arc",
        12: "Shotgun",
        13: "Rayfall",
        14: "Bubble",
        15: "Eagle",
        16: "V Laser",
        17: "Magnum",
        18: "Needle",
        19: "Starshot",
        20: "Glider",
        21: "Homing Star",
        22: "Trap",
        23: "Drill",
        24: "Titan",
        25: "Claw",
        26: "Knuckle",
        27: "Afterburner",
        28: "Blade",
        29: "Meteor Storm",
        30: "Twin Fang",
        31: "Gravity",
        32: "Phoenix",
        33: "Left Pulse",
        34: "Right Pulse",
        35: "Sword Storm",
        36: "Ion",
        37: "Flare",
        38: "Left 5-Way",
        39: "Right 5-Way",
        40: "Halo",
        41: "Wave Laser",
        42: "X Laser",
        43: "Crystal Strike",
        44: "Wyrm",
        45: "Raptor",
        46: "Waxing Arc",
        47: "Waning Arc",
        48: "Rahu I",
        49: "Rahu II",
        50: "Rahu III",
        51: "Can"
    },
    {
        0: "Standard",
        1: "Standard F",
        2: "Standard S",
        3: "Standard K",
        4: "Standard X",
        5: "Wave",
        6: "Straight G",
        7: "Straight S",
        8: "Straight T",
        9: "Left Flank H",
        10: "Right Flank H",
        11: "Left Wave",
        12: "Right Wave",
        13: "Burrow D",
        14: "Burrow P",
        15: "Freeze",
        16: "Tomahawk B",
        17: "Tomahawk G",
        18: "Gemini B",
        19: "Gemini P",
        20: "Submarine D",
        21: "Submarine P",
        22: "Submarine K",
        23: "Crescent P",
        24: "Crescent C",
        25: "Crescent K",
        26: "Dual",
        27: "Dual C",
        28: "Acrobat",
        29: "Delta",
        30: "Wall",
        31: "Smash",
        32: "Double Mine",
        33: "Geo Trap",
        34: "Titan",
        35: "Treble",
        36: "Wyvern",
        37: "Waxing Arc",
        38: "Waning Arc",
        39: "Grand Cross",
        40: "Can"
    },
    {
        0: "Standard",
        1: "Standard F",
        2: "Seeker F",
        3: "Seeker G",
        4: "Speed D",
        5: "Speed P",
        6: "Cockroach G",
        7: "Cockroach H",
        8: "Dolphin",
        9: "Dolphin G",
        10: "Spider",
        11: "Spider G",
        12: "Sky Freeze",
        13: "Ground Freeze",
        14: "Feint F",
        15: "Feint G",
        16: "Float F",
        17: "Jumping B",
        18: "Jumping G",
        19: "Diving",
        20: "Wave",
        21: "Satellite",
        22: "Satellite H",
        23: "Beast F",
        24: "Trio H",
        25: "Wall",
        26: "Reflection",
        27: "Caboose C",
        28: "Caboose T",
        29: "Caboose X",
        30: "Twin Flank F",
        31: "Twin Flank G",
        32: "Umbrella",
        33: "Throwing D",
        34: "Throwing P",
        35: "Double Wave",
        36: "Titan",
        37: "Cheetah",
        38: "Wolf Spider",
        39: "Orca",
        40: "Penumbra I",
        41: "Penumbra II",
        42: "Penumbra III",
        43: "Can"
    },
    {
        0: "Standard",
        1: "High Jump",
        2: "Ground",
        3: "Formula",
        4: "Stabilizer",
        5: "Short Thrust",
        6: "Long Thrust",
        7: "Quick Jump",
        8: "Feather",
        9: "Wide Jump",
        10: "Booster",
        11: "Swallow",
        12: "Raven",
        13: "Eclipse",
        14: "Ultimate",
        15: "Can"
    }
]

ph3Parts = [
    {
        0: "Ray 01",
        1: "Splendor",
        2: "Glory",
        3: "Milky Way",
        4: "Earth",
        5: "Sol",
        6: "Metal Ape",
        7: "Metal Bear",
        8: "Metal Ox",
        9: "Swift",
        10: "Shrike",
        11: "Peregrine",
        12: "Javelin",
        13: "Glaive",
        14: "Halberd",
        15: "Criminal",
        16: "Buggy",
        17: "Juggler",
        18: "Defender",
        19: "Seeker",
        20: "Breaker",
        21: "Seal Head",
        22: "Dour Head",
        23: "Tank Head",
        24: "Chickenheart",
        25: "Rahubeast",
        26: "Ruhiel",
        27: "Lancer",
        28: "Gladiator",
        29: "Ray Soldier",
        30: "Athena",
        31: "Rebecca",
        32: "May",
        33: "Lumen",
        34: "Pepper",
        35: "Nybble",
        36: "Vulcan",
        37: "Spitfire",
        38: "Albatross"
    },
    {
        0: "Basic",
        1: "Needle",
        2: "Sniper",
        3: "Gatling",
        4: "Ion",
        5: "V Laser",
        6: "Dragon",
        7: "Hydra",
        8: "Bubble",
        9: "Splash",
        10: "Stun",
        11: "Shotgun",
        12: "Magnum",
        13: "Drill",
        14: "Knuckle",
        15: "Quickshot",
        16: "Surge",
        17: "Flame",
        18: "Hornet",
        19: "Vertical",
        20: "Buster",
        21: "Meteor Storm",
        22: "Left Pulse",
        23: "Right Pulse",
        24: "Twin Fang",
        25: "Flare",
        26: "Rahu I",
        27: "Slicer",
        28: "Gravity",
        29: "3-Way",
        30: "Left Arc",
        31: "Right Arc",
        32: "Starshot",
        33: "Homing Star",
        34: "Glider",
        35: "Halo",
        36: "Afterburner",
        37: "Rayfall",
        38: "Eagle",
        39: "Trap",
        40: "Sword Storm",
        41: "Vulture",
        42: "Pursuit",
        43: "Titan",
        44: "Left 5-Way",
        45: "Right 5-Way",
        46: "Claw",
        47: "Blade",
        48: "Phoenix"
    },
    {
        0: "Standard R",
        1: "Standard F",
        2: "Standard S",
        3: "Standard K",
        4: "Standard X",
        5: "Straight R",
        6: "Straight G",
        7: "Straight S",
        8: "Straight T",
        9: "Left Flank F",
        10: "Right Flank F",
        11: "Left Flank H",
        12: "Right Flank H",
        13: "Left Flank X",
        14: "Right Flank X",
        15: "Burrow D",
        16: "Burrow P",
        17: "Tomahawk R",
        18: "Tomahawk B",
        19: "Tomahawk G",
        20: "Tomahawk S",
        21: "Gemini D",
        22: "Gemini P",
        23: "Dual R",
        24: "Dual D",
        25: "Dual C",
        26: "Submarine D",
        27: "Submarine P",
        28: "Submarine K",
        29: "Submarine X",
        30: "Crescent R",
        31: "Crescent P",
        32: "Crescent C",
        33: "Crescent K",
        34: "Freeze",
        35: "Wave",
        36: "Left Wave",
        37: "Right Wave",
        38: "Acrobat",
        39: "Delta",
        40: "Wall",
        41: "Smash",
        42: "Double Mine",
        43: "Geo Trap",
        44: "Titan",
        45: "Solar Pillar",
        46: "Rapid",
        47: "Grand Cross",
        48: "Cluster",
        49: "Drake R",
        50: "Drake G",
        51: "Drake X",
        52: "Heavy R",
        53: "Heavy D",
        54: "Heavy H",
        55: "Heavy K"
    },
    {
        0: "Standard R",
        1: "Standard D",
        2: "Twin Flank F",
        3: "Twin Flank G",
        4: "Speed R",
        5: "Speed D",
        6: "Speed P",
        7: "Cockroach G",
        8: "Cockroach H",
        9: "Dolphin R",
        10: "Dolphin G",
        11: "Dolphin X",
        12: "Jumping B",
        13: "Jumping G",
        14: "Caboose C",
        15: "Caboose T",
        16: "Caboose X",
        17: "Wave",
        18: "Double Wave",
        19: "Wall",
        20: "Umbrella",
        21: "Trio F",
        22: "Trio H",
        23: "Titan",
        24: "Throwing D",
        25: "Throwing P",
        26: "Reflection",
        27: "Float F",
        28: "Feint F",
        29: "Feint G",
        30: "Seeker R",
        31: "Seeker F",
        32: "Seeker G",
        33: "Diving",
        34: "Spider R",
        35: "Spider H",
        36: "Spider G",
        37: "Sky Freeze",
        38: "Ground Freeze",
        39: "Satellite",
        40: "Satellite H",
        41: "Beast F"
    },
    {
        0: "Standard",
        1: "Formula",
        2: "Stabilizer",
        3: "Precision",
        4: "Wide Jump",
        5: "Aerial",
        6: "Eclipse",
        7: "Ultimate",
        8: "High Jump",
        9: "Ground",
        10: "Quick Jump",
        11: "Feather",
        12: "Short Thrust",
        13: "Long Thrust",
        14: "Swallow",
        15: "Plus One",
        16: "Booster",
        17: "Overhaul",
        18: "Raven",
        19: "Prowler"
    }
]

global configs
configs = ConfigParser()
configs.read("config.ini")
dirname = "OBS Sources"
pImgPath = "Player Images"

def loadClearLoop():
    state = configs.get("status", "state")
    dolphin.hook()
    if configs.getboolean("configurations", "autoload") and dolphin.is_hooked():
        if int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) != 0 and state != "loaded": # robo bytes loaded
            loadParts()
    if configs.getboolean("configurations", "autoclear") and dolphin.is_hooked():
        if int.from_bytes(dolphin.read_bytes(0x8024FCF8, 2)) == 0 and state != "cleared": # robo bytes unloaded
            clearParts()

    if configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear"):
        window.after(500, loadClearLoop)


def loadParts():
    dolphin.hook()

    byteList = [
        0x8040bab7, 0x8040bab9, 0x8040babb, 0x8040babd, 0x8040babf,
        0x8041044b, 0x8041044d, 0x8041044f, 0x80410451, 0x80410453,
        0x80414ddf, 0x80414de1, 0x80414de3, 0x80414de5, 0x80414de7,
        0x80419773, 0x80419775, 0x80419777, 0x80419779, 0x8041977b
    ]
    parts = []

    if dolphin.is_hooked():
        
        for byte in byteList:
            value = dolphin.read_byte(byte)
            match configs.get("configurations", "version"):
                case "Vanilla":
                    bodyDict = vanillaParts[0]
                    gunDict = vanillaParts[1]
                    bombDict = vanillaParts[2]
                    podDict = vanillaParts[3]
                    legDict = vanillaParts[4]
                case "Project Hive 3":
                    bodyDict = ph3Parts[0]
                    gunDict = ph3Parts[1]
                    bombDict = ph3Parts[2]
                    podDict = ph3Parts[3]
                    legDict = ph3Parts[4]

            if byte in [0x8040bab7, 0x8041044b, 0x80414ddf, 0x80419773]:
                part = bodyDict.get(value)
            elif byte in [0x8040bab9, 0x8041044d, 0x80414de1, 0x80419775]:
                part = gunDict.get(value)
            elif byte in [0x8040babb, 0x8041044f, 0x80414de3, 0x80419777]:
                part = bombDict.get(value)
            elif byte in [0x8040babd, 0x80410451, 0x80414de5, 0x80419779]:
                part = podDict.get(value)
            elif byte in [0x8040babf, 0x80410453, 0x80414de7, 0x8041977b]:
                part = legDict.get(value)
            parts.append(part)

        s = [parts[0] + "\n", parts[1] + "\n", parts[2] + "\n", parts[3] + "\n", parts[4]]
        with open(path.join(dirname, "red.txt"), "w") as f:
            f.writelines(s)

        s = [parts[5] + "\n", parts[6] + "\n", parts[7] + "\n", parts[8] + "\n", parts[9]]
        with open(path.join(dirname, "blue.txt"), "w") as f:
            f.writelines(s)

        s = [parts[10] + "\n", parts[11] + "\n", parts[12] + "\n", parts[13] + "\n", parts[14] + "\n", " " * int(configs.get("configurations", "buildspad"))]
        with open(path.join(dirname, "green.txt"), "w") as f:
            f.writelines(s)

        s = [parts[15] + "\n", parts[16] + "\n", parts[17] + "\n", parts[18] + "\n", parts[19] + "\n", " " * int(configs.get("configurations", "buildspad"))]
        with open(path.join(dirname, "yellow.txt"), "w") as f:
            f.writelines(s)

        currentStatus = statusQueue.cget("text")
        if "Loaded parts to sources" not in currentStatus:
            addStatusText("Loaded parts to sources")

        configs.set("status", "state", "loaded")
    
        with open("config.ini", "w") as configFile:
            configs.write(configFile)


def clearParts():
    with open(path.join(dirname, "red.txt"), "r") as f:
        if f.read() != configs.get("configurations", "cleartext"):

            with open(path.join(dirname, "red.txt"), "w") as f:
                f.write(configs.get("configurations", "cleartext"))

            with open(path.join(dirname, "blue.txt"), "w") as f:
                f.write(configs.get("configurations", "cleartext"))

            with open(path.join(dirname, "green.txt"), "w") as f:
                f.write(configs.get("configurations", "cleartext") + "\n" + " " * int(configs.get("configurations", "buildspad")))

            with open(path.join(dirname, "yellow.txt"), "w") as f:
                f.write(configs.get("configurations", "cleartext") + "\n" + " " * int(configs.get("configurations", "buildspad")))

            currentStatus = statusQueue.cget("text")
            if "Cleared parts from sources" not in currentStatus:
                addStatusText("Cleared parts from sources")

            configs.set("status", "state", "cleared")
    
            with open("config.ini", "w") as configFile:
                configs.write(configFile)


def updateSB():
    with open(path.join(dirname, "p1name.txt"), "w") as f:
        f.write(p1name.get() + "\n" + " " * int(configs.get("configurations", "namespad")))
        p1imagePath = path.join(pImgPath, p1name.get() + " - p1.png")
        p1imageFile = Path(p1imagePath)
        if p1imageFile.is_file():
            shutil.copy(p1imagePath, path.join(pImgPath, "p1.png"))
        else: 
            shutil.copy(path.join(pImgPath, "p1unknown.png"), path.join(pImgPath, "p1.png"))

    with open(path.join(dirname, "p1score.txt"), "w") as f:
        f.write(p1score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))

    with open(path.join(dirname, "p2name.txt"), "w") as f:
        f.write(p2name.get() + "\n" + " " * int(configs.get("configurations", "namespad")))
        p2imagePath = path.join(pImgPath, p2name.get() + " - p2.png")
        p2imageFile = Path(p2imagePath)
        if p2imageFile.is_file():
            shutil.copy(p2imagePath, path.join(pImgPath, "p2.png"))
        else: 
            shutil.copy(path.join(pImgPath, "p2unknown.png"), path.join(pImgPath, "p2.png"))
        
    with open(path.join(dirname, "p2score.txt"), "w") as f:
        f.write(p2score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))

    addStatusText("Updated scoreboard")


def incDecScore(component):
    if component == "p1plus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))
    elif component == "p1minus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))
    elif component == "p2plus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))
    elif component == "p2minus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get() + "\n" + " " * int(configs.get("configurations", "scorespad")))


def switchSB():
    temp = p1name.get()
    p1name.delete(0, 'end')
    p1name.insert(0, p2name.get())
    p2name.delete(0, 'end')
    p2name.insert(0, temp)
    temp = p1score.get()
    p1score.delete(0, 'end')
    p1score.insert(0, p2score.get())
    p2score.delete(0, 'end')
    p2score.insert(0, temp)
    updateSB()


def updateClearText():
    #read file, compare to clearText, if same then update robo files
    updateRobos = False
    clearText = clearEntry.get(1.0, "end-1c")
    with open(path.join(dirname, "red.txt"), "r") as f:
        if (f.read() == configs.get("configurations", "cleartext")):
            updateRobos = True

    configs.set("configurations", "cleartext", clearText)
    
    with open("config.ini", "w") as configFile:
        configs.write(configFile)

    if updateRobos:
        with open(path.join(dirname, "red.txt"), "w") as f:
            f.write(clearText)
        with open(path.join(dirname, "blue.txt"), "w") as f:
            f.write(clearText)
        with open(path.join(dirname, "green.txt"), "w") as f:
            f.write(clearText + "\n" + " " * int(configs.get("configurations", "buildspad")))
        with open(path.join(dirname, "yellow.txt"), "w") as f:
            f.write(clearText + "\n" + " " * int(configs.get("configurations", "buildspad")))


def show(b):
    match b.config("text")[-1]:
        case "Load Parts":
            b.grid(row=1, column=0, columnspan=2)
        case "Clear Parts":
            b.grid(row=1, column=2, columnspan=3)


def hide(b):
    b.grid_forget()


def checkTick(tickVar, tickBox, partsButton):
    if (tickVar.get()):
        s = "true"
        hide(partsButton)
        if not (configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear")):
           window.after(500, loadClearLoop)
    else:
        s = "false"
        show(partsButton)
    match tickBox.config("text")[-1]:
        case "Auto Load Parts":
            configs.set("configurations", "autoload", s)
        case "Auto Clear Parts":
            configs.set("configurations", "autoclear", s)
    with open("config.ini", "w") as configFile:
        configs.write(configFile)


def updatePad(box, pad):
    match pad:
        case "builds":
            configs.set("configurations", "buildspad", box.get())

            with open(path.join(dirname, "green.txt"), "r") as f:
                greenLines = f.readlines()

            if (len(greenLines) > 0):
                greenLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "green.txt"), "w") as f:
                    f.writelines(greenLines)

            with open(path.join(dirname, "yellow.txt"), "r") as f:
                yellowLines = f.readlines()

            if (len(yellowLines) > 0):
                yellowLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "yellow.txt"), "w") as f:
                    f.writelines(yellowLines)


        case "scores":
            configs.set("configurations", "scorespad", box.get())

            with open(path.join(dirname, "p1score.txt"), "r") as f:
                p1ScoreLines = f.readlines()

            if (len(p1ScoreLines) > 0):
                p1ScoreLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "p1score.txt"), "w") as f:
                    f.writelines(p1ScoreLines)
                
            with open(path.join(dirname, "p2score.txt"), "r") as f:
                p2ScoreLines = f.readlines()

            if (len(p2ScoreLines) > 0):
                p2ScoreLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "p2score.txt"), "w") as f:
                    f.writelines(p2ScoreLines)

        case "names":
            configs.set("configurations", "namespad", box.get())

            with open(path.join(dirname, "p1name.txt"), "r") as f:
                p1NameLines = f.readlines()

            if (len(p1NameLines) > 0):
                p1NameLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "p1name.txt"), "w") as f:
                    f.writelines(p1NameLines)
                
            with open(path.join(dirname, "p2name.txt"), "r") as f:
                p2NameLines = f.readlines()

            if (len(p2NameLines) > 0):
                p2NameLines[-1] = " " * int(box.get())
                with open(path.join(dirname, "p2name.txt"), "w") as f:
                    f.writelines(p2NameLines)

    with open("config.ini", "w") as configFile:
        configs.write(configFile)


def setVersion(comboBox):
    configs.set("configurations", "version", comboBox.get())
    with open("config.ini", "w") as configFile:
        configs.write(configFile)


def addStatusText(newStatus):
    currentStatus = statusQueue.cget("text").split("\n")
    currentStatus.append(newStatus)
    statusQueue.configure(text="\n".join(currentStatus))
    window.after(3000, lambda:popStatusQueue(newStatus))


def popStatusQueue(text):
    currentStatus = statusQueue.cget("text").split("\n")
    currentStatus.remove(text)
    statusQueue.configure(text="\n".join(currentStatus))


def updatePlayerNameList(playerNames, p1name, p2name):
    playerNameString = playerNames.get(1.0, "end-1c")
    playerNameList = playerNameString.split("\n")
    playerNameList = sorted(playerNameList, key=str.casefold)
    for i in range(int(configs.get("playernames", "numplayers"))):
        configs.remove_option("playernames", "player" + str(i))
    configs.set("playernames", "numplayers", str(len(playerNameList)))
    for i in range(len(playerNameList)):
        configs.set("playernames", "player" + str(i), playerNameList[i])
    with open("config.ini", "w") as configFile:
        configs.write(configFile)
    playerNameString = "\n".join(playerNameList)
    playerNames.delete(1.0, "end-1c")
    playerNames.insert(1.0, playerNameString)
    p1name["values"] = playerNameList
    p2name["values"] = playerNameList


def updateTourneyInfo(tourneyName, tourneyRound):
    with open(path.join(dirname, "tourney.txt"), "w") as f:
        f.write(tourneyName.get())
    with open(path.join(dirname, "round.txt"), "w") as f:
        f.write(tourneyRound.get())
    addStatusText("Updated tourney info")


def saveBuilds(p1name, p2name, tourneyName):
    redParts = []
    blueParts = []
    greenParts = []
    yellowParts = []
    with open(path.join(dirname, "red.txt"), "r") as f:
        redParts = f.readlines()
    with open(path.join(dirname, "blue.txt"), "r") as f:
        blueParts = f.readlines()
    with open(path.join(dirname, "green.txt"), "r") as f:
        greenParts = f.readlines()[:-1]
    with open(path.join(dirname, "yellow.txt"), "r") as f:
        yellowParts = f.readlines()[:-1]
    for parts in redParts, blueParts, greenParts, yellowParts:
        for i in range(len(parts)):
            parts[i] = parts[i].replace("\n", "")
    filename = "builds.xlsx"
    curSheetname = tourneyName.get() + " " + str(datetime.date.today())
    df = pd.DataFrame([[p1name.get()] + redParts + blueParts, [p2name.get()] + greenParts + yellowParts], columns=["Player", "Robo1", "Gun1", "Bomb1", "Pod1", "Legs1", "Robo2", "Gun2", "Bomb2", "Pod2", "Legs2"])
    if Path(filename).is_file():
        xl = pd.ExcelFile(filename)
        existingDfs = {sheet_name: xl.parse(sheet_name).drop(columns="Unnamed: 0") for sheet_name in xl.sheet_names}
        with pd.ExcelWriter(filename) as writer:
            for sheetname in existingDfs:
                existingDf = existingDfs[sheetname]
                if sheetname == curSheetname:
                    existingDf = existingDf._append(df)
                existingDf.to_excel(writer, sheet_name=sheetname)
            if curSheetname not in existingDfs:
                df.to_excel(writer, sheet_name=curSheetname)
    else:
        df.to_excel(filename, sheet_name=curSheetname)
    addStatusText("Saved builds to '" + filename + "'")



window = tk.Tk()
window.title("CRBR Overlay Manager")
window.iconbitmap(path.join("..", "assets", "crom.ico"))

### tabs
tabs = ttk.Notebook(window)
mainTab = ttk.Frame(tabs)
configTab = ttk.Frame(tabs)
tabs.add(mainTab, text="Main")
tabs.add(configTab, text="Config")
tabs.grid(row=0, column=0)

### main tab
## parts components
loadPartsButton = ttk.Button(mainTab, text="Load Parts", command=loadParts)
if not configs.getboolean("configurations", "autoload"):
    loadPartsButton.grid(row=1, column=0, columnspan=2)

clearPartsButton = ttk.Button(mainTab, text="Clear Parts", command=clearParts)
if not configs.getboolean("configurations", "autoclear"):
    clearPartsButton.grid(row=1, column=2, columnspan=3)

savePartsButton = ttk.Button(mainTab, text="Save Parts", command=lambda:saveBuilds(p1name, p2name, tourneyName))
savePartsButton.grid(row=0, column=5, columnspan=2)

## scoreboard components
playerNameList = []
for i in range(int(configs.get("playernames", "numplayers"))):
    playerNameList.append(configs.get("playernames", "player" + str(i)))
playerNameList = sorted(playerNameList, key=str.casefold)
p1label = ttk.Label(mainTab, text="P1:")
p1label.grid(row=3, column=0)
p1nameVar = tk.StringVar()
p1name = ttk.Combobox(mainTab, width=16, textvariable=p1nameVar)
p1name.grid(row=4, column=0, columnspan=3, padx=7)
p1name["values"] = playerNameList

p2label = ttk.Label(mainTab, text="P2:")
p2label.grid(row=3, column=4)
p2nameVar = tk.StringVar()
p2name = ttk.Combobox(mainTab, width=16, textvariable=p2nameVar)
p2name.grid(row=4, column=4, columnspan=3, padx=7)
p2name["values"] = playerNameList

p1score = ttk.Entry(mainTab, width=4)
p1score.grid(row=5, column=1)
p1score.insert(0, "0")

p1minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p1minus1"))
p1minus1.grid(row=5, column=0)
p1plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p1plus1"))
p1plus1.grid(row=5, column=2)

p2score = ttk.Entry(mainTab, width=4)
p2score.grid(row=5, column=5)
p2score.insert(0, "0")

p2minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p2minus1"))
p2minus1.grid(row=5, column=4)
p2plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p2plus1"))
p2plus1.grid(row=5, column=6)

switch = ttk.Button(mainTab, text="<->", width=4, command=switchSB)
switch.grid(row=4, rowspan=2, column=3)

updateSbButton = ttk.Button(mainTab, text="Update SB", command=updateSB)
updateSbButton.grid(row=0, column=0, columnspan=2, padx=10, pady=7)

## tourney info
tnLabel = ttk.Label(mainTab, text="Event:")
tnLabel.grid(row=7, column=0)
tourneyName = ttk.Entry(mainTab)
tourneyName.grid(row=8, column=0, columnspan=3)
trLabel = ttk.Label(mainTab, text="Round:")
trLabel.grid(row=7, column=4)
tourneyRound = ttk.Entry(mainTab)
tourneyRound.grid(row=8, column=4, columnspan=3)
tourneyInfoButton = ttk.Button(mainTab, text="Update Tourney", command=lambda:updateTourneyInfo(tourneyName, tourneyRound))
tourneyInfoButton.grid(row=0, column=2, columnspan=3)


## status queue
statusQueue = ttk.Label(mainTab, justify="center")
statusQueue.grid(row=9, column=0, columnspan=7)

### config
## clear text
ceLabel = ttk.Label(configTab, text="Clear Text:")
ceLabel.grid(row=0, column=0)
clearEntry = tk.Text(configTab, width=16, height=4, font=("Arial", 9))
clearEntry.grid(row=1, rowspan=2, column=0, columnspan=2)
clearEntry.insert(1.0, configs.get("configurations", "cleartext"))

saveClearText = ttk.Button(configTab, text="Save", width=5, command=updateClearText)
saveClearText.grid(row=0, column=1)

## pads
buildsPadLabel = ttk.Label(configTab, text="Builds Pad  ")
buildsPadLabel.grid(row=3, column=0, pady=7, sticky='e')
buildsPadBox = ttk.Spinbox(configTab, from_=0, to=100, width=12, command=lambda:updatePad(buildsPadBox, "builds"))
buildsPadBox.grid(row=3, column=1, pady=7, sticky='w')
buildsPadBox.insert(0, configs.get("configurations", "buildspad"))

scoresPadLabel = ttk.Label(configTab, text="Scores Pad  ")
scoresPadLabel.grid(row=4, column=0, pady=7, sticky='e')
scoresPadBox = ttk.Spinbox(configTab, from_=0, to=100, width=12, command=lambda:updatePad(scoresPadBox, "scores"))
scoresPadBox.grid(row=4, column=1, pady=7, sticky='w')
scoresPadBox.insert(0, configs.get("configurations", "scorespad"))

namesPadLabel = ttk.Label(configTab, text="Names Pad  ")
namesPadLabel.grid(row=5, column=0, padx=(10, 0), pady=7, sticky='e')
namesPadBox = ttk.Spinbox(configTab, from_=0, to=100, width=12, command=lambda:updatePad(namesPadBox, "names"))
namesPadBox.grid(row=5, column=1, pady=7, sticky='w')
namesPadBox.insert(0, configs.get("configurations", "namespad"))

## autoload
loadTickVar = tk.BooleanVar()
loadTickVar.set(configs.getboolean("configurations", "autoload"))
loadTickBox = ttk.Checkbutton(configTab, text="Auto Load Parts", variable=loadTickVar, command=lambda:checkTick(loadTickVar, loadTickBox, loadPartsButton))
loadTickBox.grid(row=3, column=2, columnspan=2, padx=10, pady=7)
clearTickVar = tk.BooleanVar()
clearTickVar.set(configs.getboolean("configurations", "autoclear"))
clearTickBox = ttk.Checkbutton(configTab, text="Auto Clear Parts", variable=clearTickVar, command=lambda:checkTick(clearTickVar, clearTickBox, clearPartsButton))
clearTickBox.grid(row=4, column=2, columnspan=2, padx=10, pady=7)

## patch combobox
patchVar = tk.StringVar()
patchComboBox = ttk.Combobox(configTab, width=15, textvariable=patchVar, state="readonly")
patchComboBox.grid(row=5, column=2, columnspan=2, padx=10, pady=7)
patchComboBox["values"] = ("Vanilla", "Project Hive 3")
patchComboBox.bind("<<ComboboxSelected>>", lambda _:setVersion(patchComboBox))
patchComboBox.set(configs.get("configurations", "version"))

## player names
pnLabel = ttk.Label(configTab, text="Player Names:")
pnLabel.grid(row=0, column=2)
playerNames = tk.Text(configTab, width=16, height=4, font=("Arial", 9))
playerNames.grid(row=1, rowspan=2, column=2, columnspan=2)
playerNameList = []
for i in range(int(configs.get("playernames", "numplayers"))):
    playerNameList.append(configs.get("playernames", "player" + str(i)))
playerNameString = "\n".join(playerNameList)
playerNames.insert(1.0, playerNameString)
savePlayerNames = ttk.Button(configTab, text="Save", width=5, command=lambda:updatePlayerNameList(playerNames, p1name, p2name))
savePlayerNames.grid(row=0, column=3)

if configs.getboolean("configurations", "autoload") or configs.getboolean("configurations", "autoclear"):
    loadClearLoop()
window.mainloop()