""" This python script is designed to scrap members from a Telegram entity(Group/Supergroup), and send a custom message to each member in their inbox.
    Custom message here is just a template, customize it according to your needs.
"""
from telethon.sync import TelegramClient, events
from telethon import TelegramClient

# Use your own values from Core Telegram.
api_id = ""
api_hash = ""
client = TelegramClient('name', api_id, api_hash)

user_name = []

caption_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse gravida."

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
    with open("output.txt", "w") as txt_file:
         for line in user_name:
             txt_file.write("".join(line) + "\n")

with client:
    client.loop.run_until_complete(main())
