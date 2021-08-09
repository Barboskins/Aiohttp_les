from aiohttp import web
import aiopg
import gino

# DB_DSN = 'postgres://postgres:amibamcx3700@localhost:5432/aiohttp'
DB_DSN = f'postgres://aiohttp:12345@127.0.0.1:5432/aiohttp'

"""создаем объет gino"""
db = gino.Gino()

"""Базовая модель класса с разными методами, для наследования др. моделями"""
class BaseModel:
    @classmethod
    async def get_or_404(cls, id_):
        instance = cls.get_or_404(id_)
        """Если нет id то надо вывести исключение об этом"""
        if not instance:
            raise web.HTTPNotFound()
        return instance


"""Модель User с полями"""
class User(db.Model,BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    _idx1 = db.Integer('users_user_username', 'username', unique=True)

"""Пример"""

class Health(web.View):

    async def get(self):
        return web.json_response({'status':'OK'})

"""Регистрация подключения к БД"""

async def register_pg_pool(app):
    print('приложение запущено')
    async with aiopg.create_pool(DB_DSN) as pool:
        app['pg_pool'] = pool
        yield
        pool.close()
    print('приложение завершено')

"""Регистрация подключения к ОРМ"""
async def register_orm(app):
    await db.set_bind(DB_DSN)
    yield
    await db.pop_bind().close()


"""Вьюха для получения  всех пользователей из БД"""

class UserView(web.View):
    async def get(self):
        pool = self.request.app['pg_pool']
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM users")
                db_response = await cur.fetchall()
                return web.json_response(db_response)


"""Вьюха для получения пользователей из БД по ID"""


app = web.Application()
app.add_routes([web.get('/health', Health)])
app.add_routes([web.get('/users', UserView)])
app.cleanup_ctx.append(register_pg_pool)
app.cleanup_ctx.append(register_orm)

web.run_app(app)
