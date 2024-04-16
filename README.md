# About
This project demonstrating working with prisma

we have found out u have to define the schema in the schema.prisma[conventional name] file

but if u want to use another name for the schema file you can do it like this
`--schema=schema2.prisma`

after defining the schema which will care the database and its tables and columns, and so

type
`prisma dp push` [provide schema if custom one]

this is will create the database it can be created locally like with sqlite3
or with mysql in MySQL workbench

after creating the database u have to generate the client and u can use it
`prisma generate --watch`[provide custom schema if found]

u will find out that the code snippet in any file when u importing prisma has changed so if u defined a user table in the schema u will find a user model in the client folder
```python
from prisma import User
```

and so

and write ur code in any file then run it and it will be reflected automatically in the database

every database has different urls
also u can make the mysql inside ur project by providing the 
```bash
url = "file:database.db"
```

also sqlite is not very supported from prisma

and for some reason it looks prisma has some problems with Pydantic library maybe if u downgrade Pydantic this is will solve it

# Prisma
to learn about prisma there are three things
prisma server or just prisma
prisma client
prisma cli

prisma is considered new ORM generation


# Dir
i have give app.py for mysql database and main.py for sqlite database

i wont go further, those examples are sufficient for us

# Note
prisma handles many thing for u like unrepeated data,data types [built on top of pyright], editor support and more
also it supports async and sync programming
