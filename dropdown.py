import typing

import discord
from discord.ext import commands


# 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟
# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label=' ', value=1, description=' ', emoji='1️⃣'),
            discord.SelectOption(label=' ', value=2, description=' ', emoji='2️⃣'),
            discord.SelectOption(label=' ', value=3, description=' ', emoji='3️⃣'),
            discord.SelectOption(label=' ', value=4, description=' ', emoji='4️⃣'),
            discord.SelectOption(label=' ', value=5, description=' ', emoji='5️⃣'),
            discord.SelectOption(label=' ', value=6, description=' ', emoji='6️⃣'),
            discord.SelectOption(label=' ', value=7, description=' ', emoji='7️⃣'),
            discord.SelectOption(label=' ', value=8, description=' ', emoji='8️⃣'),
            discord.SelectOption(label=' ', value=9, description=' ', emoji='9️⃣'),
            discord.SelectOption(label=' ', value=10, description=' ', emoji='🔟')
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Hole', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.

        # await interaction.response.send_message(f'Good job on your {self.values[0]}')
        print(f"{interaction.user.name} selected {self.values[0]}")


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'))
        self.hole_count = None
        self.total_holes = []

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = Bot()


@bot.command()
async def letsgo(ctx, *, hole_count_num: int):

    # Create the view containing our dropdown
    bot.hole_count_num = DropdownView()

    # Sending a message containing our view
    for hole in range(0, hole_count_num):
        view = DropdownView()
        bot.total_holes.append(view)
        await ctx.send(f'How did you do on Hole {hole+1}?:', view=view)


# todo whatever I want

@bot.command()
async def goodbye(ctx):
    for hole in bot.total_holes:
        hole.stop()
        print(f"Stopped hole {hole}")
    await ctx.send(f'Drive home safe')
