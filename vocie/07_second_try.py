import wave
import pyaudio
import numpy,pylab,time
a=time.time()
def filtering(wave_data):
    wave_list=wave_data.tolist()
    L=numpy.max(wave_list)-numpy.min(wave_list)

    while 1:
        if int(abs(wave_list[0]))< (0.15* L):
           wave_list.remove(wave_list[0])
        else:
            break
    while 1:
        if int(abs(wave_list[-1]))< (0.15* L):
            wave_list.remove(wave_list[-1])
        else:
            break
     
    return(wave_list)

def sound(pathfile):
    wf = wave.open(pathfile,"rb")
    #创建PyAudio对象
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True)
    nframes = wf.getnframes()
    framerate = wf.getframerate()
    #读取完整的帧数据到str_data中，这是一个string类型的数据
    str_data = wf.readframes(nframes)
    wf.close()
    #将波形数据转换为数组
    # A new 1-D array initialized from raw binary or text data in a string.
    wave_data = numpy.fromstring(str_data, dtype=numpy.short)
    #将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
    #wave_data.shape = -1,2
    #将数组转置
    #wave_data = wave_data.T
    #time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
    wave_data1=filtering(wave_data)
import wave
import pyaudio
import numpy
import pylab
import os
def filtering(wave_data):
    wave_list=wave_data.tolist()
    L=numpy.max(wave_list)-numpy.min(wave_list)
    for i in range(10):
        while 1:
            if int(abs(wave_list[i]))< (0.15* L):
               wave_list.remove(wave_list[i])
            else:
                break
        while 1:
            if int(abs(wave_list[-1-i]))< (0.15* L):
                wave_list.remove(wave_list[-1-i])
            else:
                break
     
    return(wave_list)

def sound(pathfile):
    wf = wave.open(pathfile,"rb")
    #创建PyAudio对象
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True)
    nframes = wf.getnframes()
    framerate = wf.getframerate()
    #读取完整的帧数据到str_data中，这是一个string类型的数据
    str_data = wf.readframes(nframes)
    wf.close()
    #将波形数据转换为数组
    # A new 1-D array initialized from raw binary or text data in a string.
    wave_data = numpy.fromstring(str_data, dtype=numpy.short)
    #将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
    #wave_data.shape = -1,2
    #将数组转置
    #wave_data = wave_data.T
    #time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
    wave_data1=filtering(wave_data)
    time = numpy.arange(0,nframes*len(wave_data1)/len(wave_data))*((1.0/framerate)*len(wave_data1)/len(wave_data))
    #绘制波形图
    pylab.plot(time, wave_data1)
    pylab.subplot(212)
    pylab.plot(time, wave_data1, c="g")
    pylab.xlabel("time (seconds)")
    pylab.show()
    return(wave_data1)

def analysis(list1,list2):
    if type(list1)!=type([]):
        list(list1)
        list(list2)
        
    m=len(list1)
    n=len(list2)

    v0=list(range(m+1))
    v1=list(range(m+1))
    v1[0]=0

    if m==0 or n==0:
        print('list is empty')
        return(0)
    else:
        for j in range(n):
            v1[0]=v1[0]+1
            for i in range(m):
                if str(list1[i])==str(list2[j]):
                    cost=0
                else:
                    cost=1
                
                v1[i+1]=min(v1[i]+1,v0[i+1]+1,v0[i]+cost)

            for nn in range(m+1):
                v0[nn]=v1[nn]
        result=1-v1[-1]/max(m,n)

        return(result)

one=sound("E:\\workspace\\python\\recently\\音频\\1.wav")
two=sound("E:\\workspace\\python\\recently\\音频\\2.wav")
b=time.time()
print('音频耗时：'+str(int(b-a)))
print('相似度为：'+str(round(analysis(one,two)/0.01151857,3)))
c=time.time()
print('分析耗时：'+str(int(c-b)))
print('总耗时：'+str(int(c-a)))
