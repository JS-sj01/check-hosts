#f = open("connect_result.log",'r')
#mylist = f.readlines(10)
#print(mylist)


with open('connect_result.log','r') as f:
   data = f.readlines()

   for line in data:
       odom = line.split()
       numbers_float = map(float, odom)
       print(numbers_float)
