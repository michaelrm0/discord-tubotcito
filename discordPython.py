import discord
llave = "NzU0OTYwMDYyMzM3OTA4ODk3.X18VWQ.vzBHgIXssPO5gvHAV42a1ml7G7w"
cliente = discord.Client()
@cliente.event
async def on_message(mensaje):
    if mensaje.content.find("!hola-mundo") != -1:
        await mensaje.channel.send("Hola! desde discord")
cliente.run(llave)