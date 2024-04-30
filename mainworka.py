import logging
import os

from telegram import __version__ as TG_VER
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

my_bot_token = os.environ['tokentg']

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Dictionnaire des produits avec leurs descriptions et vidéos
products = {
    "static": {
        "description": "HASH premium de qualité, séché à l'air, rosay 95µ",
        "video": "static.mp4"
    },
    "3x": {
        "description": "HASH premium filtré trois fois, acapulco 120µ",
        "video": "3x.mp4"
    },
    "beldia": {
        "description": "Beldia static AK47, HASH de qualité supérieure",
        "video": "staticak.mp4"
    },
    "jaune": {
        "description": "HASH jaune mousseux, première presse tom and jerry",
        "video": "jaune.mp4"
    },
    "rosay": {
        "description": "HASH premium rosay 95µ",
        "video": "rozay.mp4"
    }
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to our premium HASH bot. To see available products, use the command /products.",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
    Welcome to our Premium HASH Bot! Here are the available commands:

    /start - Start the bot and get a welcome message.
    /help - Display this help message.
    /products - View available products and their descriptions.
    /static - View the static product video.
    /3x - View the 3x product video.
    /beldia - View the beldia product video.
    /jaune - View the jaune product video.
    /rosay - View the rosay product video.
    /frozen - View the frozen product video.

    Feel free to explore our offerings and enjoy your experience!
    """
    await update.message.reply_text(help_text)


async def list_products(update: Update,
                        context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message listing available products."""
    product_list = '\n'.join(
        [f"{product}: {products[product]['description']}" for product in products])
    await update.message.reply_text(
        f"Available products:\n{product_list}")


async def send_product_video(update: Update,
                             context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a video of the requested product."""
    product_name = update.message.text.strip().lower()
    if product_name in products:
        video_path = products[product_name]['video']
        with open(video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Product not found.")


async def send_static_video(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the static product video."""
    static_video_path = products.get("static", {}).get("video")
    if static_video_path:
        with open(static_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Static product video not found.")


async def send_frozen_video(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the frozen product video."""
    frozen_video_path = products.get("frozen", {}).get("video")
    if frozen_video_path:
        with open(frozen_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Frozen product video not found.")


async def send_jaune_video(update: Update,
                           context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the jaune product video."""
    jaune_video_path = products.get("jaune", {}).get("video")
    if jaune_video_path:
        with open(jaune_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Jaune product video not found.")


async def send_3x_video(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the 3x product video."""
    _3x_video_path = products.get("3x", {}).get("video")
    if _3x_video_path:
        with open(_3x_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("3x product video not found.")


async def send_rosay_video(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the rosay product video."""
    rosay_video_path = products.get("rosay", {}).get("video")
    if rosay_video_path:
        with open(rosay_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Rosay product video not found.")


async def send_beldia_video(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the beldia product video."""
    beldia_video_path = products.get("beldia", {}).get("video")
    if beldia_video_path:
        with open(beldia_video_path, 'rb') as video:
            await update.message.reply_video(video=video)
    else:
        await update.message.reply_text("Beldia product video not found.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(my_bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("products", list_products))
    application.add_handler(CommandHandler("static", send_static_video))
    application.add_handler(CommandHandler("frozen", send_frozen_video))
    application.add_handler(CommandHandler("jaune", send_jaune_video))
    application.add_handler(CommandHandler("3x", send_3x_video))
    application.add_handler(CommandHandler("rosay", send_rosay_video))
    application.add_handler(CommandHandler("beldia", send_beldia_video))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()