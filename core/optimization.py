from core.google_api import get_route
import random
import datetime as dt
import re
import copy
import math


# flake8: noqa E203
def apply_ga(
    pois,
    travel_date,
    travel_schedule={"start": "0900", "end": "1830"},
    lunch_time={"start": "1300", "end": "1400"},
    crossover_probability=0.33,
    mutation_probability=0.05,
):
    matrix = [[None for _ in pois]]
    routes = []
    for i in range(0, len(pois) - 1):
        matrix.append([None for _ in pois])
        for j in range(i + 1, len(pois)):
            routes.append(
                get_route(
                    f"place_id:{pois[i].get('place_id')}",
                    f"place_id:{pois[j].get('place_id')}",
                )
            )

    index = 0
    for i in range(0, len(pois) - 1):
        for j in range(i + 1, len(pois)):
            matrix[i][j] = routes[index]
            matrix[j][i] = routes[index]
            index += 1

    print("travel_date")
    print(travel_date)
    print("--")
    print("travel_schedule")
    print(travel_schedule)
    print("--")
    print("lunch_time")
    print(lunch_time)
    print("--")
    print("total_generations")
    print(len(pois) * 100)
    print("--")
    print("population_size")
    print(pow(len(pois), 2))
    print("--")
    print("mutation_probability")
    print(mutation_probability)
    print("--")
    print("crossover_probability")
    print(crossover_probability)
    print("--")
    ga = GeneticAlgorithm(
        pois=pois,
        time_matrix=matrix,
        travel_date=travel_date,
        travel_schedule=travel_schedule,
        lunch_time=lunch_time,
        total_generations=len(pois) * 100,
        population_size=pow(len(pois), 2),
        mutation_probability=mutation_probability,
        crossover_probability=crossover_probability,
    )

    tour = ga.evolve()
    index, result = next(
        (
            (index, item)
            for index, item in enumerate(tour)
            if int(item.get("schedule", {}).get("start", "0").replace(":", ""))
            >= int(travel_schedule["end"])
        ),
        (-1, None),
    )
    if index == -1:
        return tour
    else:
        new_tour = tour[0 : index + 1 if result["type"] == "poi" else index]
        return __finish_tour(new_tour, travel_schedule["end"])


def __finish_tour(new_tour, end_tour):
    limit = int(end_tour)
    start_poi = int(
        new_tour[-1].get("schedule", {}).get("start", 0).replace(":", "")
    )
    if start_poi > limit:
        last_route = new_tour[-2]
        new_tour = new_tour[0:-1]
        new_tour[-1]["schedule"]["end"] = last_route["schedule"]["end"]
    else:
        new_tour[-1]["schedule"]["end"] = f"{end_tour[:2]}:{end_tour[2:]}"
    return new_tour


def __format_date(date):
    return dt.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


