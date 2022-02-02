# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oD4xY1FGaUC82R-uvQGr35AdMJkIhNXO
"""

import numpy as np
x=[10,30,50] #node sayısı
y=[0.2,0.5,0.8,1.0] # percentage of car owner
z=[0.5,1]#schedule percentage
t=5 #number of working day
import random
import pandas as pd

def distance_matrix(nodesayısı):
    a = np.round(np.random.rand(nodesayısı+2, nodesayısı+2)*100,2) #+2:dummy and end node
    distance_mat = np.tril(a) + np.tril(a, -1).T
    np.fill_diagonal( distance_mat, 1000)
    for i in range(1,nodesayısı+2):
        distance_mat[0][i]=0.0
        distance_mat[i][0]=0.0

    return (distance_mat)


def feasibility_check(car_owner,schedule,worker_number):
    status=True
    for i in range(schedule.shape[1]):
        intersec=0
        for j in range(0,schedule.shape[0]-1):
            if schedule[j][i]==1 and car_owner[j]==1:
                intersec+=1
        if intersec*5<worker_number:
            status=False
    return (status)
test_number=0
for i in range(len(x)):
    for j in range(len(y)):
        car_owner = np.zeros(x[i]+2)#+2:dummy and end node
        #car_owner = [0]*(x[i] + 2)  # +2:dummy and end node
        owner_number=x[i]*y[j]
        counter=0
        while counter<owner_number:
            rand_owner=random.randint(1, x[i])
            if car_owner[rand_owner]==0:
                car_owner[rand_owner]=1
                counter+=1
        for k in range(len(z)):
            schedule=np.zeros((x[i]+2,5))# dummy and end node
            schedule[0]=1.0 # dummy node
            schedule[-1] = 1.0 #end node
            worker_number=x[i]*z[k]
            rand_worker=random.randint(1, x[i])
            feasiblity=False
            while feasiblity==False:
                for l in range(t):
                    counter_worker = 0
                    while counter_worker < worker_number:
                        rand_owner = random.randint(1, x[i])
                        if schedule[rand_owner][l]==0:
                            schedule[rand_owner][l]=1
                            counter_worker+=1
                feasiblity=feasibility_check(car_owner,schedule,worker_number)
            test_number+=1
            car_owner_df=pd.DataFrame(car_owner)
            schedule_df = pd.DataFrame(schedule,columns=['1','2','3','4','5'])

            distance_matrix_df=pd.DataFrame(distance_matrix(x[i]))
            schedule_df.to_csv("schedule_test"+str(test_number)+".csv")
            car_owner_df.to_csv("car_owner_test" + str(test_number) + ".csv",header=False)
            distance_matrix_df.to_csv("distance_matrix_test" + str(test_number) + ".csv")