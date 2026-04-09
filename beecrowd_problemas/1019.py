t = int(input())

h = t//3600
m = (t%3600)//60
s = t - h*3600 - m*60

print(f"{h}:{m}:{s}")
