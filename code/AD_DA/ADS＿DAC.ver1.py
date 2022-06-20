import time
import datetime
import ADS1256
import RPi.GPIO as GPIO
import csv #,os

#日時と動作の種類の設定
date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
action = 'air'
#round = '1'

GPIO.setmode(GPIO.BCM)
channel = 24
GPIO.setup(channel,GPIO.OUT)

try:
    print("Program start\r\n")
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    path = "../data/{0}_{1}.csv".format(date,action)
    with open(path,'w') as f:
        writer = csv.writer(f,lineterminator='\n')
        t_start = time.time()
        for i in range(250):
                ADC_Value = ADC.ADS1256_GetAll()
                GPIO.output(channel,GPIO.HIGH)
                I_tx1_rx1 = int(ADC_Value[0]*5000/0x7fffff)
                Q_tx1_rx1 = int(ADC_Value[1]*5000/0x7fffff)
                I_tx1_rx2 = int(ADC_Value[2]*5000/0x7fffff) 
                Q_tx1_rx2 = int(ADC_Value[3]*5000/0x7fffff)
                time.sleep(0.001)
                GPIO.output(channel,GPIO.LOW)
                I_tx2_rx1 = -(int(ADC_Value[0]*5000/0x7fffff))
                Q_tx2_rx1 = -(int(ADC_Value[1]*5000/0x7fffff))
                I_tx2_rx2 = -(int(ADC_Value[2]*5000/0x7fffff))
                Q_tx2_rx2 = -(int(ADC_Value[3]*5000/0x7fffff))
                #print (i,I1,Q1,I2,Q2,I3,Q3,I4,Q4)
                writer.writerow([i,I_tx1_rx1,Q_tx1_rx1,I_tx1_rx2,Q_tx1_rx2
                ,I_tx2_rx1,Q_tx2_rx1,I_tx2_rx2,Q_tx2_rx2])
                time.sleep(0.001)


except:
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
t_fin = time.time()
# 測定時間の記録
print(float(t_fin-t_start))

