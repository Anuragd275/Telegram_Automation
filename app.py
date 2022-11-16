from telethon import TelegramClient

api_id = API_ID
api_hash = 'API_HASH'
# values of your account
client = TelegramClient('session', api_id, api_hash)

async def main():
    source = ''
    destination = ''
    message_id_list = []

    async for message in client.iter_messages(source, limit=3):
        message_id_list.append(message.id)
    await client.send_message(destination, message, source)

with client:
    client.loop.run_until_complete(main())
