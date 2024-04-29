def reverse(str):
  str1 = ''
  for s in str[::-1]:
    str1=str1+s
  return str1


def new_avg(arr, navg):
  sum = 0
  for i in range(len(arr)):
    sum = sum + arr[i]
  a=(len(arr)+1)*navg - sum
  if a<0:
    return ValueError
  else:
    return a

def sum_sequence(b,f,s):
  sum=0
  for i in range(b,f+1,s):
    return sum

def max_diff(lst):
  if lst:
    max=lst[0]
    min=lst[0]
    for l in lst:
      if l<min:
       min=l
      if l>max:
       max=l
    d=max-min
    return d
  else:
    return 0


def countSmileys(lst):
  count=0
  for l in lst:
    if len(l)==2:
      if l[0] in (":",';') and l[1] in (')','D'):
        count=count+1
    if len(l)==3:
      if l[0] in (":",';') and l[1] in ('-','~') and l[2] in (')','D'):
        count=count+1
  return count


def Sentence_Count(str):
  count=0
  for s in str:
    if s in ('.','?','!'):
      count=count+1
  return count


def tortoise_racing(v1,v2,s):
  if v2>v1:
    t=s/(v2-v1)
  else:
    return [-1,-1,-1]
  lst=[]
  lst.append(int(t))
  lst.append(int((t%1)*60))
  lst.append(round((t%1*60)%1*60))
  return lst


def Calc_String_Rotation(str1,str2):
  for i in range(len(str1)):
    if str2[i:]+str2[:i]==str1:
      return i
  return '-1'
