sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
a=set(sequence_0)
if len(sequence_0)==len(a):
    print("sequence_0, все элементы уникальны")
else:
    print("sequence_0, Последовательность не уникальна.")
b=set(sequence_1)
if len(sequence_1)==len(b):
    print("sequence_1, все элементы уникальны")
else:
    print("sequence_1, Последовательность не уникальна.")
c=set(sequence_2)
if len(sequence_2)==len(c):
    print("sequence_2, все элементы уникальны")
else:
    print("sequence_2, Последовательность не уникальна.")
d=set(sequence_3)
if len(sequence_3)==len(d):
    print("sequence_3, все элементы уникальны")
else:
    print("sequence_3, Последовательность не уникальна.")