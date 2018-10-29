from database import cursor, db
import json

########################################################################################################################
########################################################################################################################
# User

class User:
    def __init__(self, id, name, team_id, date_created, date_updated):
        self.id = id
        self.team_id = team_id
        self.name = name
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"[ Id: {self.id}, Name: {self.name} ]"

    @classmethod
    def create_user_from_row(cls, row):
        id, name, team_id, date_created, date_updated = row
        return User(id, name, team_id, date_created, date_updated)

    ####################################################################################################################
    # GET

    @classmethod
    def get_all_users(cls):
        users = []
        cursor.execute("""SELECT * FROM users""")
        for row in cursor:
            user = User.create_user_from_row(row)
            users.append(user)
        return users

    @classmethod
    def get_user(cls, id):
        cursor.execute("""SELECT * from users WHERE id = %s""", (id, ))
        row = cursor.fetchone()
        return User.create_user_from_row(row)

    ####################################################################################################################
    # INSERT

    @classmethod
    def insert_user_into_database(cls, name, team_id, date_created, date_updated):
        cursor.execute("""INSERT INTO users (name, team_id, date_created, date_updated)
        VALUES (%s, %s, %s, %s)""", (name, team_id, date_created, date_updated))
        db.commit()


    ####################################################################################################################
    # UPDATE

    @classmethod
    def update_user(cls, id, attribute, value):
        query_string = f"""UPDATE users SET {attribute} = %s WHERE id = %s"""
        cursor.execute(query_string, (value, id,))
        db.commit()

    ####################################################################################################################
    # DELETE

    @classmethod
    def delete_user(cls, id):
        cursor.execute("""DELETE FROM users where id = %s""", (id, ))
        db.commit()

    ####################################################################################################################
    # JSON CONVERSION

    @classmethod
    def get_all_users_json(cls):
        all_users = User.get_all_users()
        users_json = {
            'results': [

            ]
        }
        for user in all_users:
            user_data = User.get_user_dict(user)
            users_json['results'].append(user_data)
        return json.dumps(users_json)

    @classmethod
    def get_user_json(cls, id):
        user = User.get_user(id)
        user_dict = User.get_user_dict(user)
        return json.dumps(user_dict)

    @classmethod
    def get_user_dict(cls, user):
        user_data = {
                'id': user.id,
                'name': user.name,
                'team_id': user.team_id,
                'date_created': user.date_created.isoformat(),
                'date_updated': user.date_updated.isoformat(),
            }
        return user_data

    @classmethod
    def create_user_from_json(cls, user_json):
        name = user_json['name']
        team_id = user_json['team_id']
        date_created = user_json['date_created']
        date_updated = user_json['date_updated']
        User.insert_user_into_database(name, team_id, date_created, date_updated)

if __name__ == "__main__":
    for user in User.get_all_users():
        print(user)
        for point in user.get_points():
            print("    " + str(point))

    print()

    for user in User.get_all_users():
        print(user)
    print()
