multi=[['A',3],['B',5],['C',7]]
for x,y in multi:
    print(x,'=',y)

m1=[[1,2,3],
    [4,5,6],
    [7,8,0]]
m2=[1,0,1]
m3=[0,0,0]
for i in range(0,3,1):
    for j in range(0,3,1):
        m3[i]+=(m1[i][j]*m2[j])
print(m3)