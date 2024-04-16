import asyncio
from prisma import Prisma
from prisma.models import Post
import random
import string


def randomize():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))[0:10]
async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    # write your queries here
    user = await Post.prisma().create(
        {
            'title': 'Hello from prisma!',
            'desc': 'Prisma is a database toolkit and makes databases easy.',
            'published': True,
        }
    )
    print(user)

    users = await db.post.find_many()
    print(users)

    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())