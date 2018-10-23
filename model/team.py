from database import cursor, db
from .user import User
from .points import Points

class Team:
    def __init__(self, id, name, date_created, date_updated):
        self.id = id
        self.name = name
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"[ Id: {self.id}, Name: {self.name} ]"

    def get_users(self):
        cursor.execute("""SELECT * FROM users WHERE team_id = %s""", (self.id, ))
        users = []
        for row in cursor:
            user = User.create_user(row)
            users.append(user)
        return users

    def get_point_total(self):
        cursor.execute("""SELECT SUM(points.points)
                        FROM teams
                        JOIN users ON teams.id = users.team_id
                        JOIN points ON users.id = points.user_id
                        WHERE teams.id = %s
                        """, (self.id, ))

        return cursor.fetchone()[0]


    @classmethod
    def get_all_teams(cls):
        teams = []
        cursor.execute("""SELECT * FROM teams""")
        for row in cursor:
            team = Team.create_team(row)
            teams.append(team)
        return teams

    @classmethod
    def create_team(cls, row):
        id, name, date_created, date_updated = row
        return Team(id, name, date_created, date_updated)

    @classmethod
    def get_team(cls, id):
        cursor.execute("""SELECT * from teams WHERE id = %s""", (id, ))
        row = cursor.fetchone()
        return Team.create_team(row)

    @classmethod
    def update_team(cls, id, attribute, value):
        query_string = f"""UPDATE teams SET {attribute} = %s WHERE id = %s"""
        cursor.execute(query_string, (value, id,))
        db.commit()

    @classmethod
    def delete_team(cls, id):
        cursor.execute("""DELETE FROM teams where id = %s""", (id, ))
        db.commit()


if __name__ == "__main__":

    for team in Team.get_all_teams():
        print(team)
        print(team.get_point_total())
