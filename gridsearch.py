# -*- coding: utf-8 -*-
"""his1_homeworkgridsearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/random643/62372badc513b0ba9cd29179eeeff233/his1_homeworkgridsearch.ipynb

# 1. Decision tree
"""

!pip install bayesian-optimization

def black_box_function(x, y):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    return -x ** 2 - (y - 1) ** 2 + 1

"""## 1.1. Getting data"""

from google.colab import drive
drive.mount('/content/drive')

data_url = '/content/drive/MyDrive/Gis/his1/for_work.csv'

import pandas as pd
data_raw = pd.read_csv(data_url)

data_raw

print(data_raw.info())

from collections import Counter

# Assuming data_raw is your DataFrame
data = data_raw.drop(columns=['Class'])  # Adjust this based on your actual column names
target = data_raw['Class']

# Display information about the dataset
print(data.info())

# Display the distribution of classes in the target
print(Counter(target))

def target_function(V1, V2, V3, V4):
    # Ваш код обучения модели с использованием параметров
    # ...

    # Возвращаем значение метрики, которую мы хотим оптимизировать
    return accuracy

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=0)

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0 )
cross_val_score(clf, data, target, cv=10)

clf.fit(data,target)

clf.get_depth()

from sklearn.model_selection import GridSearchCV

depth_uptimize = clf.get_depth()

parameters = { 'max_depth':range(2, depth_uptimize + 1  )}

parameters

clf_GridSearchCV = GridSearchCV(clf, parameters)

clf_GridSearchCV

clf_GridSearchCV.fit(data,target)

clf_GridSearchCV.best_params_

clf_GridSearchCV.best_estimator_

from sklearn import tree
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(20,10))
tree.plot_tree(clf_GridSearchCV.best_estimator_,feature_names = data.columns )

print(Counter(target))

print(data_raw.shape)
print(target.shape)

"""## 1.2. Tree learning"""

from bayes_opt import BayesianOptimization
pbounds = {'x': (2, 4), 'y': (-3, 3)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

from google.colab import drive
drive.mount('/content/drive')

optimizer.maximize(
    init_points=2,
    n_iter=3,
)

print(optimizer.max)

for i, res in enumerate(optimizer.res):
    print("Iteration {}: \n\t{}".format(i, res))

optimizer.set_bounds(new_bounds={"x": (-2, 3)})

optimizer.maximize(
    init_points=0,
    n_iter=5,
)





depth_uptimize = clf.get_depth()

parameters = { 'max_depth':range(2, depth_uptimize + 1  )}

optimizer.maximize(init_points=5, n_iter=10)

"""## 1.3. Visualizing the tree"""

best_params = optimizer.max['params']  # Получите оптимальные гиперпараметры
best_max_depth = int(round(best_params['max_depth']))  # Преобразуйте параметры в int и округлите
 = DecisionTreeClassifier(max_depth=best_max_depth, random_state=0)  # Создайте модель с оптимальными параметрами

best_clf.fit(data, target)  # Обучите модель с оптимальными параметрами на данных

from sklearn import tree
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(30, 20))  # Увеличьте размер изображения

# Определите свою цветовую палитру для filled=True
node_colors = ['lightgray' if feature != -2 else 'lime' for feature in best_clf.apply(data)]

fig = plt.figure(figsize=(20, 10))
tree.plot_tree(best_clf, feature_names=data.columns, filled=True)

data.columns

"""# 2. Datalog

## 2.1. Creating terms

## 2.2. Query
"""



"""## 2.3. Conjunction"""



"""## 2.4. Functions"""



"""## 2.5. Conditions"""



"""# 3. Describing the Tree with Datalog

## 3.1. Creating terms
"""



"""## 3.2. Rules"""



"""## 3.2. Facts"""



"""## 3.3. Query"""



"""# 4. Dynamic clauses generation"""

for index, row in data.iterrows():
  prop1[index] = row['prop1']
  prop2[index] = row['prop2']