from database import cursor, db
import json

########################################################################################################################
########################################################################################################################
# Points

class Team:
    def __init__(self, id, name, date_created, date_updated):
        self.id = id
        self.name = name
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"[ Id: {self.id}, Name: {self.name} ]"

    @classmethod
    def create_team_from_row(cls, row):
        id, name, date_created, date_updated = row
        return Team(id, name, date_created, date_updated)

    ####################################################################################################################
    # GET

    @classmethod
    def get_all_teams(cls):
        teams = []
        cursor.execute("""SELECT * FROM teams""")
        for row in cursor:
            team = Team.create_team_from_row(row)
            teams.append(team)
        return teams

    @classmethod
    def get_team(cls, id):
        cursor.execute("""SELECT * from teams WHERE id = %s""", (id, ))
        row = cursor.fetchone()
        return Team.create_team_from_row(row)

    ####################################################################################################################
    # INSERT

    @classmethod
    def insert_team_into_database(cls, name, date_created, date_updated):
        cursor.execute("""INSERT INTO teams (name, date_created, date_updated)
        VALUES (%s, %s, %s)""", (name, date_created, date_updated))
        db.commit()

    ####################################################################################################################
    # UPDATE

    @classmethod
    def update_team(cls, id, attribute, value):
        query_string = f"""UPDATE teams SET {attribute} = %s WHERE id = %s"""
        cursor.execute(query_string, (value, id,))
        db.commit()

    ####################################################################################################################
    # DELETE

    @classmethod
    def delete_team(cls, id):
        cursor.execute("""DELETE FROM teams where id = %s""", (id, ))
        db.commit()

    ####################################################################################################################
    # JSON CONVERSION

    @classmethod
    def get_all_teams_json(cls):
        all_teams = Team.get_all_teams()
        team_json = {
            'results': [

            ]
        }
        for team in all_teams:
            team_data = Team.get_team_dict(team)
            team_json['results'].append(team_data)
        team_json = json.dumps(team_json)
        return team_json

    @classmethod
    def get_team_json(cls, id):
        team = Team.get_team(id)
        team_data = Team.get_team_dict(team)
        team_json = json.dumps(team_data)
        return team_json

    @classmethod
    def get_team_dict(cls, team):
        team_data = {
            'id': team.id,
            'name': team.name,
            'date_created': team.date_created.isoformat(),
            'date_updated': team.date_updated.isoformat(),
        }
        return team_data

    @classmethod
    def create_team_from_json(cls, team_json):
        name = team_json['name']
        date_created = team_json['date_created']
        date_updated = team_json['date_updated']
        Team.insert_team_into_database(name, date_created, date_updated)


if __name__ == "__main__":

    for team in Team.get_all_teams():
        print(team)
        print(team.get_point_total())
