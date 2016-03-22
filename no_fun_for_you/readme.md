# no_fun_for_you

This scripts triggers a text-to-speech warning when you spend too much time on social media.

## Usage

1. Download and install [Python](https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi)
2. Download [PyWin32](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/pywin32-220.win32-py2.7.exe/download)
3. __Important:__ Right click the install file PyWin32 and select __Run as administrator__ to install.
   
   If that doesn't work you can try ​installing PyWin32 from the command prompt. Make sure you open the command prompt by right-clicking and selecting __Run as administrator__ and running this command `C:\python27\python.exe -m pip install pypiwin32`

4. Install pyttsx by running the following in the command prompt `python -m pip install pyttsx`
5. If `python` isn't a defined command you need to type the full path to python, e.g. `C:\python27\python.exe -m pip install pyttsx`
6. Double click the script file to run.

__Optional__: If you'd like to run the script without opening a console window: Change the file extension from __.py__ to __.pyw__

### Automation

To further automate the script you can use the Windows Task Scheduler.

1. Open the Task Scheduler by running __Run__ `WIN + R` and typing `Taskschd.msc`
2. Select __Create activity__.
3. Name the activity something like *Notificationhandle*
4. Create a new trigger in the __Trigger__-tab and select the time your workday starts. E.g. *Monday 09:30*
5. Select __Stop activity if it runs longer than__ and type in `210 min` to stop the script at lunch time 12:00.
6. Create another trigger and select 13.00 Monday-Friday to activate the script again after lunch. Set __Stop activity__ to `240 min` to stop the script after the workday ends.
7. To activate the script every workday, select __Every week__ and check __Monday-Friday__
8. Hit __OK__ and go to the __Actions__-tab. Here you can select what happens when the trigger is trigged. Select __Run a program__ and browse to the script file.