# Custom Robo Overlay Manager
This is a tool for managing overlays while streaming/recording Custom Robo: Battle Revolution. I designed this for OBS but it works fine for any recording software that allows text sources to read from a text file. The portion of this tool for loading builds works with both Vanilla CRBR and *Project Hive 3*, a patch made by the netplay community and used for the community's tournaments. This will be updated in future if new parts are added or parts are reordered.

## Set Up
If you'd rather follow a video, click [here](https://www.youtube.com/watch?v=UlpfOva9VVs). The setup information in this video is accurate, but keep in mind that some of the usage has changed as I've added and adjusted features.

1. Download the `crbr-overlay-manager.zip` file in releases. Unzip it, then put the unzipped folder in a location where you won't need to move it anytime soon.
2. Open OBS (or another recording software), then make 8 text sources, 4 for the builds, 2 for the players' names, and 2 for the players' current game scores. If you only care about managing builds and not scores, or vice versa, then you can just make the relevant text sources.
3. Set each text source to read from a file, then pick the text files in `crbr-overlay-manager/dist/OBS Sources`. `red.txt`, `blue.txt`, `green.txt`, & `yellow.txt` are for the robos of the corresponding colors, and `p1name.txt`, `p1score.txt`, `p2name.txt`, & `p2score.txt` are for the corresponding players' names and scores.

## Usage
First, run the `OBS Overlay Manager.exe` in the `dist` folder. This should open a window titled `OBS Overlay Manager`, which you can also pin to the taskbar.
- Open Dolphin, start up Custom Robo, and go to the P1+P1vsP2+P2 tag parts select screen. Click the `Load to OBS` button in the Overlay Manager window to load the currently selected parts into the OBS text sources for the builds, and the `Clear` button to clear those sources if you're still waiting for players to pick parts.
- Fill player names in the `P1:` and `P2:` input fields, put scores in the input fields below them, and click `Update SB` to update the OBS text sources for the scoreboard. You can also click the `-1` and `+1` buttons to quickly decrement and increment each player's score, and press the `<->` button to switch both players' scores and names.

![image](https://github.com/user-attachments/assets/625097ec-15b0-4275-b8b0-bd766e40b65f)

- In the `Config` tab, you can set what text gets put in the 4 build sources when the `Clear` button is pressed by filling the `Clear Text` input box, then clicking the `Save Clear Text` button.
- You can also set padding for the builds, scores, and player names text sources. Since text sources (at least in OBS) are always anchored to the left edge regardless of align, texts of various lengths will cause the text box to move around if the text isn't left aligned. Configuring the pads for the various sources will add the given number of spaces on a line below the actual text, which can help prevent the text sources from shifting. If you don't want to bother with this, you can leave all the pads at 0.
- With the tick boxes in the upper right section, you can enable auto loading and auto clearing parts. Enabling `Auto Load Parts` will automatically load both players' selected parts into the 4 robo text sources after both players hit START on part select. Enabling `Auto Clear Parts` will automatically clear all 4 robos to the clear text when entering part select. Keep in mind that enabling either of these options will remove the corresponding button from the `Main` tab.
- Select either `Vanilla` or `Project Hive 3` from the dropdown depending on which version you're currently playing.

![image](https://github.com/user-attachments/assets/f197d50d-2ab7-4d0e-a13a-92cf4535eae6)

## Acknowledgements
Thanks to my friend zensol for helping me figure out a good amount of the parts loading stuff. Thanks to aldelaro5 for making the amazing [Dolphin Memory Engine](https://github.com/aldelaro5/dolphin-memory-engine), thanks to Randovania for making a [Python library for Memory Engine](https://github.com/randovania/py-dolphin-memory-engine) which made my life considerably easier, and thanks to the numerous contributors to both of those projects. Thanks to the [tkinter](https://docs.python.org/3/library/tkinter.html) contributors for the powerful UI tools, and thanks to the [PyInstaller](https://pyinstaller.org/en/stable/) contributors for enabling me to package everything into an .exe. Finally, thanks to the CRBR netplay community for providing a place to play and talk about CR 20+ years after the game released, join the community on [discord](https://discord.gg/qPXvwdeT3V) if you also love Custom Robo.
