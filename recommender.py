import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances


def get_recommendation(hhkey):
    return [hhkey + 4, hhkey // 2, hhkey]
