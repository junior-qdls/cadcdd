import itertools
import numpy as np
import math
import functools
import numbers
from random import random
import json


def do_reduce(clusters, poi):
    index = poi["k"]
    poi.pop("k")
    poi.pop("x")
    poi.pop("y")
    clusters[index].append(poi)
    return clusters


def group_places_by_distance(total_days, places):
    # get all places id
    places_by_id = list(map(lambda place: place["place_id"], places))
    # create a numpy array with place's location as key
    arr = list(map(lambda poi: {**poi, "x": poi["x"], "y": poi["y"]}, places))

    # kmeans processing
    # kmeans = KMeans(n_clusters=total_days, random_state=0).fit(np_array)

    # labels = kmeans.labels_.tolist()
    cluster = Kmeans(
        {
            "k": total_days,
            "runs": math.floor(-(-(len(places_by_id) / total_days + 1) + 1)),
            "equalize": True,
            "normalize": False,
        }
    )

    cluster.calc(arr)

    # clustered_places_sorted = sorted(
    #    zip(places_by_id, labels), key=lambda x: x[1]
    # )
    reduced_cluster = functools.reduce(
        do_reduce, arr, [[] for _ in range(0, total_days)]
    )

    for cluster in reduced_cluster:
        cluster.sort(
            key=functools.cmp_to_key(lambda a, b: b["rating"] - a["rating"])
        )

    return reduced_cluster


def __permute(_input, perm_arr, used_chars):
    i, ch = 0, 0
    for i in range(0, len(_input)):
        del _input[i, i + 1][0]
        used_chars.append(ch)
        if len(_input) == 0:
            perm_arr.append(used_chars)
        __permute(_input, perm_arr, used_chars)
        _input.insert(i, ch)
        used_chars.pop()
    return []


def __rad(x):
    return x * math.pi / 180


def __c_sort(d, e):
    if d < e:
        return -1
    elif d > e:
        return 1
    else:
        return 0


def __sort_by(a, b, c):
    c = [b(x) for x in a]
    return c.sort(functools.cmp_to_key(__c_sort()))