class GeneticAlgorithm(object):
    populations = []

    def __init__(
        self,
        pois,
        time_matrix,
        travel_date,
        travel_schedule,
        lunch_time,
        total_generations,
        population_size,
        mutation_probability,
        crossover_probability=1 / 3,
    ):
        self.travel_schedule = travel_schedule
        self.total_generations = total_generations
        self.travel_date = travel_date
        self.pois = pois
        self.time_matrix = time_matrix
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.travel_date = self.__build_date_hour(
            self.travel_schedule["start"]
        )
        self.available_time = (
            self.__build_date_hour(self.travel_schedule["end"]).minute
            - self.travel_date.minute
        )
        self.lunch_time = {
            "start": self.__build_date_hour(lunch_time["start"]),
            "end": self.__build_date_hour(lunch_time["end"]),
        }
        self.__init_population(population_size)
        self.__sort()

    def evolve(self):
        for i in range(0, self.total_generations):
            self.__crossover(self.__selection())
            self.__mutation()
            self.__sort()
        return self.__build_itinerario(self.best_individual)

    def __build_itinerario(self, chromosome):
        had_lunch = False
        route = chromosome["route"]
        itinerary = []
        minutes_to_subtract = self.time_matrix[0][route[1]]["duration"]
        current_time = self.travel_date - dt.timedelta(
            minutes=minutes_to_subtract
        )
        itinerary.append({"type": "home", **self.pois[route[0]]})

        position = 0
        position, [obj, duration, next_event] = self.__get_event(
            "route", position, self.pois, route
        )

        while position < len(route) - 1:
            next_time = current_time + dt.timedelta(minutes=duration)
            c_lunch_time = chromosome.get("lunch_time")
            c_lunch_time_start = None
            if c_lunch_time:
                c_lunch_time_start = c_lunch_time.get("start")
            if c_lunch_time_start is None:
                c_lunch_time_start = self.travel_date + dt.timedelta(days=1)
            if not had_lunch and c_lunch_time_start < next_time:
                end_minute = chromosome["lunch_time"]["end"].minute
                start_minute = chromosome["lunch_time"]["start"].minute
                lunch_duration = end_minute - start_minute
                current_time, schedule = self.__get_schedule(
                    lunch_duration, current_time
                )
                itinerary.append(
                    {
                        "type": "lunch",
                        "duration": lunch_duration,
                        "schedule": schedule,
                    }
                )
                had_lunch = True

            current_time, schedule = self.__get_schedule(
                duration, current_time
            )
            itinerary.append({**obj, "schedule": schedule})
            position, [obj, duration, next_event] = self.__get_event(
                next_event, position, self.pois, route
            )

        current_time, schedule = self.__get_schedule(duration, current_time)
        itinerary.append({**obj, "schedule": schedule})
        position, [obj, duration, next_event] = self.__get_event(
            next_event, position, self.pois, route
        )

        current_time, schedule = self.__get_schedule(duration, current_time)
        itinerary.append({**obj, "schedule": schedule})
        return itinerary

    def __get_schedule(self, duration, current_time):
        start = current_time.strftime("%H:%M")
        end = current_time + dt.timedelta(minutes=duration)
        return end, {"start": start, "end": end.strftime("%H:%M")}

    def __get_event(self, current_event, position, pois, route):
        if current_event == "poi":
            poi = pois[route[position]]
            return (
                position,
                [{"type": "poi", **poi}, poi["expected_time"], "route"],
            )

        next_route = self.time_matrix[route[position]][route[position + 1]]
        position += 1

        return (
            position,
            [{"type": "route", **next_route}, next_route["duration"], "poi"],
        )

    def __crossover(self, parents):
        new_population = []
        while len(new_population) < len(self.populations):
            positions = self.__get_random_positions(2, 0, len(parents))
            parent1 = parents[positions[0]]
            parent2 = parents[positions[1]]
            for route in self.__crossover_parents(
                parent1["route"], parent2["route"]
            ):
                new_population.append(self.__create_chromosome(route))
        self.populations = new_population

    def __mutation(self):
        for individual in self.populations:
            if random.random() < self.mutation_probability:
                self.__mutate(individual)

    def __mutate(self, individual):
        route = individual["route"]
        positions = self.__get_random_positions(
            math.floor((len(route) - 1) / 2), 1, len(route) - 1
        )
        for p in range(0, len(positions) - 1, 2):
            aux = route[positions[p]]
            route[positions[p]] = route[positions[p + 1]]
            route[positions[p + 1]] = aux
        individual["lunch_time"] = None
        individual["fitness"] = self.__get_fitness(individual)

    def __crossover_parents(self, parent1, parent2):
        even, odd = self.__get_positions_and_maps(parent1, parent2)
        return [
            *self.__map_children(parent1, parent2, even[0], even[1]),
            *self.__map_children(parent1, parent2, odd[0], odd[1]),
        ]

    def __map_children(self, parent1, parent2, positions, maps):
        children = [
            [0 for _ in range(0, len(parent1))],
            [0 for _ in range(0, len(parent1))],
        ]
        for i in range(1, len(parent1)):
            if i in positions:
                children[0][i] = parent1[i]
                children[1][i] = parent2[i]
            else:
                try:
                    children[0][i] = maps[0][parent2[i]]
                except Exception:
                    children[0][i] = parent2[i]
                try:
                    children[1][i] = maps[1][parent1[i]]
                except Exception:
                    children[1][i] = parent1[i]

        return children

    def __get_positions_and_maps(self, parent1, parent2):
        even_positions = []
        odd_positions = []
        even_points = [[], []]
        odd_points = [[], []]

        for i in range(1, len(parent1), 2):
            even_points[0].append(parent1[i])
            even_points[1].append(parent2[i])
            even_positions.append(i)

            odd_points[0].append(
                parent1[i + 1] if i + 1 < len(parent1) else None
            )
            odd_points[1].append(
                parent2[i + 1] if i + 1 < len(parent2) else None
            )
            odd_positions.append(i + 1)

        last = len(odd_points[0]) - 1

        if odd_points[0][last] or odd_points[0][last] is None:
            del odd_points[0][last : last + 1]
            del odd_points[1][last : last + 1]
            del odd_positions[last : last + 1]

        return [
            [even_positions, self.__get_maps(even_points)],
            [odd_positions, self.__get_maps(odd_points)],
        ]

    def __get_maps(self, points):
        data1, data2 = points
        x = 0
        for i in range(0, len(data1)):
            try:
                index = data2.index(data1[x])
                data2[index] = data2[x]
                del data1[x : x + 1]
                del data2[x : x + 1]
                x -= 1
            except Exception:
                pass
            x += 1
        m1, m2 = {}, {}

        for i in range(0, len(data1)):
            m1[data1[i]] = data2[i]
            m2[data2[i]] = data1[i]
        return [m1, m2]

    def __selection(self):
        total = math.floor(len(self.populations) * self.crossover_probability)
        total = total if total % 2 == 0 else total + 1
        others = math.floor(total / 8)
        best = total - others
        cut_point = len(self.populations) - best
        random_elements = []
        positions = self.__get_random_positions(others, 0, cut_point)
        random_elements = [self.populations[i] for i in positions]
        result = [*random_elements, *self.populations[cut_point:]]
        return result

    def __init_population(self, size):
        self.populations = []
        total = len(self.pois) - 1

        for i in range(0, size):
            route = [0, *self.__get_random_positions(total, 1, total)]
            self.populations.append(self.__create_chromosome(route))

        first_route = [n for n in range(0, len(self.pois))]
        self.best_individual = self.__create_chromosome(first_route)

    def __sort(self):
        self.populations.sort(key=lambda t: t["fitness"], reverse=True)
        best = self.populations[-1]
        if best["fitness"] < self.best_individual["fitness"]:
            self.best_individual = best

    def __create_chromosome(self, route):
        chromosome = {"route": route, "lunch_time": None}
        return {"fitness": self.__get_fitness(chromosome), **chromosome}

    def __get_fitness(self, individual):
        route = individual["route"]
        lunch_time = individual["lunch_time"]
        travel_time = self.time_matrix[0][route[1]].get("duration")
        total = travel_time + self.pois[route[len(route) - 1]].get(
            "expected_time"
        )
        day_schedule = self.travel_date
        for i in range(1, len(route) - 1):

            travel_time = self.time_matrix[route[i]][route[i + 1]].get(
                "duration"
            )
            expected_time = self.pois[route[i]].get("expected_time")
            penalties = self.__calculate_penalties(
                day_schedule,
                self.pois[route[i]],
                self.time_matrix[route[i]][route[i - 1]].get("duration"),
            )
            day_schedule, spent1 = self.__addSpentTime(
                individual, day_schedule, expected_time
            )
            day_schedule, spent2 = self.__addSpentTime(
                individual, day_schedule, travel_time
            )
            total += spent1 + spent2 + expected_time + travel_time + penalties
        return abs(self.available_time - total)

    def __calculate_penalties(self, day, place, travel_time):
        date = self.travel_date
        open_time, close_time = "", ""
        try:
            open_time = self.__build_date_hour(
                place.get("opening_hours").get("periods")[day].get("open")
            )
            close_time = self.__build_date_hour(
                place.get("opening_hours").get("periods")[day].get("close")
            )
        except Exception:
            open_time = self.__build_date_hour(
                self.travel_schedule.get("start")
            )
            close_time = self.__build_date_hour(
                self.travel_schedule.get("end")
            )
        if not (open_time <= date < close_time):
            return (
                open_time.minute - date.minute
                if date.minute - open_time.minute
                else travel_time
            )
        else:
            return 0

    def __addSpentTime(self, individual, current_time, time_to_spend):
        lunch_time = 0
        if individual.get("lunch_time") is not None:
            current_time = current_time + dt.timedelta(minutes=time_to_spend)
        else:
            next_stop = copy.deepcopy(current_time)
            next_stop = next_stop + dt.timedelta(minutes=time_to_spend)
            if current_time <= self.lunch_time.get("start") <= next_stop:
                lunch_time = self.__have_lunch(
                    individual, current_time, next_stop
                )
            else:
                current_time = current_time + dt.timedelta(
                    minutes=time_to_spend
                )
        return current_time, lunch_time

    def __have_lunch(self, individual, current_date, next_date):
        invaded_time = None
        time_window = next_date.minute - current_date.minute
        lunch_time = (
            self.lunch_time.get("end").minute
            - self.lunch_time.get("start").minute
        )
        diff1 = abs(self.lunch_time.get("start").minute - current_date.minute)
        diff2 = abs(self.lunch_time.get("start").minute - next_date.minute)
        if diff1 < diff2:
            individual.update({"lunch_time": {"start": current_date}})
            current_date = current_date + dt.timedelta(minutes=lunch_time)
            individual["lunch_time"]["end"] = current_date
            current_date = current_date + dt.timedelta(minutes=time_window)
            invaded_time = diff1
        else:
            current_date = current_date + dt.timedelta(minutes=time_window)
            individual.update({"lunch_time": {"start": current_date}})
            current_date = current_date + dt.timedelta(minutes=lunch_time)
            individual["lunch_time"]["end"] = current_date
            invaded_time = diff2
        return lunch_time + invaded_time

    def __build_date_hour(self, time):
        h, m = re.findall(r"\d{2}", time)
        return self.travel_date.replace(hour=int(h), minute=int(m))

    def __get_random_positions(self, picked_numbers, start_number, max_number):
        random_numbers = [
            n for n in range(start_number, max_number + 1 + start_number - 1)
        ]
        result = random.sample(random_numbers, picked_numbers)
        if picked_numbers == 0:
            return []
        if picked_numbers == 1:
            return [*result]
        return result
