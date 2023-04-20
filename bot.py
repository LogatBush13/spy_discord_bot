import discord
import cv2
import numpy as np
import pyautogui
import randomyt

settings = {
    'camera_enabled' : False,
    'screenshot_enabled' : False,
    'click_enabled' : False,
    'typing_enabled' : False,
    'yt_enabled' : False
}

async def send_message(message):
    try:
        msg = message.content.lower()

        if msg == '.camspy':
            if settings['camera_enabled']:
                cam = cv2.VideoCapture(0)
                result, image = cam.read()

                if result:
                    cv2.imwrite('pictures/spy/camspy.png', image)
                    await message.channel.send(file=discord.File('pictures/spy/camspy.png'))

                else:
                    await message.channel.send('An error occured')
            else:
                await message.channel.send('Camera is not enabled')

        if msg == '.screenspy':
            if settings['screenshot_enabled']:
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                
                cv2.imwrite('pictures/spy/screenspy.png', image)

                await message.channel.send(file=discord.File('pictures/spy/screenspy.png'))
            else:
                await message.channel.send('Screenshotting is not enabled')

        if msg == '.click':
            if settings['click_enabled']:
                pyautogui.click()
                await message.channel.send('clicked NYHEHEHEHEHE')
            else:
                await message.channel.send('Clicking is not enabled (NERD)')

        if msg.startswith('.type '):
            if settings['typing_enabled']:
                word = msg.replace('.type ', '')
                pyautogui.write(word)
                await message.channel.send(f'typed {word}')
            else:
                await message.channel.send('Typing is not enabled')

        if msg == '.yt':
            if settings['yt_enabled']:
                video = 'https://www.youtube.com/watch?v=' + randomyt.youtube_search()
                await message.channel.send(video)
            else:
                await message.channel.send('Youtube is not enabled')

        if msg == '.help':
            await message.channel.send('.camspy : take picture with my camera \n .screenspy : take screenshot on my pc \n .click : click my mouse \n .type : type something on my comuter ex .type (message) \n .yt : pulls up a random youtube video \n .help : pulls up help message')


    except discord.HTTPException:
        pass


def run_bot(token):

    TOKEN = token

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        await send_message(message)

        
    client.run(TOKEN)