class Results:

    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):

    def number_of_wins(self):
        print(f"Футбольных побед: {self.victories}")

    def number_of_draws(self):
        print(f"Футбольных ничьих: {self.draws}")

    def number_of_losses(self):
        print(f"Футбольных поражений: {self.losses}")

    @classmethod
    def total_points(cls):
        print(f"Общее количество очков: {3*cls.victories + cls.draws}")


class Hockey(Results):

    def number_of_wins(self):
        print(f"Хоккейных побед: {self.victories}")

    def number_of_draws(self):
        print(f"Хоккейных ничьих: {self.draws}")

    def number_of_losses(self):
        print(f"Хоккейных поражений: {self.losses}")

    def total_points(self):
        print(f"Общее количество очков: {2*self.victories + self.draws}")


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    if team is football_team:
        team.number_of_wins()
    else:
        team.number_of_draws()

for team in (football_team, hockey_team):
    if team is football_team:
        team.number_of_losses()
    else:
        team.total_points()



