import dolphin_memory_engine as dolphin
import tkinter as tk
from tkinter import ttk
from os import path

bodyDict = {
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
}
gunDict = {
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
}
bombDict = {
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
}
podDict = {
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
}
legDict= {
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

with open("config.txt", "r") as f:
    config = f.read().split("!&*#^@%)")
clearText = config[0]
buildsPad = " " * int(config[1])
scoresPad = " " * int(config[2])
namesPad = " " * int(config[3])
dirname = "OBS Sources"

def loadToOBS():
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

    s = [parts[10] + "\n", parts[11] + "\n", parts[12] + "\n", parts[13] + "\n", parts[14] + "\n", buildsPad]
    with open(path.join(dirname, "green.txt"), "w") as f:
        f.writelines(s)

    s = [parts[15] + "\n", parts[16] + "\n", parts[17] + "\n", parts[18] + "\n", parts[19] + "\n", buildsPad]
    with open(path.join(dirname, "yellow.txt"), "w") as f:
        f.writelines(s)

    partsStatus.configure(text="Updated sources to builds")


def clearBuilds():
    with open(path.join(dirname, "red.txt"), "w") as f:
        f.write(clearText)

    with open(path.join(dirname, "blue.txt"), "w") as f:
        f.write(clearText)

    with open(path.join(dirname, "green.txt"), "w") as f:
        f.write(clearText + "\n" + buildsPad)

    with open(path.join(dirname, "yellow.txt"), "w") as f:
        f.write(clearText + "\n" + buildsPad)

    partsStatus.configure(text="Cleared sources")


def updateSB():
    with open(path.join(dirname, "p1name.txt"), "w") as f:
        f.write(p1name.get() + "\n" + namesPad)

    with open(path.join(dirname, "p1score.txt"), "w") as f:
        f.write(p1score.get() + "\n" + scoresPad)

    with open(path.join(dirname, "p2score.txt"), "w") as f:
        f.write(p2score.get() + "\n" + scoresPad)

    with open(path.join(dirname, "p2name.txt"), "w") as f:
        f.write(p2name.get() + "\n" + namesPad)
    sbStatus.configure(text="Scoreboard updated")


def incDecScore(component):
    if component == "p1plus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get() + "\n" + scoresPad)
    elif component == "p1minus1":
        curScore = p1score.get()
        p1score.delete(0, 'end')
        p1score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p1score.txt"), "w") as f:
            f.write(p1score.get() + "\n" + scoresPad)
    elif component == "p2plus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) + 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get() + "\n" + scoresPad)
    elif component == "p2minus1":
        curScore = p2score.get()
        p2score.delete(0, 'end')
        p2score.insert(0, int(curScore) - 1)
        with open(path.join(dirname, "p2score.txt"), "w") as f:
            f.write(p2score.get() + "\n" + scoresPad)


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


def updateConfig():
    try:
        global clearText
        global buildsPad
        global scoresPad
        global namesPad
        clearText = clearEntry.get(1.0, "end-1c")
        buildsPad = " " * int(buildsPadEntry.get())
        scoresPad = " " * int(scoresPadEntry.get())
        namesPad = " " * int(namesPadEntry.get())

        with open("config.txt", "w") as f:
            f.write(clearText + "!&*#^@%)" + str(len(buildsPad)) + "!&*#^@%)" + str(len(scoresPad)) + "!&*#^@%)" + str(len(namesPad)))
        configStatusLabel.config(text="")
    except ValueError:
        configStatusLabel.config(text="Make sure all pads are numbers")


window = tk.Tk()
window.title("OBS Overlay Manager")

## tabs
tabs = ttk.Notebook(window)
mainTab = ttk.Frame(tabs)
configTab = ttk.Frame(tabs)
tabs.add(mainTab, text="Main")
tabs.add(configTab, text="Config")
tabs.grid(row=0, column=0)

## parts components
loadPartsButton = ttk.Button(mainTab, text="Load to OBS", command=loadToOBS)
loadPartsButton.grid(row=1, column=1, columnspan=2, padx=10, pady=7)

clearPartsButton = ttk.Button(mainTab, text="Clear", command=clearBuilds)
clearPartsButton.grid(row=2, column=1, columnspan=2, padx=10, pady=7)

partsStatus = ttk.Label(mainTab)
partsStatus.grid(row=1, column=3, rowspan=2, columnspan=4)

## scoreboard components
p1label = ttk.Label(mainTab, text="P1:")
p1label.grid(row=3, column=0)
p1name = ttk.Entry(mainTab)
p1name.grid(row=4, column=0, columnspan=3, padx=7, pady=(0, 7))

p2label = ttk.Label(mainTab, text="P2:")
p2label.grid(row=3, column=5)
p2name = ttk.Entry(mainTab)
p2name.grid(row=4, column=5, columnspan=3, padx=7, pady=(0, 7))

p1score = ttk.Entry(mainTab, width=4)
p1score.grid(row=5, column=1)
p1score.insert(0, "0")

p1minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p1minus1"))
p1minus1.grid(row=5, column=0)
p1plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p1plus1"))
p1plus1.grid(row=5, column=2)

p2score = ttk.Entry(mainTab, width=4)
p2score.grid(row=5, column=6)
p2score.insert(0, "0")

p2minus1 = ttk.Button(mainTab, text="-1", width=3, command=lambda:incDecScore("p2minus1"))
p2minus1.grid(row=5, column=5)
p2plus1 = ttk.Button(mainTab, text="+1", width=3, command=lambda:incDecScore("p2plus1"))
p2plus1.grid(row=5, column=7)

switch = ttk.Button(mainTab, text="<->", width=4, command=switchSB)
switch.grid(row=4, column=4, rowspan=2)


updateSbButton = ttk.Button(mainTab, text="Update SB", command=updateSB)
updateSbButton.grid(row=6, column=1, columnspan=2, padx=10, pady=7)

sbStatus = ttk.Label(mainTab)
sbStatus.grid(row=6, column=3, columnspan=4)

## config
ceLabel = ttk.Label(configTab, text="Clear Text: ")
ceLabel.grid(row=0, column=0, pady=7, sticky='e')
clearEntry = tk.Text(configTab, width=16, height=3, font=("Calibri", 10))
clearEntry.grid(row=0, column=1, pady=7, sticky='w')
clearEntry.insert(1.0, config[0])

bpeLabel = ttk.Label(configTab, text="Builds Pad: ")
bpeLabel.grid(row=1, column=0, pady=7, sticky='e')
buildsPadEntry = ttk.Entry(configTab, width=12)
buildsPadEntry.grid(row=1, column=1, pady=7, sticky='w')
buildsPadEntry.insert(0, config[1])

speLabel = ttk.Label(configTab, text="Scores Pad: ")
speLabel.grid(row=2, column=0, pady=7, sticky='e')
scoresPadEntry = ttk.Entry(configTab, width=12)
scoresPadEntry.grid(row=2, column=1, pady=7, sticky='w')
scoresPadEntry.insert(0, config[2])

npeLabel = ttk.Label(configTab, text="Player Names Pad: ")
npeLabel.grid(row=3, column=0, padx=(50, 0), pady=7, sticky='e')
namesPadEntry = ttk.Entry(configTab, width=12)
namesPadEntry.grid(row=3, column=1, pady=7, sticky='w')
namesPadEntry.insert(0, config[3])

saveConfig = ttk.Button(configTab, text="Save", command=updateConfig)
saveConfig.grid(row=4, column=1, pady=7)

configStatusLabel = ttk.Label(configTab)
configStatusLabel.grid(row=5, column=0, columnspan=2, pady=7)

window.config(bg="#2f2f2f")
window.mainloop()