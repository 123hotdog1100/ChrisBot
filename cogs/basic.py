import nextcord
from nextcord.ext import commands
import api.PteroAPI as p


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Used to echo back your input")
    async def echo(self, interaction: nextcord.Interaction, arg: str):
        await interaction.response.send_message(f'You Said:{arg}')

    @nextcord.slash_command(description="Whitelist your self on the Vanilla SMP")
    async def whitelist(self, interaction: nextcord.Interaction, username: str):
        p.whitelist(username)
        await interaction.response.send_message(f'I have whitelisted: {username}')@nextcord.slash_command()

    @nextcord.slash_command(description="remove your whitelist your self on the Vanilla SMP")
    async def unwhitelist(self, interaction: nextcord.Interaction, username: str):
        p.removewhitelist(username)
        await interaction.response.send_message(f'I have unwhitelisted: {username}')


def setup(bot):
    bot.add_cog(basic(bot))
