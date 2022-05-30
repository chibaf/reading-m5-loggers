class m5logger:
    
  def read_logger(self,ser):
    import serial
    line = ser.readline()
    while True:
      try:
        line2=line.strip().decode('utf-8')
      except UnicodeDecodeError:
        line = ser.readline()
        continue
      break
    data = [str(val) for val in line2.split(",")]
    data1=[]
    for i in range(0,10):
      try:
        data1.append(float(data[i+2]))
      except IndexError:
        data1=[0.0]*10
        break
    return data1