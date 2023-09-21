import discord
from discord.ext import commands
import logging
from .logger import create_logger, cleanup_logs

DEFAULT_INTENTS = discord.Intents.default()

class NezukoBot(commands.Bot):
    def __init__(self, command_prefix, log_dir='logs'):
        super().__init__(command_prefix, intents=DEFAULT_INTENTS)

        # Create loggers
        self.log_dir = log_dir
        cleanup_logs(self.log_dir)

        self.logger = create_logger('nezuko', self.log_dir)
        create_logger("discord", self.log_dir)

    async def setup_hook(self):
        self.logger.info('Setting up bot...')
        self.logger.info('Done!')

    async def on_ready(self):
        self.logger.info('Bot is ready!')
