from pydactyl import PterodactylClient
import os


Key = os.getenv('PTERO')
Server_ID = os.getenv('server')

client = PterodactylClient('https://panel.rpelliott.co.uk/', Key)
def whitelist(Player):
    client.client.servers.send_console_command(Server_ID, f"whitelist add {Player}")

def removewhitelist(Player):
    client.client.servers.send_console_command(Server_ID, f"whitelist remove {Player}")