import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

class Visualize:
    def __init__(self, r):
        fig = plt.figure(figsize=(10, 10))
        plt.axis('off')
        circle = plt.Circle((0, 0), r, color='red', fill=False)
        plt.gca().add_patch(circle)

    def createQuestionPoints(self, nr_of_questions):
        degrees_per_point = 360 / nr_of_questions
        self.deg_array = np.deg2rad(np.arange(0, 360, degrees_per_point)) # deg array of the points
        self.coord_of_points = np.zeros([nr_of_questions, 2])
        self.coord_of_points [:, 0] = np.cos(self.deg_array) # x-coords
        self.coord_of_points [:, 1] = np.sin(self.deg_array) # y-coords
        plt.plot(self.coord_of_points[:, 0], self.coord_of_points[:, 1], '.b')
    
    def createPartieBars(self, max_score):
        counter = 0
        for idx, question in df.iterrows():
            print(question.name)
            for index, partie in enumerate(df.columns):
                x = self.coord_of_points[counter, 0]*(1 + question[df.columns[index]] / max_score)
                y = self.coord_of_points[counter, 1]*(1 + question[df.columns[index]] / max_score)
                plt.plot([self.coord_of_points[counter, 0], x], [self.coord_of_points[counter, 1], y], color=color_list[index])
                plt.text(x, y, partie, fontsize=5*r)
            plt.plot([self.coord_of_points[counter, 0], 2*self.coord_of_points[counter, 0]], [self.coord_of_points[counter, 1], 2*self.coord_of_points[counter, 1]], '--k', alpha=0.5, markersize=1)
            plt.text(2*self.coord_of_points[counter, 0], 2*self.coord_of_points[counter, 1], question.name, fontsize=7*r, rotation=90, verticalalignment='center')
            counter += 1

df = pd.read_csv('Sweden_partie_program_opinions_2022.csv', sep=';', skiprows=1)
df = df.set_index(df.columns[0]) # sätt frågorna som radindex
#print(df.loc['Skatt']) # få ut en specifik fråga

max_score = 10 # maximum value for a question in the table
r = 1 # radie
color_list = ['#009933', '#000077', '#006AB3', '#83CF39', '#52BDEC', '#E8112d', '#DDDD00', '#DA291C']
visualization = Visualize(r)
visualization.createQuestionPoints(2)
visualization.createPartieBars(max_score)

plt.show()
