import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0, 3*np.pi,100)# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
y=np.sin(x)#正弦波
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
plt.rcParams['axes.unicode_minus']=False#显示负号
plt.subplot(1,2,1)#一行二列第一个图
plt.title(r'$f(x)=sin(x)$')#标题
plt.plot(x,y)#x轴数据，y轴数据来绘制点和线
x1=[t*0.375*np.pi for t in x]
y1=np.sin(x1)#正弦波
plt.subplot(1,2,2)#一行二列第二个图
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8}\pi$')#标题
plt.plot(x,y1)#x轴数据，y轴数据来绘制点和线
plt.show()#显示