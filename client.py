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

async def get_user():
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/user/1') as resp:
            return await resp.json()

async def create_user():
    async with ClientSession() as session:
        async with session.post('http://127.0.0.1:8080/user', json={
            'username':'user_1',
            'name':'name_of_user',
            'password':'pwd1'
        }) as resp:
            return await resp.json()

async def main():
    response = await check_health()
    print(response)
    response = await get_users()
    print(response)
    response = await get_user()
    print(response)
    response = await create_user()
    print(response)

asyncio.run(main())
