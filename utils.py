
from config import ALLOWED_USERS


def check_user_id(func):

    def inner(*args, **kwargs):

        updater = args[0]
        context = args[1]

        if updater.message.from_user["id"] not in ALLOWED_USERS:
            context.bot.send_message(updater.message.chat_id, "403 Forbidden")
            return

        func(*args, **kwargs)
    
    return inner