# Custom Robo Overlay Manager

This is a tool for managing overlays while streaming/recording Custom Robo: Battle Revolution being played through Dolphin. I designed this for OBS but it works fine with any recording software that allows text sources to read from a text file. The portion of this tool for loading parts to the screen works with both Vanilla CRBR & *Project Hive 3*, a patch made by the CR Netplay community and used for the community's tournaments. This will be updated in future if new parts are added or parts are reordered.

This was designed in Windows. It might work for Mac & Linux but I honestly have no earthly idea since I don't have Mac or Linux machines.

## Basic Set Up & Usage

If you'd rather follow a video, click [here](https://www.youtube.com/watch?v=UlpfOva9VVs). The setup information in this video is largely accurate, but keep in mind that some of the usage has changed as I've added and adjusted features.

1. Download the `crbr-overlay-manager.zip` file in releases, then extract the file. I recommend you put the extracted folder somewhere you won't need to move it, as you'll need to reconfigure the text sources you make in the next step if the folder's location changes.
2. Open your recording software. Make text sources for the info you want to manage with this tool, and have those text sources read from the corresponding file in `crbr-overlay-manager/dist/OBS Sources`. Refer to the table below to see which files correspond to what information. The asterisked files are filled by text entry fields, so you can use them for other purposes if you'd like.

| Filename          | Information           |
| ----------------- | --------------------- |
| `red.txt`         | Red robo's parts      |
| `blue.txt`        | Blue robo's parts     |
| `green.txt`       | Green robo's parts    |
| `yellow.txt`      | Yellow robo's parts   |
| `p1name.txt`*     | Player 1's name       |
| `p1score.txt`     | Player 1's score      |
| `p2name.txt`*     | Player 2's name       |
| `p2score.txt`     | Player 2's score      |
| `tourney.txt`*    | Tourney/event name    |
| `round.txt`*      | Current tourney round |

3. Open the CRBR Overlay Manager by navigating to `crbr-overlay-manager/dist` and double clicking the `CRBR Overlay Manager.exe`. This will open a window titled "CRBR Overlay Manager" and will display the `Main` tab. You can pin the program in the taskbar for easy access on subsequent uses.

<img width="310" height="252" alt="Screenshot 2025-10-16 163400" src="https://github.com/user-attachments/assets/26602f93-5c64-4fd6-ba9f-6faa0c48e04b" />

4. To load parts, run CRBR through Dolphin and navigate to the P1+P1vsP2+P2 tag parts select screen. Click the `Load Parts` button to populate the text sources for each robo with that robo's current parts. Click the `Clear Parts` button to clear to those text sources if players are still picking builds.
5. To manage the scoreboard, enter the players' names in the `P1:` & `P2:` fields and their current scores in the boxes below those fields, then click the `Update SB` button. You can also click the `-1` & `+1` buttons to quickly decrement/increment each player's score, and press the `<->` button to switch both players' scores and names. Note: the `P1:` & `P2:` fields are actually dropdowns, and you can see how to configure those below.
6. To update tournament/event info, fill the event name in the `Event:` field and the current round in the `Round:` field, then click the `Update Tourney` button to fill the tournament info text sources.

## Additional Features & Config

Some settings can be modified in the `Config` tab.

<img width="310" height="252" alt="Screenshot 2025-10-16 163402" src="https://github.com/user-attachments/assets/e14681cc-ac12-4dc5-be6a-d2125adb42b6" />

- In the `Clear Text:` box, you can set what text gets put in the robo text sources when you click the `Clear Parts` button. Enter your preferred clear text, then click `Save`.
- In the `Player Names:` box, you can enter a list of player names that will populate the player name dropdowns. Enter each player's name on its own line, then click `Save` to sort the list and populate the dropdowns. This allows you to more quickly select names for players who appear often, but keep in mind that you can still enter other names by simply typing them in the `P1:` & `P2:` fields.
- The `Builds Pad`, `Scores Pad`, & `Names Pad` add a line of spaces below both players names & scores, and below player 2's builds. In OBS, text sources anchor to the left side by default, so these pads help make sure right- and center-aligned text sources don't move around when storing text of varying lengths. Set a value in each box to change how many spaces are entered at the bottom of the corresponding sources, or you can just set them all to 0 if you don't want to bother with it.
- In the dropdown at the bottom right, you can select which version of CRBR you're playing. Vanilla is the default version that you'd have from ripping your physical copy of CRBR, and Project Hive 3 is the community-made patch available in the CR Netplay community's discord server. Make sure to select the correct version, as some parts have different names and orders between versions.

There are some additional features for more complex functions.

- Tick the `Auto Load Parts` box to automatically load parts to the robo text sources when entering cube launch, and tick the `Auto Clear Parts` box to automatically clear the text sources when returning to stage select. Keep in mind that ticking either box will hide the corresponding button on the `Main` tab, so keep these boxes unticked if you prefer having manual control.
- This tool also enables loading particular images for each player, for example loading a picture of a robo or build that a player commonly uses. You can create your own images for each player, name them `<player_name> - p1.png` & `<player_name> - p2.png`, and place them in the `Player Images` folder. Then, whenever the scoreboard is updated, the images corresponding to each player's name are copied onto either `p1.png` or `p2.png` in `Player Images`. If there's no image matching the player's name, then `p1unknown.png` or `p2unknown.png` will be copied instead. You can add image sources in your recording software for `p1.png` & `p2.png` and these will update whenever the scoreboard is loaded. I recommend configuring the player name dropdowns to make sure that the names in the player name fields exactly match the image file names. 
- You can click the `Save Parts` button in the `Main` tab to record both players' current builds to an Excel sheet. This will create or update a file named `builds.xlsx` in the `dist` folder. A page will be created in that spreadsheet with the name `<event_name> <current_date>`, pulling event name from the `Event:` field in the `Main` tab. Builds for the same event are appended to that sheet, and a new page is created for new event names. Note: part names are pulled from the robo text files, so make sure you click `Load Parts` before clicking `Save Parts` to prevent accidentally recording the same builds twice. Also, make sure you don't have both `builds.xlsx` and the CRBR Overlay Manager open at the same time, as this can cause issues with both making changes to `builds.xlsx` by hand and automatically saving parts.

## Acknowledgements

Thanks to my friend zensol for helping me figure out a good amount of the parts loading stuff. Thanks to aldelaro5 for making the amazing [Dolphin Memory Engine](https://github.com/aldelaro5/dolphin-memory-engine), thanks to Randovania for making a [Python library for Memory Engine](https://github.com/randovania/py-dolphin-memory-engine) which made my life considerably easier, and thanks to the numerous contributors to both of those projects. Thanks to the [tkinter](https://docs.python.org/3/library/tkinter.html) contributors for the powerful UI tools, and thanks to the [PyInstaller](https://pyinstaller.org/en/stable/) contributors for enabling me to package everything into an .exe. Finally, thanks to the CR Netplay community for providing a place to play and talk about CR 20+ years after the game's release, join the community on [discord](https://discord.gg/qPXvwdeT3V) if you also love Custom Robo.
