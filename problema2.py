import os
dirEntrada = "entrada/"
files = os.listdir(dirEntrada)
dirSalida = "salida/"
ahead=0
wplayer=0
for file in files:
    if (os.path.isfile(os.path.join(dirEntrada,file)) and file.endswith('.txt')):
        with open("entrada/"+file) as getfile:
            for row in getfile:
                splRow=row.split(' ')
                if (len(splRow)>1):
                    preAhead=int(splRow[0])-int(splRow[1])
                    if (abs(preAhead)>ahead):
                        if (preAhead>0):
                            wplayer=1
                        else:
                            wplayer=2
                        ahead=abs(preAhead)
        with open(dirSalida+'salida_'+file, 'w') as f:
            f.write(str(wplayer) + " " + str(ahead))





            