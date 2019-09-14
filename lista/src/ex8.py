medida = float(input('Uma diatancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}cm e {}mm'
      .format(medida,km,hm,dam,cm, mm))