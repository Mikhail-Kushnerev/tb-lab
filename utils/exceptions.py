import aiohttp


async def check_connect(url):
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            print(response.status)
            if response.status == 400:
                raise Exception
    except Exception:
        print("s")
    else:
        return True
