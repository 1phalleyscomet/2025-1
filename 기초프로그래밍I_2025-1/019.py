import time
start_time = time.monotonic()
time.sleep(3)
print(start_time)
fa=1
for i in range(1,100,1):
    fa*=i
print(fa)
end_time=time.monotonic()
print(end_time)
print(end_time-start_time)
