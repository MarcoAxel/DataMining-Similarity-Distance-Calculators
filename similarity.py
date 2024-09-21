import numpy as np

def smc_similarity(set1, set2):
    # Calculate the Simple Matching Coefficient (SMC) similarity
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def jaccard_similarity(set1, set2):
    # Calculate the Jaccard Similarity
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def cosine_similarity(vector1, vector2):
    # Calculate the Cosine Similarity
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    return dot_product / (norm_vector1 * norm_vector2)

# Example usage:

# SMC and Jaccard similarity for sets
set1 = set([1, 2, 3, 4, 5])
set2 = set([3, 4, 5, 6, 7])
smc_result = smc_similarity(set1, set2)
jaccard_result = jaccard_similarity(set1, set2)

print(f"SMC Similarity: {smc_result}")
print(f"Jaccard Similarity: {jaccard_result}")

# Cosine similarity for vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
cosine_result = cosine_similarity(vector1, vector2)

print(f"Cosine Similarity: {cosine_result}")
