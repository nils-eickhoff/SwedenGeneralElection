from turtle import clear
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import jaccard_score
sns.set()

class Visualize:
    def __init__(self, r):
        self.r = r
        fig = plt.figure(figsize=(15, 8))
        plt.axis('off')
        inner_circle = plt.Circle((0, 0), self.r, color='red', fill=False)
        outer_circle = plt.Circle((0, 0), 2*self.r, color='red', fill=False, linestyle='--')
        plt.gca().add_patch(inner_circle)
        plt.gca().add_patch(outer_circle)
        plt.text(-0.5, 2.1, 'Nisses Election Compass')

    def createQuestionPoints(self, nr_of_questions):
        degrees_per_point = 360 / nr_of_questions
        self.deg_array = np.deg2rad(np.arange(0, 360, degrees_per_point)) # deg array of the points
        self.coord_of_points = np.zeros([nr_of_questions, 2])
        self.coord_of_points [:, 0] = np.cos(self.deg_array) # x-coords
        self.coord_of_points [:, 1] = np.sin(self.deg_array) # y-coords
        plt.plot(self.coord_of_points[:, 0], self.coord_of_points[:, 1], '.b')
    
    def createPartieBars(self, max_score: int):
        counter = 0
        answers = np.arange(df.shape[0])
        for idx, question in df.iterrows():
            sorted_value_index = np.argsort(question.values)
            previous_value = 0
            answers[counter] = int(input(f"{df.index[counter]}: "))
            if ( counter == 0 ):
                x_org = self.coord_of_points[counter, 0]*(1 + answers[counter] / max_score)
                y_org = self.coord_of_points[counter, 1]*(1 + answers[counter] / max_score)
            elif ( counter > 0 ):
                x_cur = self.coord_of_points[counter, 0]*(1 + answers[counter] / max_score)
                y_cur= self.coord_of_points[counter, 1]*(1 + answers[counter] / max_score)
                plt.plot([x_prev, x_cur], [y_prev, y_cur], color=color_list[-1])
                #plt.text(x_prev, y_prev, "YOUR_ANSWER", fontsize=5*r)
            x_prev = self.coord_of_points[counter, 0]*(1 + answers[counter] / max_score)
            y_prev = self.coord_of_points[counter, 1]*(1 + answers[counter] / max_score)
            for index in sorted_value_index:
                current_partie = df.columns[sorted_value_index[index]]
                current_value = question.values[sorted_value_index[index]]
                current_partie_color = color_list[sorted_value_index[index]]
                x0 = self.coord_of_points[counter, 0]*(1 + previous_value / max_score)
                y0 = self.coord_of_points[counter, 1]*(1 + previous_value / max_score)
                x1 = self.coord_of_points[counter, 0]*(1 + current_value / max_score)
                y1 = self.coord_of_points[counter, 1]*(1 + current_value / max_score)
                plt.plot([x0, x1], [y0, y1], color=current_partie_color)
                plt.text(x1, y1, current_partie, fontsize=5*r)
                previous_value = current_value
            #plt.plot([self.coord_of_points[counter, 0], x1], [self.coord_of_points[counter, 1], y1], '--k', alpha=0.5, markersize=0.5)
            if (counter / df.shape[0] < 0.5):
                plt.text(self.coord_of_points[counter, 0]*2.05*self.r, self.coord_of_points[counter, 1]*2.05*self.r, question.name, fontsize=7*r, rotation=360*(counter/df.shape[0]) - 90, verticalalignment='center', fontweight='bold')
            else:
                plt.text(self.coord_of_points[counter, 0]*2.05*self.r, self.coord_of_points[counter, 1]*2.05*self.r, question.name, fontsize=7*r, rotation=360*(counter/df.shape[0]) + 90, verticalalignment='center', fontweight='bold')
            counter += 1
        plt.plot([x_cur, x_org], [y_cur, y_org], color=color_list[-1])

print("Please enter ant int i, where i ≥ 0\n")
df = pd.read_csv('Sweden_partie_program_opinions_2022.csv', sep=';', skiprows=1)
df = df.set_index(df.columns[0]) # use the questions as radii index

#answer = input(f"{df.index[0]}: ")
#print(f"Your answer: {answer}\n")
#print(df.loc['Skatt']) # extract a specific question

max_score = 10 # maximum value for a question in the table
r = 1 # radii
color_list = ['#009933', '#000077', '#006AB3', '#83CF39', '#52BDEC', '#E8112d', '#DDDD00', '#DA291C', '#FFA500']
visualization = Visualize(r)
visualization.createQuestionPoints(df.shape[0])
visualization.createPartieBars(max_score)

plt.show()
