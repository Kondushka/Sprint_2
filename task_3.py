# тут можно сделать через global points и global total
# или сделать локально через __init__
# Но все работает и без этого, так что я решила упростить код :)


class PointsForPlace:

    @staticmethod
    def get_points_for_place(place: int):
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
            return 0
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
            return 0
        else:
            return 101 - place


class PointsForMeters:

    @staticmethod
    def get_points_for_meters(meters: int):
        if meters < 0:
            print("Количество метров не может быть отрицательным")
            return 0
        else:
            return meters * 0.5


class TotalPoints(PointsForPlace, PointsForMeters):

    def get_total_points(self, place, meters):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(10, 10))
