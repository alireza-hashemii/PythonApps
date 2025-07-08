import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes , filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a directory for saving voice messages
VOICE_DIR = 'voice_messages'
os.makedirs(VOICE_DIR, exist_ok=True)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a voice message, and I'll save it.")

# Handler for voice messages
async def voice_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the voice message
    voice = update.message.voice
 
    # Get the file ID of the voice message
    file_id = voice.file_id
    
    # Download the voice message
    new_file = await context.bot.get_file(file_id)
   
    # Define the file path
    file_path = os.path.join(VOICE_DIR, f"{file_id}.ogg")  # OGG is the format for Telegram voice messages
    
    # Save the file
    await new_file.download_to_drive(file_path)
    
    # Respond to the user
    await update.message.reply_text(f"I received your voice message and saved it as {file_id}.ogg!")



if __name__ == '__main__':
    application = ApplicationBuilder().token('7711067037:AAHJvNsCgaU8R-34iELq98Nb_N8yI-pUHrA').build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Add handler for voice messages
    application.add_handler(MessageHandler(filters._Voice, voice_message_handler))

    # Start polling updates
    application.run_polling(poll_interval=1, timeout=100)