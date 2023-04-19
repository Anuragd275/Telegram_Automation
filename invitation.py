#Scrap users from 1 channel and send them vustom messages.

from telethon.sync import TelegramClient, events
from telethon import TelegramClient

api_id = ""
api_hash = ""


client = TelegramClient('name', api_id, api_hash)

user_name = []

caption_text = "Are you looking for the best deals on your favorite items? Want to stay ahead of the competition and get unbeatable prices? Look no further than our exclusive WhatsApp group, where we provide the best steals on Amazon and Flipkart.\n\n Sorry to slide into your dm ;__;"

async def main():

    chat = ''
    users = await client.get_participants(chat)
    print(users[0].first_name)

    for user in users:
        if user.username is not None:
            user_name.append(user.username)

    for receiver in user_name:
        await client.send_file(receiver,'photo.jpeg', caption='')

    # this piece of code  will save all the members in a txt file.

    # with open("output.txt", "w") as txt_file:
    #     for line in user_name:
    #         txt_file.write("".join(line) + "\n")

with client:
    client.loop.run_until_complete(main())
