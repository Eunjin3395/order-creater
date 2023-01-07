import random
import unicodedata

def fill_str_with_space(input_s="", max_size=40, fill_char=" "):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)


# catText와 catWeight 리스트 생성
# catText --> category 이름 string으로 구성된 리스트
# catWeight --> category별 weight int로 구성된 리스트
def setCategory(ver):
  global catText
  global catWeight
  global catNum
  # category.txt 읽어오기, 개행문자 제거
  temp=[]
  f=open('./settings/'+ver+'/category.txt','r')
  lines=f.readlines()
  for line in lines:
    line=line.strip()
    line=line.rstrip('\n')
    temp.append(line)
  f.close()

  # category.txt에서 , 기준으로 카테고리 이름과 카테고리 가중치 분리해 리스트에 저장하기
  catText=[]
  catWeight=[]
  for elem in temp:
    name,num=elem.split(',')
    catText.append(name)
    catWeight.append(int(num))
  catNum=len(catText)


# txt 읽어와서 menu dictonary 완성하기
# menu --> 'category' : [[menu list],[weight list]]로 구성된 딕셔너리
def setMenu(ver):
  global menu
  menu={}
  for cat in catText:
    f=open('./settings/'+ver+'/'+cat+'.txt','r')
    lines=f.readlines()
    menuText=[]
    menuWeight=[]
    for line in lines:
      line=line.strip()
      line=line.rstrip('\n')
      name,num=line.split(',')
      menuText.append(name)
      menuWeight.append(int(num))
    menu[cat]=[menuText,menuWeight]


class Order:
  def __init__(self):
    self.totalNum=int(random.choices(list(range(2,15)),[2,18,18,18,10,8,4,1,1,1,1,1,1])[0]) # 가중치 적용해 총 잔 수 지정
    self.divNum=[0]*catNum #카테고리별로 지정된 음료 잔수에 대한 리스트
    self.totalDict={} #'음료': n잔 쌍으로 이루어진 dict, 중복 거름

  def setQuan(self): # setting divNum array -> 총 잔 수를 음료 카테고리별로 랜덤 분배하기 
    while(sum(self.divNum)<self.totalNum):
      index=int(random.choices(list(range(0,catNum)),catWeight)[0]) #음료 카테고리를 랜덤으로 뽑기
      if(self.totalNum>=4):
        q=random.randint(1,int(self.totalNum*0.6)) #그 카테고리에 지정될 잔 수 랜덤 뽑기(1~총 잔수의 50%)까지 가능
      else:
        q=random.randint(1,int(self.totalNum))
      if(sum(self.divNum)+q>self.totalNum): #그 카테고리에 q를 더함으로써 합이 총 잔수를 초과하는 경우
        self.divNum[index]+=self.totalNum-sum(self.divNum)
      else:
        self.divNum[index]+=q

  def setMenu(self): # setting totalDict -> 음료 카테고리별 수량을 음료 메뉴별로 랜덤 지정하기
    index=0 # 각 분류의 index
    for q in self.divNum: #리스트 돌며 각 분류별 메뉴 랜덤 선택 및 잔수 지정
      if(q>0): # 해당 분류에 할당된 잔 수가 존재할 경우
        curr=0 # 현재까지 해당 분류에 추가한 잔 수
        while(curr<q): # 현재까지 추가한 잔 수가 총 잔수보다 작을 때만
          quanToAdd=random.randint(1,q-curr) # 잔 수 랜덤 지정
          curr+=quanToAdd # 현재까지 추가한 잔 수 업데이트
          menuToAdd=random.choices(menu[catText[index]][0],menu[catText[index]][1])[0] # 잔 수를 추가할 음료메뉴 선정
          if(menuToAdd in self.totalDict): # 이전에 추가된 적 있는 메뉴가 선정됐을 경우 -> 수량만 더해줌
            self.totalDict[menuToAdd]+=quanToAdd
          else: # 처음 추가하는 메뉴인 경우 dict에 값 추가
            self.totalDict[menuToAdd]=quanToAdd
      index+=1 # 다음 카테고리로 넘어가기 위한 인덱스 업데이트    

  def print(self,file,i):
    file.write("Order No.{}".format(i).center(28,'='))
    print("Order No.{}".format(i).center(32,'='))
    file.write('\n')

    for item,quan in self.totalDict.items():
      menuName=fill_str_with_space(item,max_size=24)
      s='{0}{1:>6}'.format(menuName,quan)
      print(s)
      file.write(s)
      file.write('\n')


print("Order Creater Started".center(60,'*'))
orders=int(input("1. 생성하고자 하는 주문 건수를 입력하세요. (MAX:1000)>>"))
while(orders>1000):
  orders=int(input("1. 생성하고자 하는 주문 건수를 입력하세요. (MAX:1000)>>"))

version=input("2. 생성하고자 하는 주문의 계절 버전을 입력하세요. (1:여름, 2:겨울) >>")
while (version!='1' and version!='2'):
  version=input("2. 생성하고자 하는 주문의 계절 버전을 입력하세요. (1:여름, 2:겨울) >>")

if(version=='1'):
  version='summer'
elif(version=='2'):
  version='winter'

setCategory(version)
setMenu(version)

f=open("빽다방 메뉴 연습 "+str(orders)+"개_"+version+"_ver.hwp","w",encoding='utf-8')
i=0
while(i<orders):
  i+=1
  NewOrder=Order()
  NewOrder.setQuan()
  NewOrder.setMenu()
  NewOrder.print(f,i)  
  f.write('\n\n\n\n')
  print('\n')
print(('File of '+str(orders)+' orders created').center(60,'*'))

f.close()


