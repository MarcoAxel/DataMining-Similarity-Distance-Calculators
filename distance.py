import numpy as np
from scipy.spatial.distance import cityblock, euclidean, chebyshev, mahalanobis

# Define two vectors as numpy arrays
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# City Block Distance (Manhattan Distance)
city_block_distance = cityblock(vector1, vector2)

# Euclidean Distance
euclidean_distance = euclidean(vector1, vector2)

# Lmax Distance (Chebyshev Distance)
lmax_distance = chebyshev(vector1, vector2)

# Mahalanobis Distance
# Define a covariance matrix (you may need to adjust this based on your specific data)
cov_matrix = np.array([[1, 0.5, 0.3],
                       [0.5, 2, 0.2],
                       [0.3, 0.2, 3]])
# Calculate the Mahalanobis distance
mahalanobis_distance = mahalanobis(vector1, vector2, np.linalg.inv(cov_matrix))

# Print the results
print(f"City Block Distance: {city_block_distance}")
print(f"Euclidean Distance: {euclidean_distance}")
print(f"Lmax Distance: {lmax_distance}")
print(f"Mahalanobis Distance: {mahalanobis_distance}")
