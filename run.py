from telegram.ext import CommandHandler, CallbackContext, Updater
from telegram import Update
from config import *
from logger import logger
from utils import check_user_id
from pyngrok import ngrok


ssh_tunnel = None

@check_user_id
def open_tunnel(update: Update, context: CallbackContext):
    global ssh_tunnel

    chat_id = update.message.chat_id

    logger.info("Handeling '/open' command.")

    if ssh_tunnel == None:
        ssh_tunnel = ngrok.connect(22, "tcp")

        context.bot.send_message(chat_id, ssh_tunnel.public_url)

        logger.info(f"Tunnel opened at '{ssh_tunnel.public_url}'.")

    else:
        context.bot.send_message(chat_id, ssh_tunnel.public_url)
    
@check_user_id
def close_tunnel(update: Update, context: CallbackContext):
    global ssh_tunnel

    chat_id = update.message.chat_id

    logger.info("Handeling '/close' command.")

    if ssh_tunnel != None:

        ngrok.disconnect(ssh_tunnel.public_url)


        context.bot.send_message(chat_id, "Closed.")
        logger.info(f"Tunnel '{ssh_tunnel.public_url}' closed..")

        ssh_tunnel = None
    else:
        context.bot.send_message(chat_id, "No open tunnels.")



def main():

    # Creating the bot
    updater = Updater(TOKEN)

    open_tunnel_command_handler = CommandHandler('open', open_tunnel)
    close_tunnel_command_handler = CommandHandler('close', close_tunnel)

    updater.dispatcher.add_handler(open_tunnel_command_handler)
    updater.dispatcher.add_handler(close_tunnel_command_handler)

    logger.info("Bot is running...")
    updater.start_polling()

if __name__ == "__main__":
    main()