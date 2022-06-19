import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class Visualize:
    def __init__(self, r):
        fig = plt.figure(figsize=(10, 10))
        plt.axis('off')
        circle = plt.Circle((0, 0), r, color='red', fill=False)
        plt.gca().add_patch(circle)

    def createQuestionPoints(self, nr_of_questions):
        degrees_per_point = 360 / nr_of_questions
        deg_array = np.deg2rad(np.arange(0, 360, degrees_per_point)) # deg array of the points
        self.coord_of_points = np.zeros([nr_of_questions, 2])
        self.coord_of_points [:, 0] = np.cos(deg_array) # x-coords
        self.coord_of_points [:, 1] = np.sin(deg_array) # y-coords
        plt.plot(self.coord_of_points [:, 0], self.coord_of_points [:, 1], '.b')
    
    def createPartieBars(self):
        pass

df = pd.read_csv('Sweden_partie_program_opinions_2022.csv', sep=';', skiprows=1)
df = df.set_index('Fråga') # sätt frågorna som radindex
print(df.loc['Skatt']) # få ut en specifik fråga

r = 1 # radie
visualization = Visualize(r)
visualization.createQuestionPoints(100)

# plt.show()
