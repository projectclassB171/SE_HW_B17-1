# coding=gbk
ji=0
tu=30-ji
for ji in range(1,30):
    for tu in range(1,30):
         if ji+tu == 30:
            if tu*4+ji*2 == 90:
              print("����:",ji,"������:",tu)

