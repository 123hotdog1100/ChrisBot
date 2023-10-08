from pydactyl import PterodactylClient
import config


Key = config.ptero
Server_ID = config.server

client = PterodactylClient('https://panel.rpelliott.co.uk/', Key)
def whitelist(Player):
    client.client.servers.send_console_command(Server_ID, f"whitelist add {Player}")

def removewhitelist(Player):
    client.client.servers.send_console_command(Server_ID, f"whitelist remove {Player}")