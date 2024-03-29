import numpy as np
import re
import textdistance
import sklearn
from sklearn.cluster import AgglomerativeClustering
data=['reliance supermarket','bigbasket','star bazaar','big bazaar','mumbai vadapav','mumbai local','reliance jio','reliance gold','reliance capital','tata capital','jio mart','D Mart','7738','7773','9820','9821','5430']
print(data)
def normalize(data):
	return re.sub('[^a-z0-9]+','',data.lower())
def group_texts(data,threshold=0.4):
    normalized_texts=np.array([normalize(text) for text in data])
    distances=1-np.array([[textdistance.jaro_winkler(one,another) for one in normalized_texts] for another in normalized_texts])
    clustering=AgglomerativeClustering(distance_threshold=threshold,affinity="precomputed",linkage="complete",n_clusters=None).fit(distances)
    centers=dict()
    for cluster_id in set(clustering.labels_):
        index=clustering.labels_==cluster_id
        centrality=distances[:,index ][index].sum(axis=1)
        centers[cluster_id]=normalized_texts[index][centrality.argmin()]
    return [centers[i] for i in clustering.labels_]
print(group_texts(data))