import asyncio, orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(user='root', password='', db='awesome', loop=loop, charset='utf8')
    u = User(name='Test15', email='test15@example.com', passwd='123456', image='about:blank')
    await u.save()
    # await orm.destory_pool()

# #要运行协程，需要使用事件循环
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        # loop.close()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()