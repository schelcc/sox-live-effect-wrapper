# MicFX
Live microphone effects in linux using SoX and pulseaudio

## What is this?
It's a little Tkinter front end to the linux program SoX http://sox.10957.n7.nabble.com/csladpsa-doc-td951.html . I made this in some free time and it's really just meant to be a toy for voice calls like on Discord. I'm sorry if it's poorly written, I've never really written stuff to be used by other people. I'm just putting this out there because I have yet to see something like it.

## Setup and Dependencies
Obviously you're gonna need Python 3+ and SoX. You're also gonna need tkinter (python) if that's somehow not already installed and finally Pavucontrol.
To set it up just run the python script micFX.py and it should open a GUI. On startup it should start a Pulseaudio null sink where it will play its output. To use it in your given app just start the recording on that app and go into Pavucontrol. Navigate to the recording tab and switch your application to the monitor of null. From there you should be good to go.

## Known problems
So my code is pretty inefficient right now. In the future I'd like to swap from just executing bash commands to using SoX's wrapper. Currently it seems to spawn many null sinks? I'm not really sure what's doing it but I'm working on fixing it. Another thing is that the audio gets screwed up after using it so I usually just ```pulseaudio -k```. Not very efficient but that's how it goes.

Another thing, to use the autotune function you have to have the LADSPA pluging installed - ```sudo apt install autotalent```

## Suggestions please
This is my first time publishing code that can be used by other people so odds are I screwed something up, just let me know. I'm super open to suggestions so feel free to give me some. I'm still fairly inexperienced just to warn.

Thanks!
