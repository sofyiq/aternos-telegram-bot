from telegram.ext import *
import secret
import time
from python_aternos import Client, ServerStartError
from getpass import getpass

#Note
print("Note: this script will never work on cloud apps like heroku or repl.it")

# Log in
username = input("Please insert your username: ")
password = input("Please insert your password: ")
botapi = input("Please insert your Telegram Bot API: ")

try:
    aternos = Client.restore_session()
except Exception:
    aternos = Client.from_credentials(username, password)

# Returns AternosServer list
servs = aternos.list_servers()

# Get the first server by the 0 index
myserv = servs[0]
 
print("Scripts running...")
 
def startserver_function(update, context):
    try:
        myserv.start()
        update.message.reply_text("Server is Starting 🕐")
        while (myserv.status_num != 1):
            myserv.fetch()
            time.sleep(5)
        update.message.reply_text("Server is Online ✅")
        update.message.reply_text("Note: Server will automagically offline in 4 minutes if there is no player online 🗿")
    except ServerStartError as err:
        update.message.reply_text("Server already running 😡")

def stopserver_function(update, context):
    myserv.stop()
    while (myserv.status_num == 1):
        myserv.fetch()
        time.sleep(5)
    update.message.reply_text("Server Stopped 🚫")

def serverstatus_function(update, context):
    myserv.fetch()
    if (myserv.status_num == 1):
        update.message.reply_text("Online ✅")
    else:
        update.message.reply_text("Server Offline 🚫")

def help_function(update, context):
    update.message.reply_text(
        """
    Available commands:
 
    /startserver
    /stopserver
    /playerlist
    /ip
    /serverstatus
    """
    )

def start_function(update, context):
    update.message.reply_text(
        """
    Tele-Aternos~
    Available commands:
 
    /startserver
    /stopserver
    /playerlist
    /ip
    /serverstatus
    """
    )

def playerlist_function(update, context):
    myserv.fetch()
    if (myserv.status_num == 0):
        update.message.reply_text("This server is offline init")
    elif (myserv.players_count <= 0):
       update.message.reply_text("This server is empty, just like my feelings towards you")
    else:
       message = f"{myserv.players_count}, {myserv.players_list}"
       update.message.reply_text(message)

def error_handler_function(update, context):
    print(f"Update: {update} caused error: {context.error}")
 
# Connecting our app with the Telegram API Key and using the context
updater = Updater(secret.API_KEY, use_context=True)
my_dispatcher = updater.dispatcher
 
# Adding CommandHandler from telegram.ext to handle defined functions/commands
my_dispatcher.add_handler(CommandHandler("help", help_function))
my_dispatcher.add_handler(CommandHandler("startserver", startserver_function))
my_dispatcher.add_handler(CommandHandler("stopserver", stopserver_function))
my_dispatcher.add_handler(CommandHandler("playerlist", playerlist_function))
my_dispatcher.add_handler(CommandHandler("serverstatus", serverstatus_function))
my_dispatcher.add_handler(CommandHandler("start", start_function))

# Error Handling if any
my_dispatcher.add_error_handler(error_handler_function)
 
# Starting the bot using polling() function and check for messages every sec
updater.start_polling(1.0)
updater.idle()

#save session
aternos.save_session()
