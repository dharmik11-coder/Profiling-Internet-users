from os import listdir
import pandas as pd
from dir_list import make_list
from win_list import windows_func
from Spearman import spearman_files
from Spearman import p_calc

org_path='../InfosecData/'                             #excel files
processed_path = '../processed_files/'                 #storing cv files

#mon11_epo = 1360587600  (8AM)
#fri22_epo = 1361570400  (5PM)

file_list=[]                                    #list to store filenames
week10_list=[]
week227_list=[]
week300_list=[]

#removing unwanted data and converting excel to csv files using below function
def process_data():
    for i in make_list(org_path):
        file_list.append(i)

    num = 0                                     #just for viewing output file number on console
    for i in file_list:
        num += 1
        t_path= org_path + i
        df=pd.read_excel(t_path)
        df.drop(df.columns[[0,1,2,4,6,7,8]], axis=1, inplace=True)       #discarding unrequired data

        df['Real First Packet'] =df['Real First Packet']/1000               #milisecond time to seconds
        df=df[(df['Real First Packet'] > 1360587600) & (df['Real First Packet']  < 1361570400 ) & (df['Duration'] !=0)]
        df['doctets/duration'] = (df['doctets']/df['Duration'])*1000
        df.drop(df.columns[[0,2]], axis =1,inplace=True)

        csv_files= i.replace('xlsx','csv')                               #xls to csv
        outputpath = processed_path + csv_files
        df.to_csv(outputpath ,index=False)                               #saving as csv files
        print("file", num ,"processing...")


#process_data()


#week10_list=windows_func(10)

#week227_list=windows_func(227)

#week300_list=windows_func(300)

#spearman_files(week10_list,week227_list,week300_list)
p_calc()