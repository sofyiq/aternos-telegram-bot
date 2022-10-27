# Access your Aternos server from Telegram Bot
> Note: this will never work on cloud 

##Make a Telegram Bot
1. Create your own telegram bot on https://telegram.me/BotFather
2. Press Start button
3. Type /newbot and hit enter
4. Follow the instruction
5. Takes note on API_TOKEN

##Install Python
1. Go to this website https://www.python.org/downloads/release/python-3110/ and download python
2. Launch the installer
3. Make sure to check ""Add Python.exe to Path
4. Follow the instruction

##Launching the scripts
clone this repo either using zip file or git

###Edit secret.py file
1. Right click secret.py file and click edit with your desire text editor
2. Copy your Telegram Bot API_TOKEN and paste it

###Install required libs
1. Open cmd on repo's directory and type
> pip3 install -r requirements.txt

Now, you can open cmd on repo's directory and launch the scripts with
> python aternos.py