def __get_distance(p1, p2):
    R = 6378137
    dlat = __rad(p2["x"] - p1["x"])
    dlong = __rad(p2["y"] - p1["y"])
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        __rad(p1["x"])
    ) * math.cos(__rad[p2["x"]]) * math.sin(dlong / 2) * math.sin(dlong / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


def __create_matrix_of_distance(_input):
    array_of_distances = []
    for item_from in _input:
        distances = []
        for item_to in _input:
            distances.append(self.__get_distance(item_from, item_to))
        array_of_distances.append(distances)
    return array_of_distances


def __get_id(metas, _id):
    for i in range(0, len(metas)):
        if metas[i]["id"] == _id:
            return metas[i]
    return None


def __count(centroids):
    count = 0
    for prop in centroids["data"]:
        if prop in centroids["data"]:
            count += 1
    return count


def __count_transfers(transfers, k):
    transfer = transfers[k]
    count = 0
    for prop in transfer:
        if prop in transfer:
            count += 1
    return count


def __sort_by_preference(pref, meta):
    return pref.sort(
        functools.cmp_to_key(lambda a, b: meta.dists[a] - meta.dists[b])
    )


class Kmeans:
    def __init__(self, obj):
        self.ks = obj["k"]
        self.runs = obj["runs"]
        self.equalize = obj["equalize"]
        self.normalize = obj["normalize"]
        self.max_size = math.inf
        self.centroids = []
        self.ps = 0
        self.points = []
        self.metas = []

    def get_optimal_permutation(self, pickup, _input):
        input_with_index = list(
            {"index": index, **item} for index, item in enumerate(_input)
        )
        distances = __create_matrix_of_distance(input_with_index)
        permutations = __permute(input_with_index, [], [])
        return {}

    def calc(self, data):
        self.ps = len(data)
        self.max_size = (
            math.ceil(self.ps / self.ks) if self.equalize else math.inf
        )
        self.points = data

        if self.normalize:
            self.__do_normalize()

        result = []

        for run in range(0, self.runs):
            result.append({"centroids": [], "sum": math.inf})
            self.__kmeans_plus_plus()

            for k in range(0, self.ks):
                result[run]["centroids"].append(
                    {"x": self.centroids[k]["x"], "y": self.centroids[k]["y"]}
                )

            if self.equalize:
                self.__init_metas()
                self.__initial_assignment()
                self.__update_means()
                self.__refine_result()
            else:
                self.__kmeans()
            result[run]["sum"] = self.__diff_sum()

        result.sort(key=functools.cmp_to_key(lambda a, b: a["sum"] - b["sum"]))

        self.centroids = []

        for k in range(0, self.ks):
            centroid = {
                "x": result[0]["centroids"][k]["x"],
                "y": result[0]["centroids"][k]["y"],
                "k": k,
                "items": 0,
                "data": {},
                "count": lambda: __count(centroids=centroid),
            }
            self.centroids.append(centroid)

        if self.equalize:
            self.__init_metas()
            self.__initial_assignment()
            self.__update_means()
            self.__refine_result()
        else:
            self.__kmeans()

        return self.__diff_sum()

    def __do_normalize(self):
        self.points.sort(
            key=functools.cmp_to_key(lambda a, b: a["x"] - b["x"])
        )
        x_min = self.points[0]["x"]
        x_max = self.points[self.ps - 1]["x"]

        self.points.sort(
            key=functools.cmp_to_key(lambda a, b: a["y"] - b["y"])
        )

        y_min = self.points[0]["y"]
        y_max = self.points[self.ps - 1]["y"]

        for p in range(0, self.ps):
            self.points[p]["x"] = (self.points[p]["x"] - x_min) / (
                x_max - x_min
            )
            self.points[p]["y"] = (self.points[p]["y"] - y_min) / (
                y_max - y_min
            )

    def __init_metas(self):
        self.metas = []
        for p in range(0, self.ps):
            self.points[p]["k"] = -1
            meta = Meta(
                p,
                self.points[p],
                self.points[p]["x"],
                self.points[p]["y"],
                self.ks,
            )
            for k in range(0, self.ks):
                meta.dists[k] = self.__get_distance(meta, self.centroids[k])
                if k > 0:
                    if meta.dists[k] < meta.dists[meta.primary]:
                        meta.primary = k
                    elif meta.dists[k] > meta.dists[meta.secondary]:
                        meta.secondary = k
            self.metas.append(meta)

    def __kmeans_plus_plus(self):
        self.centroids = []
        D = []
        ntries = 2 + round(math.log(self.ks))

        p0 = self.points[math.floor(random() * self.ps)]

        centroid = {
            "x": p0["x"],
            "y": p0["y"],
            "k": 0,
            "items": 0,
            "data": {},
            "count": lambda: __count(self.centroid),
        }

        self.centroids.append(centroid)

        D = [
            math.pow(self.__get_distance(p0, self.points[i]), 2)
            for i in range(0, self.ps)
        ]

        D_sum = functools.reduce(lambda a, b: a + b, D)

        for k in range(1, self.ks):
            best_d_sum = -1
            best_idx = -1
            for i in range(0, ntries):
                rnd_val = math.floor(random() * D_sum)
                for n in range(0, self.ps):
                    if rnd_val <= D[n]:
                        break
                    else:
                        rnd_val -= D[n]

                tmp_d = []
                for m in range(0, self.ps):
                    cmp1 = D[m]
                    cmp2 = math.pow(
                        self.__get_distance(self.points[m], self.points[n]), 2
                    )
                    tmp_d.append(cmp2 if cmp1 > cmp2 else cmp1)

                tmp_d_sum = functools.reduce(lambda a, b: a + b, tmp_d)

                if best_d_sum < 0 or tmp_d_sum < best_d_sum:
                    best_d_sum = tmp_d_sum
                    best_idx = n

            D_sum = best_d_sum
            centroid = {
                "x": self.points[best_idx]["x"],
                "y": self.points[best_idx]["y"],
                "k": k,
                "items": 0,
                "data": {},
                "count": lambda: __count(centroid),
            }

            self.centroids.append(centroid)

            for i in range(0, self.ps):
                cmp1 = D[i]
                cmp2 = math.pow(
                    self.__get_distance(self.points[best_idx], self.points[i]),
                    2,
                )
                D[i] = cmp2 if cmp1 > cmp2 else cmp1

    def __update_means(self):
        for k in range(0, self.ks):
            centroid = self.centroids[k]
            sum_x = 0
            sum_y = 0
            for prop in centroid["data"]:
                if prop in centroid["data"]:
                    sum_x += centroid["data"][f"{ prop }"]["x"]
                    sum_y += centroid["data"][f"{ prop }"]["y"]

            if sum_x > 0 and sum_y > 0:
                centroid["x"] = sum_x / centroid["items"]
                centroid["y"] = sum_y / centroid["items"]

    def __update_distances(self):
        for id in range(0, len(self.metas)):
            c = self.metas[id]
            c.secondary = -1
            for k in range(0, self.ks):
                c.dists[k] = self.__get_distance(c, self.centroids[k])
                if c.primary != k:
                    if c.secondary < 0 or c.dists[k] < c.dists[c.secondary]:
                        c.secondary = k

    def __transfer(self, meta, dstnum):
        del self.centroids[meta.primary]["data"][f"{meta.id}"]
        self.centroids[meta.primary]["items"] -= 1

        self.centroids[dstnum]["data"][f"{ meta.id }"] = meta
        self.centroids[dstnum]["items"] += 1

        meta.primary = dstnum
        meta.item["x"] = dstnum

    def __initial_assignment(self):
        assigned = []

        for start in range(0, len(self.metas)):
            self.metas.sort(
                key=functools.cmp_to_key(
                    lambda c1, c2: c2.priority() - c1.priority()
                )
            )
            for _id in range(0, len(self.metas)):
                c = self.metas[_id]
                if c.id in assigned and assigned.index(c.id) >= 0:
                    _id += 1
                    continue

                centroid = self.centroids[c.primary]
                centroid["data"][f"{c.id}"] = self.__get_id(self.metas, c.id)
                c.item["k"] = c.primary
                assigned.append(c.id)
                centroid["items"] += 1
                start += 1
                _id += 1

                if centroid["items"] == self.max_size:
                    full = c.primary
                    for b in range(_id, len(self.metas)):
                        ca = self.metas[b]
                        if ca.primary == full:
                            for k in range(0, self.ks):
                                if (
                                    k == full
                                    or self.centroids[k]["items"]
                                    >= self.max_size
                                ):
                                    continue
                                if (
                                    ca.primary == full
                                    or ca.dists[k] < ca.dists[ca.primary]
                                ):
                                    ca.primary = k
                    break

    def __refine_result(self):
        max_iter = -1
        min_size = math.floor(self.ps / self.ks)
        max_size = math.ceil(self.ps / self.ks)
        preferences = [k for k in range(0, self.ks)]
        transfers = [{} for _ in range(0, self.ks)]

        iter = 0
        while max_iter <= 0 or iter < max_iter:
            self.__update_distances()
            self.metas.sort(
                key=functools.cmp_to_key(
                    lambda c1, c2: c1.priority() - c2.priority()
                )
            )

            active = 0
            for m in range(0, len(self.metas)):
                c = self.metas[m]
                source = self.centroids[c.primary]
                preferences = self.__sort_by_preference(preferences, c)
                transferred = False

                for k in range(0, self.ks):
                    if k == c.primary:
                        continue

                    dest = self.centroids[k]
                    others = transfers[k]

                    for other in others:
                        if other in others:
                            c2 = self.__get_id(self.metas, other)
                            if c.gain(k) + c2.gain(c.primary) > 0:
                                self.__transfer(c2, c.primary)
                                self.__transfer(c, k)
                                active += 2
                                transferred = True
                                del others[other]
                                break
                    if c.gain(k) > 0 and (
                        dest["items"] < self.max_size
                        and source["items"] > self.min_size
                    ):
                        self.__transfer(c, k)
                        active += 1
                        transferred = True
                        break
                if not transferred and (
                    c.dists[c.primary] > c.dists[c.secondary]
                ):
                    transfers[c.primary][c.id] = c

            for k in range(0, self.ks):
                transfers[k] = {}

            if active <= 0:
                break

            self.__update_means()

    def __diff_sum(self):
        sum = 0
        for p in range(0, self.ps):
            point = self.points[p]
            centroid = self.centroids[point["k"]]
            dif_x = math.pow(point["x"] - centroid["x"], 2)
            dif_y = math.pow(point["y"] - centroid["y"], 2)
            sum += dif_x + dif_y
        return sum

    def __kmeans(self):
        converged = False
        while not converged:
            i = 0
            converged = True
            sums = [{"x": 0, "y": 0, "items": 0} for _ in self.ks]

            for p in range(0, self.ps):
                distances = __sort_by(
                    self.centroids,
                    lambda centroid: self.__get_distance(
                        centroid, self.points[p]
                    ),
                )
                print(f"distances = {distances}")

                closestItem = distances[0]
                k = closestItem["k"]

                if (
                    not isinstance(self.points[p]["k"], numbers.Number)
                    or self.points[p]["k"] != k
                ):
                    converged = False
                self.points[p]["k"] = k
                sums[k]["x"] += self.points[p]["x"]
                sums[k]["y"] += self.points[p]["y"]
                sums[k]["items"] += 1

            for k in range(0, self.ks):
                if sums[k]["items"] > 0:
                    self.centroids[k]["x"] = sums[k]["x"] / sums[k]["items"]
                    self.centroids[k]["y"] = sums[k]["y"] / sums[k]["items"]
                self.centroids[k]["items"] = sums[k]["items"]

    def __permute(_input, perm_arr, used_chars):
        i, ch = 0, 0
        for i in range(0, len(_input)):
            del _input[i, i + 1][0]
            used_chars.append(ch)
            if len(_input) == 0:
                perm_arr.append(used_chars)
            __permute(_input, perm_arr, used_chars)
            _input.insert(i, ch)
            used_chars.pop()
        return []

    def __rad(self, x):
        return x * math.pi / 180

    def __c_sort(self, d, e):
        if d < e:
            return -1
        elif d > e:
            return 1
        else:
            return 0

    def __sort_by(self, a, b, c):
        c = [b(x) for x in a]
        return c.sort(key=functools.cmp_to_key(self.__c_sort()))

    def __get_distance(self, p1, p2):
        R = 6378137
        dlat = self.__rad(p2["x"] - p1["x"])
        dlong = self.__rad(p2["y"] - p1["y"])
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
            self.__rad(p1["x"])
        ) * math.cos(self.__rad(p2["x"])) * math.sin(dlong / 2) * math.sin(
            dlong / 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d

    def __create_matrix_of_distance(self, _input):
        array_of_distances = []
        for item_from in _input:
            distances = []
            for item_to in _input:
                distances.append(self.__get_distance(item_from, item_to))
            array_of_distances.append(distances)
        return array_of_distances

    def __get_id(self, metas, _id):
        for i in range(0, len(metas)):
            if metas[i]["id"] == _id:
                return metas[i]
        return None

    def __count(self, centroids):
        count = 0
        for prop in centroids["data"]:
            if prop in centroids["data"]:
                count += 1
        return count

    def __count_transfers(self, transfers, k):
        transfer = transfers[k]
        count = 0
        for prop in transfer:
            if prop in transfer:
                count += 1
        return count

    def __sort_by_preference(self, pref, meta):
        pref.sort(
            key=functools.cmp_to_key(
                lambda a, b: meta.dists[a] - meta.dists[b]
            )
        )
        return pref


class Meta:
    def __init__(self, _id, item, x, y, ks):
        self.id = _id
        self.item = item
        self.x = x
        self.y = y
        self.dists = []
        self.dists = list(math.inf for _ in range(0, ks))
        self.primary = 0
        self.secondary = 0

    def priority(self):
        return self.dists[self.secondary] - self.dists[self.primary]

    def gain(self, k):
        return self.dists[self.primary] - self.dists[k]

    def __getitem__(self, k):
        return getattr(self, k)


if __name__ == "__main__":
    k = 3
    size = 6
    vectors = [
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1813713, "lng": -78.4842769},
                "viewport": {
                    "northeast": {
                        "lat": -0.1799286701072778,
                        "lng": -78.48189249999999,
                    },
                    "southwest": {
                        "lat": -0.1826283298927222,
                        "lng": -78.48507169999999,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque La Carolina.",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 1287,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/100514919223717872928">J. Michael Seyfert</a>'
                    ],
                    "photo_reference": "CmRaAAAAwjIUobV_1ol8NDJ2lrFInylb4CCiu0ThtOPPSDm_T3cNLTxL5pF-fPow6RtDvv4skCJ8M-hA9_3uXMMTFtXHlXZ1NXbByk70zsk8bL2yYcuwyHktARD_g57tOmHl2J9sEhDIE7URnkbr2qAxvhX56OgTGhRcZP9_j_RwLi3nNYkXut9dgpjE5w",
                    "width": 1980,
                }
            ],
            "place_id": "ChIJfVNWrIea1ZERE632s71GslY",
            "plus_code": {
                "compound_code": "RG98+F7 Quito",
                "global_code": "67F3RG98+F7",
            },
            "rating": 4.5,
            "reference": "ChIJfVNWrIea1ZERE632s71GslY",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 32060,
            "vicinity": "Av. de los Shyris, Quito",
            "x": -0.1813713,
            "y": -78.4842769,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1968675, "lng": -78.4726878},
                "viewport": {
                    "northeast": {
                        "lat": -0.1950655201072778,
                        "lng": -78.47114537010728,
                    },
                    "southwest": {
                        "lat": -0.1977651798927222,
                        "lng": -78.47384502989273,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Guápulo",
            "opening_hours": {"open_now": False},
            "photos": [
                {
                    "height": 3456,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/115262518655189606810">john garcia</a>'
                    ],
                    "photo_reference": "CmRaAAAAx0VwBPyJTcTSs08CIf8dflsNW2Azwtc-Nx3okKDCGLcM7lFk64F6pVvUTiQBvdKjTwzplLMosNyNpEul8M5LY7mIyUD2vmtd4DuDaI7W8c4H-yhhCaBxQEfZq6Ih-z2SEhDhPuu31HKnqWsf6AKZolO5GhT4sjt8IdpdsSdeLl9LEf0FR1MLEQ",
                    "width": 5184,
                }
            ],
            "place_id": "ChIJGUq4e56Q1ZERdH0rLAWfd80",
            "plus_code": {
                "compound_code": "RG3G+7W Quito",
                "global_code": "67F3RG3G+7W",
            },
            "rating": 4.6,
            "reference": "ChIJGUq4e56Q1ZERdH0rLAWfd80",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 1919,
            "vicinity": "Av. de los Conquistadores, Quito",
            "x": -0.1968675,
            "y": -78.4726878,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2091555, "lng": -78.498611},
                "viewport": {
                    "northeast": {
                        "lat": -0.2078056701072778,
                        "lng": -78.49726117010727,
                    },
                    "southwest": {
                        "lat": -0.2105053298927222,
                        "lng": -78.49996082989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque El Ejido",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3456,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/107344361996438833346">Ivonne Mendoza</a>'
                    ],
                    "photo_reference": "CmRaAAAA548EaJW0D2JfqAATd-0zeZWZ_YJnz2bLC8qseWCa5205JJiFePBCNjkB2ndXpI7yOho-UBaks5d1GDYrlQeJdQhh-gU5Zm1mjmCnSR81Rbp49vS4PXSOG8PaDHc6FoO6EhCX65rb8TVss8Isix0-i4q3GhThDH_gm-ZOD9juPn3Nqx3pyW3wOA",
                    "width": 4608,
                }
            ],
            "place_id": "ChIJm1GbfD2a1ZERHKCj5t2so6M",
            "plus_code": {
                "compound_code": "QGR2+8H Quito",
                "global_code": "67F3QGR2+8H",
            },
            "rating": 4.1,
            "reference": "ChIJm1GbfD2a1ZERHKCj5t2so6M",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 16298,
            "vicinity": "Quito",
            "x": -0.2091555,
            "y": -78.498611,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2146667, "lng": -78.5024237},
                "viewport": {
                    "northeast": {
                        "lat": -0.2137552701072778,
                        "lng": -78.50089917010727,
                    },
                    "southwest": {
                        "lat": -0.2164549298927222,
                        "lng": -78.50359882989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque La Alameda",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/102150273419924371412">A Google User</a>'
                    ],
                    "photo_reference": "CmRZAAAAUcVFPtqsjgqFRJTTIV7bxJDgyJ4vATfsu74vePDtrMlGeEy6d-l4XzVQRorsLGTOTyJY-IsEETL4oQID7FuvdWg1AaQl3f5t2B-jsCkVVLwnvHMee5xyJcKnty-z96WUEhBZZcoVJM71Oin9kqapv6_KGhQCYLoBVsGjh8aL862sT0RjZShz9g",
                    "width": 4032,
                }
            ],
            "place_id": "ChIJ11Ju5iOa1ZER4qOyQTtGyVk",
            "plus_code": {
                "compound_code": "QFPX+42 Quito",
                "global_code": "67F3QFPX+42",
            },
            "rating": 4.2,
            "reference": "ChIJ11Ju5iOa1ZER4qOyQTtGyVk",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 4100,
            "vicinity": "Av. Gran Colombia 242, Quito",
            "x": -0.2146667,
            "y": -78.5024237,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1823707, "lng": -78.4740633},
                "viewport": {
                    "northeast": {
                        "lat": -0.1811297701072778,
                        "lng": -78.47267937010727,
                    },
                    "southwest": {
                        "lat": -0.1838294298927222,
                        "lng": -78.47537902989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque México",
            "photos": [
                {
                    "height": 2322,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/105873263832552801561">A Google User</a>'
                    ],
                    "photo_reference": "CmRaAAAAKgvhrvdkDPqBwjcfIIUpO3cGvO_Qn3hpFtVoGg3-GNGY1SGoIFw6djx32dOrA-1WYkkTNc3AmPqnQkE6iHbf9OHbRifHJXXumU-ZHV72dysmtPtf59ndhiSnVuaO4sSNEhCm0Btq3_xM0dlEQsGa_ziUGhT2wTPKRa3Pe5mw25cutP5QYk0Sjw",
                    "width": 4128,
                }
            ],
            "place_id": "ChIJt6Dp7X-Q1ZERlnBLXm0ivdQ",
            "plus_code": {
                "compound_code": "RG9G+39 Quito",
                "global_code": "67F3RG9G+39",
            },
            "rating": 4.5,
            "reference": "ChIJt6Dp7X-Q1ZERlnBLXm0ivdQ",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 315,
            "vicinity": "Quito",
            "x": -0.1823707,
            "y": -78.4740633,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2264807, "lng": -78.5050626},
                "viewport": {
                    "northeast": {
                        "lat": -0.2251712701072778,
                        "lng": -78.50377712010729,
                    },
                    "southwest": {
                        "lat": -0.2278709298927223,
                        "lng": -78.50647677989274,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque La Tola",
            "place_id": "ChIJXdIw846Z1ZERPxQ9GiSpEK0",
            "plus_code": {
                "compound_code": "QFFV+CX Quito",
                "global_code": "67F3QFFV+CX",
            },
            "rating": 0,
            "reference": "ChIJXdIw846Z1ZERPxQ9GiSpEK0",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 0,
            "vicinity": "Calle, Ramon Miño S/N, Quito",
            "x": -0.2264807,
            "y": -78.5050626,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2164616, "lng": -78.4891136},
                "viewport": {
                    "northeast": {
                        "lat": -0.2150881201072778,
                        "lng": -78.48785937010727,
                    },
                    "southwest": {
                        "lat": -0.2177877798927222,
                        "lng": -78.49055902989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque barrial",
            "photos": [
                {
                    "height": 2160,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/107785744844725617513">Luis Carlos Aguirre</a>'
                    ],
                    "photo_reference": "CmRZAAAA8_LqgvWnO2pjFdFUlNrDTIHybbqXS4MFbeDDx-_0Jdx8Q7P43IN6YV1HUcD2wu6XmdTNxzBKZln2H_S-SBTno4cT8JUzNGSjVCLMoxUdi0ULJ677OgxjuebNqiwdJT4xEhBSTbnsSWkAPMrubKYALQIJGhQlrCcML_6X3k8L4TAURiy6v68rrw",
                    "width": 3840,
                }
            ],
            "place_id": "ChIJUYOujBya1ZERqdYIn7sxVcw",
            "plus_code": {
                "compound_code": "QGM6+C9 Quito",
                "global_code": "67F3QGM6+C9",
            },
            "rating": 3.9,
            "reference": "ChIJUYOujBya1ZERqdYIn7sxVcw",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 265,
            "vicinity": "Luis Godin, Quito",
            "x": -0.2164616,
            "y": -78.4891136,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.231169, "lng": -78.5060922},
                "viewport": {
                    "northeast": {
                        "lat": -0.2295450201072777,
                        "lng": -78.50510192010728,
                    },
                    "southwest": {
                        "lat": -0.2322446798927222,
                        "lng": -78.50780157989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque El Sena",
            "photos": [
                {
                    "height": 1536,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/110869835611723547848">Krishna Kant Kaushal</a>'
                    ],
                    "photo_reference": "CmRaAAAAWg0LxBCDFAlHMWXRyl_q9a8aZuF0E0AWZhk5Y9-EWpQP5YnSVhB8T39l_k4KA5qjvEapYScYNvQ5p1CXacXjM6l2GS-7mZlDapNv079v20Si8Wdb7MEyw6RSFdlT91pMEhAZZa-oWC819DdUjkfVvHnqGhQea3_1lUnGRJhnHEtTFcjk5tpHeA",
                    "width": 2048,
                }
            ],
            "place_id": "ChIJ_2eWV5CZ1ZERFMbTqxeENfA",
            "plus_code": {
                "compound_code": "QF9V+GH Quito",
                "global_code": "67F3QF9V+GH",
            },
            "rating": 3.8,
            "reference": "ChIJ_2eWV5CZ1ZERFMbTqxeENfA",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 68,
            "vicinity": "Piedra, Quito",
            "x": -0.231169,
            "y": -78.5060922,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2223173, "lng": -78.49909889999999},
                "viewport": {
                    "northeast": {
                        "lat": -0.2209674701072778,
                        "lng": -78.49774907010728,
                    },
                    "southwest": {
                        "lat": -0.2236671298927222,
                        "lng": -78.50044872989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Itchimbía",
            "opening_hours": {"open_now": False},
            "photos": [
                {
                    "height": 3120,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/112626973795559245441">Francis Peña</a>'
                    ],
                    "photo_reference": "CmRaAAAA1XzAnaK5_loAhZyWvyBPvCXWLSbbiZL_AqTUmSZSNPUL9sBiUrAskTEspQdnmGuBTRkl3xrXT7mBax1VFMfWDoxFXWz7sprHselOjqMnjRNr9lY6rZ1AgZMs0z43YVFKEhCSVJqoGNe5yJxauJj5eiR0GhQj4JDvCpA5Lx3xx9EtSQY7Xt82wQ",
                    "width": 4160,
                }
            ],
            "place_id": "ChIJrXGUIIuZ1ZER3pr6zhCXFlg",
            "plus_code": {
                "compound_code": "QGH2+39 Quito",
                "global_code": "67F3QGH2+39",
            },
            "rating": 4.6,
            "reference": "ChIJrXGUIIuZ1ZER3pr6zhCXFlg",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 5059,
            "vicinity": "Quito",
            "x": -0.2223173,
            "y": -78.49909889999999,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1901699, "lng": -78.47111360000001},
                "viewport": {
                    "northeast": {
                        "lat": -0.1888839201072778,
                        "lng": -78.46977267010726,
                    },
                    "southwest": {
                        "lat": -0.1915835798927222,
                        "lng": -78.47247232989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Bellavista",
            "place_id": "ChIJZZ6XCYOQ1ZERW3k8QSUDP0w",
            "plus_code": {
                "compound_code": "RG5H+WH Quito",
                "global_code": "67F3RG5H+WH",
            },
            "rating": 4,
            "reference": "ChIJZZ6XCYOQ1ZERW3k8QSUDP0w",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 1,
            "vicinity": "Quito",
            "x": -0.1901699,
            "y": -78.47111360000001,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1823272, "lng": -78.473255},
                "viewport": {
                    "northeast": {
                        "lat": -0.1809586701072778,
                        "lng": -78.47197502010728,
                    },
                    "southwest": {
                        "lat": -0.1836583298927222,
                        "lng": -78.47467467989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Guangüiltagua",
            "photos": [
                {
                    "height": 3456,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/104990536095009692694">Daysi Dominguez</a>'
                    ],
                    "photo_reference": "CmRaAAAABhFxI4cuPFmHzof6LGxJ06P0FUrRv24SgsfRlV_36OWZWgxAGW3xFSLqxzNfDx9HgHGbRBIfsWfGQod-4rMA7ggQ3fVpExKtjOG_ePcYd_VDmSPNL1cx5sGO_0_tUti7EhCRqPu8Go4hzFoYYy1Ln-_EGhTgG6HXoDV92kHz1i3uR6HOpwe5qA",
                    "width": 4608,
                }
            ],
            "place_id": "ChIJKR4Ww3-Q1ZERUkpea2pkR8c",
            "plus_code": {
                "compound_code": "RG9G+3M Quito",
                "global_code": "67F3RG9G+3M",
            },
            "rating": 4.4,
            "reference": "ChIJKR4Ww3-Q1ZERUkpea2pkR8c",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 50,
            "vicinity": "Guanguiltagua, Quito",
            "x": -0.1823272,
            "y": -78.473255,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2061903, "lng": -78.5086709},
                "viewport": {
                    "northeast": {
                        "lat": -0.2048013201072778,
                        "lng": -78.50731902010727,
                    },
                    "southwest": {
                        "lat": -0.2075009798927222,
                        "lng": -78.51001867989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Neon",
            "photos": [
                {
                    "height": 3096,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/108693630564904553254">jessi toledo</a>'
                    ],
                    "photo_reference": "CmRaAAAAb2MlFuiM7bLjs5PvFuAbjXRtcu12-v3nXn9PxJsuvUEZU2DMYKOfVd0Poq_GxH_hLIjrn1xrHedGCFCWXtMWAk0JFo6efnZJvPZ8GBGm0ltwHy27MzLhre6dPXBV8WQBEhAJ1LihWedPgIJ_o5dxv6jZGhStpGmuDhmhXP5vS4S4MXbMWP3wMQ",
                    "width": 4128,
                }
            ],
            "place_id": "ChIJA56fAjqa1ZERfPgFHGjxMtw",
            "plus_code": {
                "compound_code": "QFVR+GG Quito",
                "global_code": "67F3QFVR+GG",
            },
            "rating": 2.5,
            "reference": "ChIJA56fAjqa1ZERfPgFHGjxMtw",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 4,
            "vicinity": "Quito",
            "x": -0.2061903,
            "y": -78.5086709,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2054135, "lng": -78.4797336},
                "viewport": {
                    "northeast": {
                        "lat": -0.2041306201072778,
                        "lng": -78.47848237010727,
                    },
                    "southwest": {
                        "lat": -0.2068302798927222,
                        "lng": -78.48118202989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Feliz",
            "photos": [
                {
                    "height": 1920,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/117385772889189057257">Pato Medina</a>'
                    ],
                    "photo_reference": "CmRaAAAAapVBNFELn_3gFb7D-f8vCrCh1hM0VcAMe7rKRo0vI6GjR7c1bV7pK90puTgh0CgMQ2WIJkqMTDEl_q5H_2xdVnN3YemMwwyEO-QKXMY6bdgJZdbTm1bwgBu5nhu-mWDlEhBCRKETgwoA92ghh5MHCvrqGhRvoBe9fRt4KqcTT8J3jLEmTKG8UA",
                    "width": 1080,
                }
            ],
            "place_id": "ChIJ5bYu9ZKb1ZERwv9UGiCea1Q",
            "plus_code": {
                "compound_code": "QGVC+R4 Quito",
                "global_code": "67F3QGVC+R4",
            },
            "rating": 4.4,
            "reference": "ChIJ5bYu9ZKb1ZERwv9UGiCea1Q",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 45,
            "vicinity": "Quito",
            "x": -0.2054135,
            "y": -78.4797336,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1801565, "lng": -78.50046259999999},
                "viewport": {
                    "northeast": {
                        "lat": -0.1788066701072778,
                        "lng": -78.49911277010727,
                    },
                    "southwest": {
                        "lat": -0.1815063298927222,
                        "lng": -78.50181242989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Arqueológico Rumipamba",
            "opening_hours": {"open_now": False},
            "photos": [
                {
                    "height": 2988,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/111831443262021717744">Diana Lopez</a>'
                    ],
                    "photo_reference": "CmRaAAAAAoBwBc6IYcvD4j7A77KbpUepLEjrjMcxUgE7mtSXmpj3gLXpzttesLpb6i4-vF83q1nUlxDsuC1NX2S91eeP3WjgIXhqH-Ph32aKQmwMdzz3X4JIYlr4slb1ZQgLhWzwEhC9JMNp_38a_SRrGkMaP08gGhSRSKvXLSHpK_u5y3wZN34nXjmWVQ",
                    "width": 5312,
                }
            ],
            "place_id": "ChIJI9PFfPSa1ZERsa6L1Bhmx0E",
            "plus_code": {
                "compound_code": "RF9X+WR Quito",
                "global_code": "67F3RF9X+WR",
            },
            "rating": 4.5,
            "reference": "ChIJI9PFfPSa1ZERsa6L1Bhmx0E",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 1346,
            "vicinity": "Mañosca N35-86, Quito",
            "x": -0.1801565,
            "y": -78.50046259999999,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1847318, "lng": -78.48486299999999},
                "viewport": {
                    "northeast": {
                        "lat": -0.1833819701072778,
                        "lng": -78.48351317010727,
                    },
                    "southwest": {
                        "lat": -0.1860816298927222,
                        "lng": -78.48621282989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque La Carolina",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 2160,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/101705489112750848624">Luis Rivero</a>'
                    ],
                    "photo_reference": "CmRaAAAA7zZWy4Zu6U8hIeztcYzoBYxQbpnemrUIDkJhH2_cMjZZPuQQSLnqBctMeHAI5CsRKXAp7orw2Y2Q1vVm2ncDfL0yq16I2t8mg12bupUE-yFnsiN-GztFf69xsjJLkgyREhD9C7RJroRzb2ko0iBlcXPVGhSi2mSm3eUz9vK2Q2oS8KE3EvYEvg",
                    "width": 3840,
                }
            ],
            "place_id": "ChIJE3Ioinua1ZER70gk0EGwWGg",
            "plus_code": {
                "compound_code": "RG88+43 Quito",
                "global_code": "67F3RG88+43",
            },
            "rating": 4.5,
            "reference": "ChIJE3Ioinua1ZER70gk0EGwWGg",
            "scope": "GOOGLE",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment",
            ],
            "user_ratings_total": 3382,
            "vicinity": "Av. de los Shyris N35-174, Quito",
            "x": -0.1847318,
            "y": -78.48486299999999,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.194397, "lng": -78.5055094},
                "viewport": {
                    "northeast": {
                        "lat": -0.1930044201072778,
                        "lng": -78.50414052010727,
                    },
                    "southwest": {
                        "lat": -0.1957040798927222,
                        "lng": -78.50684017989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque",
            "place_id": "ChIJJTe0obub1ZERwN308Rte_FQ",
            "plus_code": {
                "compound_code": "RF4V+6Q Quito",
                "global_code": "67F3RF4V+6Q",
            },
            "rating": 0,
            "reference": "ChIJJTe0obub1ZERwN308Rte_FQ",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 0,
            "vicinity": "Núñez de Bonilla 478, Quito",
            "x": -0.194397,
            "y": -78.5055094,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2108737, "lng": -78.5070341},
                "viewport": {
                    "northeast": {
                        "lat": -0.2094529701072778,
                        "lng": -78.50572762010728,
                    },
                    "southwest": {
                        "lat": -0.2121526298927222,
                        "lng": -78.50842727989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Parkour - Jardín San Juan",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3120,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/112173933086975493684">Yue Grey</a>'
                    ],
                    "photo_reference": "CmRaAAAAfAYEnhmmsxq1B4agbOJDu_xq6ujt-M90S5ST2OdP1ADAbI3SS422Hp_HEYdgh3JSKxJP2vzTxWMXeGDlLptc9QCvndMPMylKjutswqECryhHYKsAK8euycCG3DPhDvjdEhAPKPAf0FwO9tyjBBWgt4dcGhSIDA_GGMeKYNHGH_uLjmdZdMK7Fw",
                    "width": 4160,
                }
            ],
            "place_id": "ChIJEzM8LSWa1ZEREePMDpFNQvQ",
            "plus_code": {
                "compound_code": "QFQV+M5 Quito",
                "global_code": "67F3QFQV+M5",
            },
            "rating": 4.2,
            "reference": "ChIJEzM8LSWa1ZEREePMDpFNQvQ",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 57,
            "vicinity": "La Habana, Quito",
            "x": -0.2108737,
            "y": -78.5070341,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1963792, "lng": -78.4731947},
                "viewport": {
                    "northeast": {
                        "lat": -0.1947157201072778,
                        "lng": -78.47161602010728,
                    },
                    "southwest": {
                        "lat": -0.1974153798927222,
                        "lng": -78.47431567989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Guápulo",
            "opening_hours": {"open_now": False},
            "photos": [
                {
                    "height": 3096,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/105764687682880533863">A Google User</a>'
                    ],
                    "photo_reference": "CmRaAAAA0-Dq02T_2Brip-1u63opcMoGGwNz72w9uw0-y0p2keNvbC9MR9QGAdK6G_UVed37KanDt-Oj1W_c2Pajbi2M_sC7m0WRhLI8ypQEr71TEykv0KFOk9OSXYa6V2JfljWIEhC5Z3JyBdH2ZhoNuOx5btR1GhQh7nmjK7qZGBzHPbgS0OMdpy0ecA",
                    "width": 4128,
                }
            ],
            "place_id": "ChIJOz3LWEiR1ZERVjbhTba9oFI",
            "plus_code": {
                "compound_code": "RG3G+CP Quito",
                "global_code": "67F3RG3G+CP",
            },
            "rating": 4.8,
            "reference": "ChIJOz3LWEiR1ZERVjbhTba9oFI",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 59,
            "vicinity": "Quito",
            "x": -0.1963792,
            "y": -78.4731947,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.2078563, "lng": -78.5052336},
                "viewport": {
                    "northeast": {
                        "lat": -0.2063315201072778,
                        "lng": -78.50382677010728,
                    },
                    "southwest": {
                        "lat": -0.2090311798927222,
                        "lng": -78.50652642989272,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque Benito Juárez",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3006,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/107856597465169492208">Diego Valenzuela</a>'
                    ],
                    "photo_reference": "CmRaAAAAQHdr7O21cpguG8-oX5JwaBRZgexa4xZZi2UH7xyMv4idT76cu9AG2uP9AlLDMAZ_GYVuW2Sd7M1qw03G5TzlOy-wvLY6eHMoZ96nGmrSi9Z0eyQv-evjNmZft1hp16MnEhBX-oZxr5xAHZ5fXKAAf_kEGhQKQ85Z1bMiIJRvl64KruZntOxq-g",
                    "width": 5344,
                }
            ],
            "place_id": "ChIJg7TbvDua1ZERioaLORWaZRI",
            "plus_code": {
                "compound_code": "QFRV+VW Quito",
                "global_code": "67F3QFRV+VW",
            },
            "rating": 4.2,
            "reference": "ChIJg7TbvDua1ZERioaLORWaZRI",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 773,
            "vicinity": "Bogotá, Quito",
            "x": -0.2078563,
            "y": -78.5052336,
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": -0.1801197, "lng": -78.48363049999999},
                "viewport": {
                    "northeast": {
                        "lat": -0.1792433201072778,
                        "lng": -78.48183807010727,
                    },
                    "southwest": {
                        "lat": -0.1819429798927222,
                        "lng": -78.48453772989271,
                    },
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_recreational-71.png",
            "name": "Parque La Carolina",
            "photos": [
                {
                    "height": 3120,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/102793201325026343198">Frank Leon</a>'
                    ],
                    "photo_reference": "CmRaAAAAJmVte5FoDpkwkfO5GBkmiwOZVdJqnqBkUb_G27isZNilo9shEbRDemsUS-aJDMmsuqzZCA8Zavc-t7rCWtbaWwyxJzqVU-_oCdha0id8YBrtp_FEHAMzu4v5wS8IYWbOEhBtIksht7LoNrlq0patMlq9GhQw3WNx4HLJSUIiRZkhBT_8DFDEXg",
                    "width": 4160,
                }
            ],
            "place_id": "ChIJqapTxnSQ1ZERmlFIq1XKWJE",
            "plus_code": {
                "compound_code": "RG98+XG Quito",
                "global_code": "67F3RG98+XG",
            },
            "rating": 4.5,
            "reference": "ChIJqapTxnSQ1ZERmlFIq1XKWJE",
            "scope": "GOOGLE",
            "types": ["park", "point_of_interest", "establishment"],
            "user_ratings_total": 227,
            "vicinity": "Quito",
            "x": -0.1801197,
            "y": -78.48363049999999,
        },
    ]

    cluster = Kmeans(
        {"k": k, "runs": size, "equalize": True, "normalize": False}
    )

    _sum = cluster.calc(vectors)
    print(f"{json.dumps(vectors)}")
