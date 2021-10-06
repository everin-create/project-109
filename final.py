import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("performance.csv")

reading_score = df["reading score"].to_list()

score_mean = statistics.mean(reading_score)

score_median = statistics.median(reading_score)

score_mode = statistics.mode(reading_score)

print("Mean, Median and Mode of reading score is {}, {} and {} respectively".format(score_mean, score_median, score_mode))

score_stdev = statistics.stdev(reading_score)

score_1stdev_start,score_1stdev_end = score_mean-score_stdev, score_mean+score_stdev
score_2stdev_start,score_2stdev_end = score_mean-(2*score_stdev), score_mean+(2* score_stdev)
score_3stdev_start,score_3stdev_end = score_mean-(3*score_stdev), score_mean+(3*score_stdev)

score_data_1stdev = [result for result in reading_score if result > score_1stdev_start and result < score_1stdev_end]
score_data_2stdev = [result for result in reading_score if result > score_2stdev_start and result < score_2stdev_end]
score_data_3stdev= [result for result in reading_score if result > score_3stdev_start and result < score_3stdev_end]

print("{}% of data for reading score lies within 1 standard deviation".format(len(score_data_1stdev)*100.0/len(reading_score)))
print("{}% of data for reading score lies within 2 standard deviations".format(len(score_data_2stdev)*100.0/len(reading_score)))
print("{}% of data for reading score lies within 3 standard deviations".format(len(score_data_3stdev)*100.0/len(reading_score)))

fig = ff.create_distplot([reading_score], ["reading score"], show_hist=False)
fig.add_trace(go.Scatter(x=[score_mean, score_mean], y=[0, 0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[score_1stdev_start, score_1stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[score_1stdev_end, score_1stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[score_2stdev_start,score_2stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[score_2stdev_end, score_2stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[score_3stdev_start, score_3stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[score_3stdev_end, score_3stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))

fig.show()

