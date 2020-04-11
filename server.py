from bot import Chatbot
import google
import sys
bot = Chatbot("token.cfg")


def makeReply(msg,user):
    reply = None
    if msg is not None:
        reply = google.translateText(msg,user)
    return reply

def run():
    print("Bot running....")
    update_id = None
    while True:
        updates = bot.getUpdates(offset=update_id)
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = str(item["message"]["text"])
                    from_ = item["message"]["from"]["id"]
                    from_user= item["message"]["from"]["first_name"]
                    reply = makeReply(message,from_user)
                    bot.sendMessage(reply, from_)
                except:
                    message = None
                    continue


if __name__ == "__main__":

    try:
        run()
    except:
        print("Bot has stopped working.")

