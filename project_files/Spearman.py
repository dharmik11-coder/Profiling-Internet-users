from os import listdir
import pandas as pd
from scipy.stats import spearmanr

win10='../win10/'
win227='../win227/'
win300='../win300/'
listforfiles= ['../spearmanV/swin10.csv','../spearmanV/swin227.csv','../spearmanV/swin300.csv']

#converting 54files of each windowsize to each single file
def spearman_files(week10_list,week227_list,week300_list):

        df10 =pd.DataFrame()
        df10['week'] = week10_list
        file1_list=listdir(win10)
        for file in file1_list:
            curr_path=win10 + file
            tdf=pd.read_csv(curr_path)
            list_OD=tdf['  avg_dpd  '].tolist()
            df10[file]=list_OD
            n_path='../spearmanV/swin10.csv'
            df10.to_csv(n_path, index = False)

        df227 = pd.DataFrame()
        df227['week'] = week227_list
        file2_list = listdir(win227)
        for file in file2_list:
            curr_path = win227 + file
            tdf = pd.read_csv(curr_path)
            list_OD = tdf['  avg_dpd  '].tolist()
            df227[file] = list_OD
            n_path = '../spearmanV/swin227.csv'
            df227.to_csv(n_path, index=False)

        df300 = pd.DataFrame()
        df300['week'] = week300_list
        file3_list = listdir(win300)
        for file in file3_list:
            curr_path = win300 + file
            tdf = pd.read_csv(curr_path)
            list_OD = tdf['  avg_dpd  '].tolist()
            df300[file] = list_OD
            n_path = '../spearmanV/swin300.csv'
            df300.to_csv(n_path, index=False)




def p_calc():
    i = 0
    windows = ['10', '227', '300']
    for f in listforfiles:
        spearman_final(f, windows[i])
        i += 1



def spearman_final(f,windows):
    df = pd.read_csv(f)
    df_week1 = df[df.week == '   w1']
    df_week2 = df[df.week == '   w2']
    df_week1.drop(['week'], axis=1, inplace=True)
    df_week2.drop(['week'], axis=1, inplace=True)
    header_list = [i for i in range(54)]
    df = pd.DataFrame(columns=header_list)
    # print(header_list)
    print(df.info())

    print(df_week2.shape[1], '****')

    for i in range(df_week1.shape[1]):
        week1user = df_week1.iloc[:, i]
        somelist = []

        for j in range(df_week2.shape[1]):
            week2user = df_week2.iloc[:, j]
            rho, p = spearmanr(week1user, week2user)
            somelist.append(rho)

        someseries = pd.Series(somelist, index=df.columns)
        df = df.append(someseries, ignore_index=True)
        df.fillna(0.001)
        print(df.shape[0], " appended ")

    # print(df.info())
    outputpath = '../final_output/' + windows + ".csv"
    df.to_csv(outputpath)