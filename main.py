import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def startjob():
    iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'
    path = './data/iris.data'
    data = pd.read_csv(path, header=None)
    features = [0, 1]
    x, y = data[features], pd.Categorical(data[4]).codes
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.7)

    #分类器
    clf = svm.SVC(C= 0.1, kernel='linear', decision_function_shape='ovr')
    clf.fit(x_train, y_train.ravel())

    #准确率
    print(clf.score(x_train, y_train))
    print('训练集准确率: ', accuracy_score(y_train, clf.predict(x_train)))
    print(clf.score(x_test, y_test))
    print('测试集准确率: ', accuracy_score(y_test, clf.predict(x_test)))

    print(x_train[:5])
    print('decision_function: \n', clf.decision_function(x_train))
    print('\npredict: \n', clf.predict(x_train))

    x1_min, x2_min = x.min()
    x1_max, x2_max = x.max()

    x1, x2 = np.mgrid[x1_min:x1_max:500j,
                     x2_min:x2_max:500j] #生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1) #测试点
    grid_hat = clf.predict(grid_test) #预测分类值
    grid_hat = grid_hat.reshape(x1.shape) #使之与输入的形状相同
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    plt.figure(facecolor='w')
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)
    plt.scatter(x[features[0]], x[features[1]], c=y, edgecolors='k', s=50, cmap=cm_dark) #样本
    plt.scatter(x_test[features[0]], x_test[features[1]], s=120, facecolors='none', zorder=10) #测试数据
    plt.xlabel(iris_feature[0], fontsize=13)
    plt.ylabel(iris_feature[1], fontsize=13)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.title('鸢尾花SVM二特征分类', fontsize=16)
    plt.grid(b=True, ls=':')
    plt.tight_layout(pad=1.5)
    plt.show()



if __name__ == '__main__':
    startjob()