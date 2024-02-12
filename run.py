import os

from src.bot import NezukoBot


def main():
    """
    Main function to run the NezukoBot.

    Retrieves the DISCORD_BOT_TOKEN and UPDATE_TREE environment variables.
    If UPDATE_TREE is '1' and user confirms, updates the command tree.
    Initializes and runs the NezukoBot with the retrieved token and update_tree flag.
    """

    # Get DISCORD_BOT_TOKEN environment variable
    token = os.getenv('DISCORD_BOT_TOKEN')

    # Check if UPDATE_TREE environment variable is '1'
    update_tree = os.getenv('UPDATE_TREE') == '1'

    # Initialize NezukoBot with command prefix 'n!' and update_tree flag
    bot = NezukoBot(command_prefix='n!', update_tree=update_tree)

    # Run NezukoBot with retrieved token
    bot.run(token)


# Test
if __name__ == '__main__':
    # If script is run directly, call the main function
    main()
