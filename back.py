import aiohttp
import asyncio
import APIKEY

async def back():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.api-ninjas.com/v1/cryptoprice?symbol=LTCBTC', headers=APIKEY.HEADERS) as resp:
            print(resp.status)
            print(await resp.text())

            
asyncio.run(back())




    