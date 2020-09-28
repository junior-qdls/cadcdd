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
