# lunch_launcher

This script opens a given URL at a given time. In this case [kvartersmenyn.se](http://kvartersmenyn.se) at 11:15.

## Usage

Run the file by double clicking it or by right clicking and selecting __Run as administrator__. Running the file as an administrator will make it easier to stop the script.

### If scripts are opening in a text editor

1. Make sure the script wasn't saved with a txt extension, e.g. `lunch.js.txt`
2. Open the command prompt and run the script by typing `wscript path\to\lunch.js` (Change `path\to` to match your scripts location)

### Automation

To make the script run automatically when the computer boots, you can put it in autostart.

1. Open __Run__ by using the command `WIN + R`.
2. Type `shell:startup` och hit __OK__.
3. Put in the script file in the folder that just opened.