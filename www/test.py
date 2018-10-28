import sys
import orm,asyncio
from models import User,Blog,Comment


def test( loop ):
    yield from orm.create_pool( loop = loop, user='root', password='1q2w3e4R', db='awesome' )
    u1=User(name='test1',email='test1@test.com',passwd='test1',image='about:blank')
    yield from u1.save()
    u2=User(name='test224',email='test2@test.com',passwd='test2',image='about:blank')
    yield from u2.save()
    u3=User(name='test224',email='test3@test.com',passwd='test3',image='about:blank')
    yield from u3.save()
    u4=User(name='test224',email='test4@test.com',passwd='test4',image='about:blank')
    yield from u4.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()
    if loop.is_closed():
        sys.exit(0)
