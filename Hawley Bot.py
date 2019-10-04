import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("아심심해")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요! 전 Hawley라고 해요!")
    if message.content.startswith("!도와줘"):
        await message.channel.send("아직은 제작자가 못만들어서 못하는 기능이예요 ㅠㅠ 나중에 정식 출시 되면 해볼게요!")
    if message.content.startswith("!놀아줘"):
        await message.channel.send("죄송하지만 저 바쁜데.. 나중에 놀아드릴게요!")
    if message.content.startswith("!이건우"):
        await message.channel.send("솔직히 말하자면 우리 반에서 제일 찐따고 못생겼고 울보인 애.")
    if message.content.startswith("!악마Hawley봇은?"):
        await message.channel.send("https://discord.gg/CVXRzmC")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
