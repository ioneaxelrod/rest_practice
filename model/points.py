from database import cursor, db
import json

########################################################################################################################
########################################################################################################################
# Points

class Points:
    def __init__(self, id, user_id, points, reason, date_created):
        self.id = id
        self.user_id = user_id
        self.points = points
        self.reason = reason
        self.date_created = date_created

    def __repr__(self):
        return f"[ Id: {self.id}, Points: {self.points} ]"

    @classmethod
    def create_points_from_row(cls, row):
        id, user_id, points, reason, date_created = row
        return Points(id, user_id, points, reason, date_created)

    ####################################################################################################################
    # GET

    @classmethod
    def get_all_points(cls):
        point_groups = []
        cursor.execute("""SELECT * FROM points""")
        for row in cursor:
            points = Points.create_points_from_row(row)
            point_groups.append(points)
        return point_groups

    @classmethod
    def get_points(cls, id):
        cursor.execute("""SELECT * from points WHERE id = %s""", (id, ))
        row = cursor.fetchone()
        return Points.create_points_from_row(row)

    ####################################################################################################################
    # INSERT

    @classmethod
    def insert_points_into_database(cls, user_id, points, reason, date_created):
        cursor.execute("""INSERT INTO points (user_id, points, reason, date_created)
        VALUES (%s, %s, %s, %s)""", (user_id, points, reason, date_created))
        db.commit()

    ####################################################################################################################
    # UPDATE

    @classmethod
    def update_points(cls, id, attribute, value):
        query_string = f"""UPDATE points SET {attribute} = %s WHERE id = %s"""
        cursor.execute(query_string, (value, id,))
        db.commit()

    ####################################################################################################################
    # DELETE

    @classmethod
    def delete_points(cls, id):
        cursor.execute("""DELETE FROM points where id = %s""", (id, ))
        db.commit()

    ####################################################################################################################
    # JSON CONVERSION

    @classmethod
    def get_all_points_json(cls):
        all_points = Points.get_all_points()
        points_json = {
            'results': [

            ]
        }
        for point in all_points:
            point_data = Points.get_points_dict(point)
            points_json['results'].append(point_data)

        points_json = json.dumps(points_json)
        return points_json

    @classmethod
    def get_points_json(cls, id):
        points = Points.get_points(id)
        points_data = Points.get_points_dict(points)
        points_json = json.dumps(points_data)
        return points_json

    @classmethod
    def get_points_dict(cls, points):
        points_data = {
            'id': points.id,
            'user_id': points.user_id,
            'points': points.points,
            'reason': points.reason,
            'date_created': points.date_created.isoformat(),
        }
        return points_data

    @classmethod
    def create_points_from_json(cls, points_json):
        user_id = points_json['user_id']
        points = points_json['points']
        reason = points_json['reason']
        date_created = points_json['date_created']
        Points.insert_points_into_database(user_id, points, reason, date_created)


if __name__ == "__main__":
    for point in Points.get_all_points():
        print(point)
