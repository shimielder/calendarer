from litestar import Litestar, get


@get('/')
async def index():
    return {}


app = Litestar([index])
