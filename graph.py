
from main import *
import pandas as pd
import matplotlib.pyplot as plt

# THIS ONLY WORKS IF THE CORRECT LINES IN MAIN.PY ARE UNCOMMENTED

data = table # this is the table of values from main.py
graph_data = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }

for strategy in data: # calculates the average of the q-values for each state, done for each strategy
    for game in data[strategy]:
       if game not in graph_data[strategy]:
           graph_data[strategy][game] = [0, 0]
       for state in data[strategy][game]:
         #   print(state, data[strategy][game][state])
           graph_data[strategy][game][0] += data[strategy][game][state][0]
           graph_data[strategy][game][1] += data[strategy][game][state][1]
       graph_data[strategy][game][0] = float(graph_data[strategy][game][0]/len(data[strategy][game]))
       graph_data[strategy][game][1] = float(graph_data[strategy][game][1]/len(data[strategy][game]))


def grim_trigger_graph(graph_data): #creates the graph for the Grim Trigger strategy opponent
   grim_x = []
   grim_y0 = []
   grim_y1 = []
   for game in graph_data["Grim Trigger"]:
      if game < 1500:
         grim_x.append(game)
         grim_y0.append(graph_data["Grim Trigger"][game][0])
         grim_y1.append(graph_data["Grim Trigger"][game][1])
   plt.plot(grim_x, grim_y0, label='Cooperate', linestyle="dashdot", color = '#FE8E49')
   plt.plot(grim_x, grim_y1, label='Defect', linestyle="solid", color = '#FE8E49')
   plt.title("Evolution of Q-values Over Training Games for The Grim Trigger Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('grim.png') # orange
   plt.show()



def hard_majority_graph(graph_data): #creates the graph for the Hard Majority strategy opponent
   hard_majority_x = []
   hard_majority_y0 = []
   hard_majority_y1 = []
   for game in graph_data["Hard Majority"]:
      if game < 1500:
         hard_majority_x.append(game)
         hard_majority_y0.append(graph_data["Hard Majority"][game][0])
         hard_majority_y1.append(graph_data["Hard Majority"][game][1])
   plt.plot(hard_majority_x, hard_majority_y0, label='Cooperate', linestyle="dashdot", color = '#0F186B') 
   plt.plot(hard_majority_x, hard_majority_y1, label='Defect', linestyle="solid", color = '#0F186B') 
   plt.title("Evolution of Q-values Over Training Games for The Hard Majority Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('hard.png')# blue lines
   plt.show()



def mean_graph(graph_data): #creates the graph for the Mean strategy opponent
   mean_x = []
   mean_y0 = []
   mean_y1 = []
   for game in graph_data['Mean']:
      if game < 1500:
         mean_x.append(game)
         mean_y0.append(graph_data["Mean"][game][0])
         mean_y1.append(graph_data["Mean"][game][1])
   plt.plot(mean_x, mean_y0, label='Cooperate', linestyle="dashdot", color = '#FE0B0B') 
   plt.plot(mean_x, mean_y1, label='Defect', linestyle="solid", color = '#FE0B0B')
   plt.title("Evolution of Q-values Over Training Games for The Mean Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('mean.png') # red lines
   plt.show()


def nice_graph(graph_data): #creates the graph for the Nice strategy opponent
   nice_x = []
   nice_y0 = []
   nice_y1 = []
   for game in graph_data["Nice"]:
      if game < 1500:
         nice_x.append(game)
         nice_y0.append(graph_data["Nice"][game][0])
         nice_y1.append(graph_data["Nice"][game][1])
   plt.plot(nice_x, nice_y0, label='Cooperate', linestyle="dashdot", color = '#FEC620') 
   plt.plot(nice_x, nice_y1, label='Defect', linestyle="solid", color = '#FEC620')  
   plt.title("Evolution of Q-values Over Training Games for The Nice Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('nice.png') # yellow lines
   plt.show()


def reverse_tit_for_tat_graph(graph_data):
   reverse_t4t_x = []
   reverse_t4t_y0 = []
   reverse_t4t_y1 = []
   for game in graph_data['Reverse Tit For Tat']:
      if game < 1500:
         reverse_t4t_x.append(game)
         reverse_t4t_y0.append(graph_data["Reverse Tit For Tat"][game][0])
         reverse_t4t_y1.append(graph_data["Reverse Tit For Tat"][game][1])
   plt.plot(reverse_t4t_x, reverse_t4t_y0, label='Cooperate', linestyle="dashdot", color = '#2CA060')
   plt.plot(reverse_t4t_x, reverse_t4t_y1, label='Defect', linestyle="solid", color = '#2CA060')  #color = 'red'
   plt.title("Evolution of Q-values Over Training Games for The Reverse\n Tit For Tat Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('reverse tit for tat.png') # green lines
   plt.show()


def tit_for_tat_graph(graph_data):
   t4t_x = []
   t4t_y0 = []
   t4t_y1 = []
   for game in graph_data["Tit For Tat"]:
      if game < 1500:
         t4t_x.append(game)
         t4t_y0.append(graph_data["Tit For Tat"][game][0])
         t4t_y1.append(graph_data["Tit For Tat"][game][1])
   plt.plot(t4t_x, t4t_y0, label='Cooperate', linestyle="dashdot", color = '#802476')
   plt.plot(t4t_x, t4t_y1, label='Defect', linestyle="solid", color = '#802476')  #color = 'red'
   plt.title("Evolution of Q-values Over Training Games for The Tit For Tat Strategy")
   plt.xlabel("Game Number") #each state from training data
   plt.ylabel("Q-Value")
   plt.legend()
   plt.savefig('tit for tat.png') # purple lines
   plt.show()

grim_trigger_graph(graph_data)
hard_majority_graph(graph_data)
mean_graph(graph_data)
nice_graph(graph_data)
reverse_tit_for_tat_graph(graph_data)
tit_for_tat_graph(graph_data)



#graph percent