from telethon import TelegramClient, events
import asyncio

import config as cfg

app = TelegramClient('Telethon_UserBot', cfg.API_ID, cfg.API_HASH)

@app.on(events.NewMessage())
async def on_message(event: events.NewMessage.Event):
    print(event.chat_id, event.message.message)
    await event.message.reply('Hello from Telethon UserBot!')

if __name__ == "__main__":
    try:
        print('App Started')
        app.start(phone=cfg.PHONE, password=cfg.TWO_STEP_PASS)
        app.run_until_disconnected()
    except KeyboardInterrupt:
        print('App Finished')