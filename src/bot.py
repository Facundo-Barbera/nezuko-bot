import logging

import discord
from discord.ext import commands

# Define the intents for the bot
INTENTS = discord.Intents.all()

# Define the extensions for the bot
EXTENSIONS = [
    "src.extensions.testing",
    "src.extensions.chat_extension"
]

# Define the base for the logger
LOGGER_BASE = "discord."


class NezukoBot(commands.Bot):
    """
    NezukoBot is a subclass of commands.Bot, which represents a Discord bot.
    """

    def __init__(self, command_prefix, update_tree=False, **options):
        """
        Initialize the bot with the given command prefix and options.
        If update_tree is True, the command tree will be updated when the bot is set up.

        :param command_prefix: The prefix that triggers the bot's commands.
        :param update_tree: Whether to update the command tree when the bot is set up.
        :param options: Additional options for the bot.
        """
        super().__init__(command_prefix, intents=INTENTS, **options)
        self.update_tree = update_tree

    @staticmethod
    def get_logger(name) -> logging.Logger:
        """
        Get a logger with the given name, prefixed with LOGGER_BASE.

        :param name: The name of the logger.
        :return: The logger.
        """
        return logging.getLogger(LOGGER_BASE + name)

    async def setup_hook(self) -> None:
        """
        Set up the bot by loading the extensions and updating the command tree if necessary.
        """
        logger = self.get_logger("bot")
        for extension in EXTENSIONS:
            try:
                await self.load_extension(extension)
            except Exception as e:
                logger.error(f"Failed to load extension {extension}.", exc_info=e)
            else:
                logger.info(f"Loaded extension {extension}.")

        if self.update_tree:
            await self.tree.sync()
            logger.info("Command tree updated.")

    async def on_ready(self) -> None:
        """
        Perform actions when the bot is ready, such as setting the status and logging that the bot is ready.
        """
        logger = self.get_logger("bot")
        logger.info("Setting status...")
        await self.change_presence(activity=discord.Game(name="Ready to help!"))
        logger.info("Bot is ready!")
