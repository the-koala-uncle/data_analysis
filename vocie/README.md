plan
-
1)录制音频
2)滤波，把首尾端的静音切除，降低对后续步骤造成的干扰
3)通过算法对比音频的相似度


content
-
01_voice_recording.py(音频录制）
02_sound_map.py（波形图、声频图）




-
journal
-
01_voice_recording(通过）
02_sound_map.py（借鉴）

直接把波形读取出来，曲线形式
先滤波，然后进行波形比对，这里我用的Levenshtein算法+EPD端点检测算法。

在国外论坛找到了一大堆算法例如：MFCC 12维语音特征算法，ZCR 过0检测算法，EPD端点检测算法，GMM拟合数据分布算法，SI语音近似算法


point
-
1）耳塞录制的音频是单声道的，双声道是左右左右……排列的
