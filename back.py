def back_main():
    import aiohttp
    import asyncio
    import APIKEY

    async def back():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.api-ninjas.com/v1/bitcoin', headers=APIKEY.HEADERS) as resp:
                if resp.status == 200:
                    JSON_BITCOIN = await resp.json()
                    BTCINFO = dict(JSON_BITCOIN)
                    BTCPRICE = BTCINFO["price"]
                else:
                    print("NOT CONNECT")
            
            

            
    asyncio.run(back())




    