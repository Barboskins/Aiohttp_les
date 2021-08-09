import asyncio
from aiohttp import ClientSession

async def check_health():
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/health') as resp:
            return await resp.json()

async def get_users():
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/users') as resp:
            return await resp.json()


async def main():
    response = await check_health()
    print(response)
    response = await get_users()
    print(response)

asyncio.run(main())
