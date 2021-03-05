from os import listdir
import pandas as pd
from dir_list import make_list
processed_path = '../processed_files/'

win10_path='../win10/'
win227_path='../win227/'
win300_path='../win300/'





mon11_epo=1360587600
mon18_epo=1361192400


f_list = []
for i in make_list(processed_path):
    f_list.append(i)


def windows_func(win_size):
    window_list = []
    week_list = []
    windows = int(32400 / win_size)                 #32400 = 9 hours * 60 min * 60sec
    for x in range(0, 5):
        start=mon11_epo + x * 86400                  #86400 = 24hrs *60 *60
        for y in range(windows):
            z = start + y * win_size
            window_list.append(z)
            week_list.append('   w1')                      #week1

    for p in range(0, 5):
        start=mon18_epo + p * 86400
        for q in range(windows):
                r = start + q * win_size
                window_list.append(r)
                week_list.append('   w2')                  #week2


    comp_window(win_size,window_list)
    return week_list

#comparing RFP to window
def comp_window(win_size,window_list):

    num = 0
    for file in f_list:
        num += 1                            #for output purpose
        t_path = processed_path + file
        n1_path = win10_path + file
        n2_path = win227_path + file
        n3_path = win300_path + file
        df = pd.read_csv(t_path)
        RFP_list = df['Real First Packet'].tolist()
        RFP_list.sort()
        OD_list = df['doctets/duration'].tolist()


        a = len(window_list)
        b = len(OD_list)
        rowindex = 0
        avg_docdur = []
        for i in range(0, a):
            while rowindex < len(RFP_list):             #checks wheter row index doesnt fall out of the time frame
                if RFP_list[rowindex] < window_list[i]:
                    rowindex = rowindex + 1
                else:
                    break

            docpdursum = 0
            cnt = 0
            while (rowindex < b):
                # comparint RFP time to window size slots  and calculating average
                if ( window_list[i] <= RFP_list[rowindex] < window_list[i] + win_size):
                    docpdursum = docpdursum + OD_list[rowindex]
                    cnt = cnt + 1
                    rowindex = rowindex + 1
                else:
                    break

            if (cnt > 0):
                avg = docpdursum / cnt
            else:
                avg = 0.0001            #assigning very small value

            avg_docdur.append(avg)

        # save to new csv
        dfObj = pd.DataFrame({'windowlist  ':window_list, '  avg_dpd  ':avg_docdur,})

        if (win_size==10):
            dfObj.to_csv(n1_path, index=False)
        elif (win_size==227):
            dfObj.to_csv(n2_path, index=False)
        else:
            dfObj.to_csv(n3_path, index=False)

        print("File", num, "processed and saved for window size",win_size)













