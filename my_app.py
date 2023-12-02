import numpy as np
import matplotlib.pyplot as plt

def ruffeux_test(heart_rate_data):
    n = len(heart_rate_data)
    heart_rate_sum = sum(heart_rate_data) 
    heart_rate_average = heart_rate_sum / n

    resting_heart_rate = heart_rate_average / 10
    work_heart_rate1 = resting_heart_rate + 15
    work_heart_rate2 = resting_heart_rate + 30

    workout_heart_rate_1 = np.zeros(n)
    workout_heart_rate_2 = np.zeros(n) 

    for i in range(n):
        workout_heart_rate_1[i] = max(0, heart_rate_data[i] - resting_heart_rate
