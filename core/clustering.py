import itertools
import numpy as np

from sklearn.cluster import KMeans


def group_places_by_distance(total_days, places):

    # get all places id
    places_by_id = list(map(lambda place: place["place_id"], places))
    # create a numpy array with place's location as key
    np_array = np.array(list(map(lambda poi: [poi["x"], poi["y"]], places)))

    # kmeans processing
    kmeans = KMeans(n_clusters=total_days, random_state=0).fit(np_array)

    labels = kmeans.labels_.tolist()

    clustered_places_sorted = sorted(
        zip(places_by_id, labels), key=lambda x: x[1]
    )

    return list(
        [place[0] for place in group]
        for key, group in itertools.groupby(
            clustered_places_sorted, lambda cps: cps[1],
        )
    )
