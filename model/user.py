from database import cursor, db
from .points import Points


class User:
    def __init__(self, id, name, team_id, date_created, date_updated):
        self.id = id
        self.team_id = team_id
        self.name = name
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"[ Id: {self.id}, Name: {self.name} ]"

    def get_points(self):
        cursor.execute("""SELECT * FROM points WHERE user_id = %s""", (self.id, ))
        point_group = []
        for row in cursor:
            points = Points.instantiate_points(row)
            point_group.append(points)
        return point_group

    @classmethod
    def get_all_users(cls):
        users = []
        cursor.execute("""SELECT * FROM users""")
        for row in cursor:
            user = User.create_user(row)
            users.append(user)
        return users

    @classmethod
    def create_user(cls, row):
        id, name, team_id, date_created, date_updated = row
        return User(id, name, team_id, date_created, date_updated)

    @classmethod
    def get_user(cls, id):
        cursor.execute("""SELECT * from users WHERE id = %s""", (id, ))
        row = cursor.fetchone()
        return User.create_user(row)

    @classmethod
    def update_user(cls, id, attribute, value):
        query_string = f"""UPDATE users SET {attribute} = %s WHERE id = %s"""
        cursor.execute(query_string, (value, id,))
        db.commit()

    @classmethod
    def delete_user(cls, id):
        cursor.execute("""DELETE FROM users where id = %s""", (id, ))
        db.commit()

if __name__ == "__main__":
    for user in User.get_all_users():
        print(user)
        for point in user.get_points():
            print("    " + str(point))

    print()

    for user in User.get_all_users():
        print(user)
    print()

