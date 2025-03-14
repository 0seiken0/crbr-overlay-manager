# Custom Robo Overlay Manager
This is a tool for managing overlays while streaming Custom Robo: Battle Revolution. I designed this for OBS but it should work fine for any software that allows text sources. The portion of this tool for loading builds is currently set up for the *Project Hive 3* patch of CR since that's what the netplay community currently runs tournaments on, and it will be updated in future if new parts are added.

## Set Up
If you'd rather follow a video, click [here](https://www.youtube.com/watch?v=UlpfOva9VVs).

1. Download the `crbr-overlay-manager.zip` file in releases. Unzip it, then put the unzipped folder in a location where you won't need to move it anytime soon.
2. Open OBS, then make 8 text sources, 4 for the builds, 2 for the players' names, and 2 for the players' current game scores. If you only care about managing builds and not scores, or vice versa, then you can just make the relevant text sources.
3. Set each text source to read from a file, then pick the text files in `dist/OBS Sources`. `red.txt`, `blue.txt`, `green.txt`, & `yellow.txt` are for the robos of the corresponding colors, and `p1name.txt`, `p1score.txt`, `p2name.txt`, & `p2score.txt` are for the corresponding player's name and score.

## Usage
First, run the `OBS Overlay Manager.exe` in the `dist` folder. This should open a window titled `OBS Overlay Manager`, which you can also pin to the taskbar.
- Open Dolphin and go to the P1+P1vsP2+P2 tag parts select screen. Click the `Load to OBS` button in the Overlay Manager window to load the currently selected parts into the OBS text sources for the builds, and the `Clear` button to clear those sources if you're still waiting for players to pick parts.
- Fill player names in the `P1:` and `P2:` input fields, put scores in the input fields below them, and click `Update SB` to update the OBS text sources for the scoreboard. You can also click the `-1` and `+1` buttons to quickly decrement and increment each player's score, and press the `<->` button to switch both player's scores and names.
- In the `Config` tab, you can set what text gets put in the 4 build sources when the `Clear` button is pressed. You can also set padding for the builds, scores, and names text sources. This will put a number of spaces on a line below the actual text to prevent the text sources from moving around with text of varying lengths. If you don't want to bother with this, you can leave all the pads at 0. After you set the pads, click `Save` to record your settings.

![image](https://github.com/user-attachments/assets/71b902d2-8ed8-47f4-b144-821a833369c8)
![image](https://github.com/user-attachments/assets/976564c9-75aa-40de-adb8-4e73b641cb39)



## Acknowledgements
Thanks to my friend zensol for helping me figure out a good amount of the parts loading stuff. Thanks to aldelaro5 for making the amazing [Dolphin Memory Engine](https://github.com/aldelaro5/dolphin-memory-engine), thanks to Randovania for making a [Python library for Memory Engine](https://github.com/randovania/py-dolphin-memory-engine) which made my life considerably easier, and thanks to the numerous contributors to both of those projects. Thanks to the CRBR netplay community for providing a place to play and talk about CR 20+ years after the game released, join the community on [discord](https://discord.gg/qPXvwdeT3V) if you also love Custom Robo.
