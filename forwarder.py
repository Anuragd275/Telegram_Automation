"""
    this python script is designed to forward all messages from a particular channel (source) to another channel (destination).
    ==> Keep in mind that the forwared message in the destination channel will have the tag saying "forwarded from xyz" channel, where xyz is the source channel.
"""

from telethon import TelegramClient

api_id = 'API_ID' #without ''
api_hash = 'API_HASH'
# Use your own values from Core Telegram.
client = TelegramClient('session', api_id, api_hash)

def main():
    async def forward_message():
        # source channel username/link.
        source = '' 
        #destination channel username/link.
        destination = ''

        #do not play with message_id_list, it may lead to unknown behavior.
        message_id_list = []

        # limit = 3 will scrape only last 3 messages from the source channel, set its value according to your needs.
        async for message in client.iter_messages(source, limit=3):
            message_id_list.append(message.id)
        await client.send_message(destination, message, source)

    with client:
        client.loop.run_until_complete(forward_message())

if __name__ == "__main__":
    main()
