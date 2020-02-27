##基础 点、线、坐标篇
import numpy as np
import matplotlib.pyplot as plt 

plt.figure(figsize=[20,5])#注意这里20的含义是指横坐标每个inch的像素值，5是纵坐标

ax1 = plt.subplot(2,2,1)
ax1.grid(color='g',linestyle='-.')
ax1.plot(np.sin(np.linspace(-2*np.pi,2*np.pi,100)),'b',alpha=0.3)

ax1 = plt.subplot(2,2,2)
x = np.linspace(-10,10,1000)
ax1.plot(np.sin(x),np.cos(x))
ax1.plot(np.exp(np.random.randn(10)),label='new curve1')
ax1.plot(np.exp(np.random.randn(10)),label='new curve2')
ax1.plot(np.exp(np.random.randn(10)),label='new curve3')
ax1.plot(np.exp(np.random.randn(10)),label='new curve4')
#不写这一句图例是显示不出来的，我反正也要写这一句，还不如就用它来定义图例
#loc是一个枚举值对应不同的字符串
ax1.legend(loc='lower right',ncol=2)#等同于loc=4

ax2 = plt.subplot(2,2,3,facecolor='black')
ax2.axis([200,800,-0.75,0.75])#这里的作用和xlim ylim一样的
ax2.plot(np.sin(np.linspace(-2*np.pi,2*np.pi,1000)),ls='-.',lw=10)

ax3 = plt.subplot(2,2,4)
x = np.random.rand(10)
#ax3.axis('tight')#这感觉是做了归一化呢
#关于tight的例子，这不是一个好的例子，具体可以参考这个链接，画直方图的时候用到的例子
#https://stackoverflow.com/questions/37558329/matplotlib-set-axis-tight-only-to-x-or-y-axis
ax3.plot(x,'m',x.cumsum(),'y',linestyle='--',marker='>')
ax3.set_xticklabels('0ABCDef')

plt.savefig('test.jpg',dpi=1000,facecolor='red')

#基础 图形篇
#直方图 条形图 饼图 散点图 箱型图
#官方例子直方图
np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75) #density代替normed=True
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') #这个文字的用法还是挺牛逼的，用了latex类似的表达
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show() 
#某例子条形图
# https://www.cnblogs.com/always-fight/p/9707727.html
y = range(1,17)
plt.bar(np.arange(16), y, alpha=0.5, width=0.3, color='yellow',edgecolor='red', label='The First Bar', lw=3)
plt.bar(np.arange(16)+0.4, y, alpha=0.2, width=0.3, color='green',edgecolor='blue', label='The Second Bar', lw=3)
#饼图
plt.pie(np.array([0.4,0.2,0.15,0.2]),labels=['dog','cat','bird','cow'],shadow=True,explode=[0.1,0,0,0],autopct='%0.1f%%')
#散点图
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

midwest = pd.read_csv('midwest_filter.csv')
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
plt.figure(figsize=(16,10),dpi=80,facecolor='w',edgecolor='k')

for i,cat in enumerate(categories):
    #正常情况下都是输入x y这么玩的
    #后来为了能更好的结合pandas使用新加了功能data,参考下面的帖子
    #https://matplotlib.org/users/prev_whats_new/whats_new_1.5.html#working-with-labeled-data-like-pandas-dataframes
    
    #Working with labeled data like pandas DataFrames
    #Plot methods which take arrays as inputs can now also work with labeled data and unpack such data.
    #
    #This means that the following two examples produce the same plot:
    #
    #Example
    #
    #df = pd.DataFrame({"var1":[1,2,3,4,5,6], "var2":[1,2,3,4,5,6]})
    #print(df)
    #plt.plot(df["var1"], df["var2"])
    #Copy to clipboard
    #Example
    #plt.scatter("var1", "var2", data=df)
    #Copy to clipboard
    #This works for most plotting methods, which expect arrays/sequences as inputs. data can be anything which supports __getitem__ (dict, pandas.DataFrame, h5py, ...) to access array like values with string keys.
    #
    #In addition to this, some other changes were made, which makes working with labeled data (ex pandas.Series) easier:
    #
    #For plotting methods with label keyword argument, one of the data inputs is designated as the label source. If the user does not supply a label that value object will be introspected for a label, currently by looking for a name attribute. If the value object does not have a name attribute but was specified by as a key into the data kwarg, then the key is used. In the above examples, this results in an implicit label="var2" for both cases.
    #plot() now uses the index of a Series instead of np.arange(len(y)), if no x argument is supplied.
    plt.scatter('area','poptotal',#注意这里的area和poptotal就是对应的列名，所以这是一种很巧妙的方法
                data=midwest.loc[midwest.category==cat,:],
                s=20,cmap=colors[i],label=str(cat))
    
plt.gca().set(xlim=(0.0,0.1),ylim=(0,90000),xlabel='Area',ylabel='Population')#plt.gca()获取当前axe实例
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Scatterplot of Midwest Area vs Population',fontsize=22)
plt.legend(fontsize=12)
plt.show()

##如何使用np.meshgrid 主要用来解决坐标网格点太多时候显示的问题
import numpy as np
import matplotlib.pyplot as plt
x = np.array([[0,1,2],[0,1,2]])
y = np.array([[1,1,1],[0,0,0]])
plt.plot(x,y,color='red',marker='.',markersize=10,linestyle='-')#要求x,y维度相同，不然会报错
plt.grid=True
plt.show()

x1 = np.array([0,1,2]) #注意这里的x1,y1表示横纵坐标的列向量 已经不是上面的二维矩阵
y1 = np.array([0,1])
X1,Y1=np.meshgrid(x1,y1)
plt.plot(X1,Y1,color='red',marker='.',markersize=10,linestyle='-')
plt.grid=True
plt.show()

#接下来就是NB之处，对于需要大量的横纵坐标点
x2 = np.linspace(0,2000,20)
y2 = np.linspace(0,2000,10)
X2,Y2=np.meshgrid(x2,y2)
plt.plot(X2,Y2,color='red',marker='.',markersize=10,linestyle='')
plt.grid = True
plt.show()

##如何在柱状图上面显示数字
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_info = pd.read_csv('student-info.csv',sep=';')
df_score = pd.read_csv('student-score.csv',sep=';')
result = pd.merge(df_info,df_score,on=['ID'])
print(result.head())
result1 = result.groupby(['age']).aggregate({'G1':'mean','G2':'mean','G3':'mean'})
ax = result1.plot(figsize=(15,5),kind='bar',width=0.9)# figsize unit: inch

#print(type(ax))   #<class 'matplotlib.axes._subplots.AxesSubplot'>
#can get all the rects (24)
for p in ax.patches:
    text = str(round(p.get_height(),2))
    ax.annotate(text, (p.get_x()+0.02, p.get_height()+0.2))
    #print(p)
