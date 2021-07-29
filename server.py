from aiohttp import web

class Health(web.View):

    async def get(self):
        return web.json_response({'status':'OK'})

async def register(app):
    print('приложение запущено')
    yield
    print('приложение завершено')


app = web.Application()
app.add_routes([web.get('/health', Health)])
app.cleanup_ctx.append(register)

web.run_app(app)
