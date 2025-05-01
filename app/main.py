class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    pass


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        count_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                income = self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
                count_income += income
        return round(count_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost_of_one = (car.comfort_class * (self.clean_power - car.clean_mark)
                       * self.average_rating / self.distance_from_city_center)
        return round(cost_of_one, 1)

    def wash_single_car(self, car: list[Car]) -> float:
        if car.clean_mark == self.clean_power:
            result = self.serve_cars(car)
            car.clean_mark = self.clean_power
            return result

    def rate_service(self, number: int) -> None:
        if number:
            self.average_rating = round(
                (self.average_rating * self.count_of_ratings + number)
                / (self.count_of_ratings + 1),
                1)
            self.count_of_ratings += 1

    pass
