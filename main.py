import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("marks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math_score"], show_hist=False)

data.pop(0)
# finding mean and std_devaiation

meanofclass = statistics.mean(data)
stddeviationofclass = statistics.stdev(data)

print("Mean of the entire maths marks for class is ", meanofclass)
print("Standard Deviation of the entire maths marks for class is ", stddeviationofclass)


def experiment():
    samples = []
    for i in range(100):
        index = random.randint(0, len(data)-1)
        samples.append(data[index])
    samplesmean = statistics.mean(samples)
    return samplesmean


samplemean = []


def sampling():
    for i in range(1000):
        value = experiment()
        samplemean.append(value)


sampling()

meanofSample = statistics.mean(samplemean)
stdevofsample = statistics.stdev(samplemean)

print(meanofSample, stdevofsample)
fig = ff.create_distplot(
    [samplemean], ["Sampling Mean distribution"], show_hist=False)


firststdstart, firststdend = meanofSample - \
    stdevofsample, meanofSample + stdevofsample
secondstdstart, secondstdend = meanofSample-2 * \
    stdevofsample, meanofSample+2 * stdevofsample
thirdstdstart, thirdstdend = meanofSample-3 * \
    stdevofsample, meanofSample + 3*stdevofsample

fig.add_trace(go.Scatter(x =[meanofSample, meanofSample], y = [0, 0.20], name = "MEAN OF SAMPLES", mode = "lines"))
fig.add_trace(go.Scatter(x =[firststdstart,firststdstart], y = [0, 0.20], name = "First Standard deviation start", mode = "lines"))
fig.add_trace(go.Scatter(x =[firststdend,firststdend], y = [0, 0.20], name = "First Standard deviation end", mode = "lines"))
fig.add_trace(go.Scatter(x =[secondstdstart,secondstdstart], y = [0, 0.20], name = "Second Standard deviation start", mode = "lines"))
fig.add_trace(go.Scatter(x =[secondstdend,secondstdend], y = [0, 0.20], name = "Second Standard deviation end", mode = "lines"))
fig.add_trace(go.Scatter(x =[thirdstdstart,thirdstdstart], y = [0, 0.20], name = "Third Standard deviation start", mode = "lines"))
fig.add_trace(go.Scatter(x =[thirdstdend,thirdstdend], y = [0, 0.20], name = "Third Standard deviation end", mode = "lines"))
#fig.show()
# first intervention 
df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()
mean1 = statistics.mean(data1)
print("mean of the first intervention is", mean1 )

#second intervention 
df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean2 = statistics.mean(data2)
print("mean of the second intervention is", mean2 )

#third intervention
df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()
mean3 = statistics.mean(data3)
print("mean of the third intervention is", mean3 )

