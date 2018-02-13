z=1
p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while z==1:
 print(p)
 print('player 1 turn')
 print('enter the first number')
 x=int(input())
 if x>20 or x<0:
     while x>20 or x<0:
      print("enter a valid number")
      x=int(input())
     p[x]='-'
 if p==['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']:
     print('player 1 wins')
     break
 print('do you want to pick another number(y/n)')
 r=input()
 if r=='y':
   print('enter the second number')
   y=int(input())
   if y>20 or y<0:
      while y>20 or y<0:
           print("enter a valid number")
           y=int(input())           
   if y==x+1 or y==x-1:
     p[y]='-'
   else:
       while y!=(x+1) or y!=(x-1):
         print("enter a valid number")
         y=int(input())
 y='-'  
 if r=='n':
     pass
 p[x]='-'
 if p==['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']:
     print('player 1 wins')
     break
 print(p)
 print('player 2 turn')
 print('enter the first number')
 x=int(input())
 if x>20 or x<0:
     print("enter a valid number")
     x=int(input())
     p[x]='-'
 if p==['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']:
     print('player 1 wins')
     break
 print('do you want to pick another number(y/n)')
 r=input()
 if r=='y':
   print('enter the second number')
   y=int(input())
   if y>20 or y<0:
       print("enter a valid number")
       y=int(input())
       p[y]='-'
   if y==x+1 or y==x-1:
     p[y]='-'
   else:
       print("enter a valid number")
       y=int(input())
       p[y]='-'
 if r=='n':
     pass
 p[x]='-'
 if p==['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']:
     print('player 2 wins')
     break
