# ***************************************************************************************
# Dự đoán điểm thi THPT và gợi ý trường-ngành học cho học sinh dựa trên điểm tổng kết   *
# Sai số theo RMSE trên tập test: khoảng 110 (<180, chấp nhận được)                     *
#                                                                                       *
# Nguyễn Đăng Cương - 1811640                                                           *    
#                                                                 Bài tập tết 2020 BKAIC*
# ***************************************************************************************



import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

#Global variable
#=====================================================================================


#function
#=====================================================================================
def LoadData(list_file):
    return {}

def split_dataset(data):
    return ({},{})

def LinearRegression(train,label):
    return (0,0)

# def add_comb(_comb, mark):
#     for item in _comb:
#         comb[item] += mark
#     return 1

# def calc(b,x):
#     ret = b[0] + b[1] * x
#     if ret > 0: 
#         return round(ret,2)
#     else:
#         return 0
    
def Prediction(toan, van, li, hoa, sinh, su, dia, gdcd, anh):
    
    return 0
    #=====================================================================================

#main function
#=====================================================================================
# data_exam = LoadData(['diem_tn_NK.xls','diem_tn_NQ.xls', 'diem_tn_PL.xls', 'diem_tn_PR.xls'])
# data_gpa = LoadData(['so_diem_tong_ket_khoi_khoi_12_NK.xls',
#                 'so_diem_tong_ket_khoi_khoi_12_NQ.xls', 'so_diem_tong_ket_khoi_khoi_12_PL.xls', 
#                 'so_diem_tong_ket_khoi_khoi_12_PR.xls'])
# data_exam.columns = exam_columns
# data_gpa = data_gpa.drop(columns = 'Ten')
# data = pd.concat([data_gpa,data_exam], axis = 1, join = 'inner')
# data = data.reset_index(drop = True)

# (train,test) = split_dataset(data)

# #training 
# for subject_lower,subject_upper in zip(subs,gpa_columns[1:]):
#     factor.setdefault(subject_lower,LinearRegression(train[subject_upper], train['_'+subject_upper]))

# #print(factor)

# #calc error (RMSE)
# error = 0
# for subject_lower,subject_upper in zip(subs,gpa_columns[1:]):
#     calc_test = calc(factor[subject_lower],test[subject_upper].all())
#     error += sum(test['_' + subject_upper] - calc_test) ** 2

# error = (error / len(test)) ** 0.5
# print('\n\t\tRMSE : ',error,'\n')

