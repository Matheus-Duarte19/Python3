medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a \n{}km \n{}hm \n{:2f}dam \n{}dm \n{}cm \n{}mm'.format(medida, km, hm, dam, dm, cm, mm))