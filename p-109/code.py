
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

print("Student Performances Stats")

#reading the file
df=pd.read_csv("data.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
Stdev = statistics.stdev(data)
median= statistics.median(data)
mode=statistics.mode(data)

#finding 3 diff Stdev by subtracting the Stdev from the mean and then adding it to the mean too.
Stdevstart1,Stdevend1=mean-Stdev,mean+Stdev
Stdevstart2,Stdevend2=mean-(2*Stdev),mean+(2*Stdev)
Stdevstart3,Stdevend3=mean-(3*Stdev),mean+(3*Stdev)

list_of_data_within_1_Stdev=[result for result in data if result> Stdevstart1 and result <Stdevend1]
list_of_data_within_2_Stdev=[result for result in data if result> Stdevstart2 and result <Stdevend2]
list_of_data_within_3_Stdev=[result for result in data if result> Stdevstart3 and result <Stdevend3]

#showing the mean, median, mode & Stdev for the entire data
print("Mean is ",mean)
print("Median is ",median)
print("Mode is ",mode)
print("Standard deviation is ",Stdev)

#finding 3 diff Stdev's and then printing them.
print(len(list_of_data_within_1_Stdev)*100.0/len(data))
print(len(list_of_data_within_2_Stdev)*100.0/len(data))
print(len(list_of_data_within_3_Stdev)*100.0/len(data))

#Drawing a graph for everything
fig=ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.06], mode="lines", name= "MEAN"))
fig.add_trace(go.Scatter(x=[Stdevstart1, Stdevstart1], y=[0, 0.06], mode="lines", name="Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[Stdevend1, Stdevend1], y=[0, 0.06], mode="lines", name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[Stdevstart2, Stdevstart2], y=[0, 0.06], mode="lines", name="Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[Stdevend2, Stdevend2], y=[0, 0.06], mode="lines", name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[Stdevstart3, Stdevstart3], y=[0, 0.06], mode="lines", name="Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x=[Stdevend3, Stdevend3], y=[0, 0.06], mode="lines", name="Standard Deviation 3 end"))
fig.show()