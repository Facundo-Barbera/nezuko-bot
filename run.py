import json
from src import NezukoBot
    

def main():
    with open('settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
        token = settings['discord_bot_token']

    bot = NezukoBot(command_prefix='!')
    bot.run(token, log_handler=None)

if __name__ == "__main__":
    main()
