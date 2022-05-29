class m5logger:
    
  def read_logger(self,ser):
    import serial
    line = ser.readline()
    line2=line.strip().decode('utf-8')
    data = [str(val) for val in line2.split(",")]
    data1=[]
    for i in range(0,10):
      data1.append(float(data[i+2]))
    return data1