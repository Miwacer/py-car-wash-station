from inspect import cleandoc


class Car:
    def __init__(self, comfort_class: int,clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: any, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: int) -> int:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car) -> int:
        price = car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1)
                                     + new_rating) / self.count_of_ratings, 1)
        return self.average_rating, 1