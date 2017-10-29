#list
import numpy
def filtering(wave_list):
    L=numpy.max(wave_list)-numpy.min(wave_list)

    while 1:
        if int(abs(wave_list[0]))< (0.15* L):
            wave_list.pop(0)
        else:
            break
    while 1:
        if int(abs(wave_list[-1]))< (0.15* L):
            wave_list.pop(-1)
        else:
            break
     
    return(wave_list)







print(filtering([20,-20,30,-60,20,-200,200,-200,300,-60,20]))
