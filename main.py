import asyncio
from prisma import Prisma
from prisma.models import User
import random
import string


def randomize():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))[0:10]
async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    # write your queries here
    user = await User.prisma().create(
        data={
            'name': randomize(),
            'email': f'{randomize()}@craigie.dev',
        },
    )
    print(user)

    users = await db.user.find_many(include={
        'posts': True,
    },)
    print(users)

    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())