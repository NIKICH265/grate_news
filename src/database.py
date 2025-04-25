from json import loads, dumps

database_link = "src/database.json"


def read_user():
    with open(database_link, "r") as file:
        database = file.read()
    return loads(database)


def create_data(user):
    db = read_user()
    idx = len(db) + 1
    user["id"] = idx
    user["password"] = user["password"].decode()
    db.append(user)
    with open(database_link, "w") as file:
        file.write(dumps(db, indent=4))
    return user
