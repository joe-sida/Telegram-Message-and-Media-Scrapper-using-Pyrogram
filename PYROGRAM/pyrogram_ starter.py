from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "telegram_api_id": int(os.getenv("TG_API_ID")),
    "telegram_hash": os.getenv("TG_API_HASH"),
}

app = Client("my_account", CONFIG["telegram_api_id"], CONFIG["telegram_hash"])

chat_id = -1001204209308  #update the chat-id from telegram web


async def main():
    async with app:
        async for message in app.get_chat_history(chat_id):
            # Get the user_id
            user_id = message.from_user.id if message.from_user else None

            # Print user_id, message text, and download media if available
            print(f"User ID: {user_id}")
            print(f"Message: {message.text}")

            # Check if the message contains media
            if message.media:
                try:
                    # Download media and print the file path
                    file_path = await app.download_media(message)
                    print(f"Media File Path: {file_path}")
                except ValueError as ve:
                    print(f"Error downloading media: {ve}")

            print("\n")  # Add a new line for better readability


app.run(main())




