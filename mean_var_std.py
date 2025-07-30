import numpy as np

def calculate(list):
    # Check list length is valid (must be 3x3 in this case)
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 matrix
    array = np.array([list[0:3], list[3:6], list[6:]])

    # Mean
    mean_c = np.mean(array, 0)
    mean_r = np.mean(array, 1)
    mean_t = np.mean(array)

    # Variance
    variance_c = np.var(array, 0)
    variance_r = np.var(array, 1)
    variance_t = np.var(array)

    # Standard Deviation
    std_c = np.std(array, 0)
    std_r = np.std(array, 1)
    std_t = np.std(array)

    # Max
    max_c = np.max(array, 0)
    max_r = np.max(array, 1)
    max_t = np.max(array)

    # Min
    min_c = np.min(array, 0)
    min_r = np.min(array, 1)
    min_t = np.min(array)

    # Sum
    sum_c = np.sum(array, 0)
    sum_r = np.sum(array, 1)
    sum_t = np.sum(array)

    calculations = {
        "mean": [mean_c, mean_r, mean_t],
        "variance": [variance_c, variance_r, variance_t],
        "standard deviation": [std_c, std_r, std_t],
        "max": [max_c, max_r, max_t],
        "min": [min_c, min_r, min_t],
        "sum": [sum_c, sum_r, sum_t],
    }

    return calculations