date = new Date();

//Loop until the time is 11:15
while(!(date.getHours()==11 && date.getMinutes()==15)) 
{
	//Wait 1 sec between each iteration.
	WScript.sleep(1000);
	date = new Date();
}


//Create a Shell object that enable us to run commands.
var WshShell = WScript.CreateObject("WScript.Shell");
//Open link in the default browser. 
WshShell.Run("http://kvartersmenyn.se");