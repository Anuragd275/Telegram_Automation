from telethon import TelegramClient

api_id = 'API_ID' #without ''
api_hash = 'API_HASH'
# values from your account
client = TelegramClient('session', api_id, api_hash)

def main():
    async def forward_message():
        source = '' 
        destination = ''
        #do not play with message_id_list.
        message_id_list = []

        # limit = 3 will scrape only last 3 messages from the source channel, set its value according to your needs.
        async for message in client.iter_messages(source, limit=3):
            message_id_list.append(message.id)
        await client.send_message(destination, message, source)

    with client:
        client.loop.run_until_complete(forward_message())

if __name__ == "__main__":
    main()
