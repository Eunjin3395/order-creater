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


coffee_Hot=[
  '앗메리카노',
  '빽\'s 카페라떼',
  '원조커피',
  '바닐라라떼',
  '달달연유라떼',
  '카페모카',
  '카라멜마끼아또',
  '달고나원조커피',
  '달고나카페라떼',
  '달고나카라멜라떼',
  '더블에스프레소',
  '에스프레소콤프레또'
]
for i in range(0,10):
  coffee_Hot[i]+="(HOT)"

coffee_Iced=[
  '앗메리카노',
  '빽사이즈 앗메리카노',
  '빽\'s 카페라떼',
  '빽사이즈 빽\'s 카페라떼',
  '원조커피',
  '빽사이즈 원조커피',
  '아이스티샷추가',
  '빽사이즈 아이스티샷추가',
  '바닐라라떼',
  '달달연유라떼',
  '카페모카',
  '카라멜마끼아또',
  '달고나원조커피',
  '달고나카페라떼',
  '달고나카라멜라떼',
  '콜드브루',
  '콜드브루라떼',
  '콜드브루흑당라떼',
  '콜드브루연유라떼',
  '디카페인콜드브루',
  '디카페인콜드브루라떼',
  '디카페인콜드브루흑당라떼',
  '디카페인콜드브루연유라떼',
  '아이스크림카페라떼',
  '아이스크림바닐라라떼',
  '아이스크림카페모카'
]
for i in range(0,15):
  coffee_Iced[i]+="(ICED)"

nonCoffee_Hot=[
  '초코라떼',
  '녹차라떼',
  '토피넛라떼',
  '민트초코라떼',
  '고구마라떼',
  '꿀밤라떼',
  '오트라떼'
]
for i in range(0,7):
  nonCoffee_Hot[i]+="(HOT)"

nonCoffee_Iced=[
  '초코라떼',
  '빽사이즈 초코라떼',
  '녹차라떼',
  '토피넛라떼',
  '민트초코라떼',
  '고구마라떼',
  '꿀밤라떼',
  '오트라떼',
  '딸기라떼',
  '미숫가루',
  '청포도플라워',
  '아이스미초'
]
for i in range(0,8):
  nonCoffee_Iced[i]+="(ICED)"

juiceAde=[
  '완전딸기주스',
  '완전토마토주스',
  '완전블루베리주스',
  '완전망고주스',
  '딸기에이드',
  '유자에이드',
  '깔라만시에이드',
  '청포도에이드',
  '자몽에이드',
  '복숭아에이드',
  '미초에이드',
  '레모네이드'
]

paiksccino=[
  '딸기바나나빽스치노',
  '초코바나나빽스치노',
  '녹차빽스치노',
  '원조빽스치노',
  '민트초코빽스치노',
  '피스타치오빽스치노',
  '초코빽스치노',
  '딸기빽스치노',
  '쿠키크런치빽스치노',
  '퐁당치노 바닐라',
  '퐁당치노 미숫가루',
  '퐁당치노 원조'
]
for i in range(0,9):
  paiksccino.append(paiksccino[i]+"(소프트)")
  paiksccino[i]+="(베이직)"

icecream=[
  '노말한 소프트'
  '노말한 소프트(+카라멜)',
  '노말한 소프트(+초콜릿)',
  '달고나크런치',
  '아포가토'
]

smoothie=[
  '고구마스무디',
  '코코넛커피스무디',
  '플레인요거트스무디',
  '딸기요거트스무디',
  '블루베리요거트스무디',
  '밀크쉐이크'
]

blackpearl=[
  '블랙펄라떼',
  '블랙펄카페라떼',
  '블랙펄밀크티'
]

tea_Hot=[
  '피치우롱스위티',
  '우롱티',
  '밀크티',
  '레몬티',
  '유자티',
  '자몽티',
  '레몬얼그레이',
  '오렌지자몽블랙',
  '페퍼민트',
  '황금캐모마일',
  '깔라만시티'
]
for i in range(0,10):
  tea_Hot[i]+="(HOT)"

tea_Iced=[
  '아이스티',
  '빽사이즈 아이스티',
  '피치우롱스위티',
  '우롱티',
  '밀크티',
  '레몬티',
  '유자티',
  '자몽티',
  '레몬얼그레이',
  '오렌지자몽블랙',
  '페퍼민트',
  '황금캐모마일'
]
for i in range(2,12):
  tea_Iced[i]+="(ICED)"

dessert=[
  '고메버터 소금빵',
  '맛카롱(순우유)',
  '맛카롱(초코크런치)',
  '맛카롱(딸기크런치)',
  '사라다빵',
  '빽그램핫도그',
  '크리미슈',
  '크리미단팥빵',
  '큰마들렌(오리지널)',
  '네모머핀(초콜릿)',
  '긴페스츄리와플',
  '순삭쿠키(코코아더블초코)',
  '순삭쿠키(청키초코)',
  '순삭쿠키(청키화이트초코)'
]

menu=[coffee_Hot,coffee_Iced,nonCoffee_Hot,nonCoffee_Iced,juiceAde,paiksccino,icecream,smoothie,blackpearl,tea_Hot,tea_Iced,dessert]

class Order:
  def __init__(self):
    self.totalNum=int(random.choices(list(range(2,15)),[2,18,18,18,12,8,8,1,1,1,1,1,1])[0]) # 가중치 적용해 총 잔 수 지정
    # [coffee_Hot,coffee_Iced,nonCoffee_Hot,nonCoffee_Iced,juiceAde,paiksccino,icecream,smoothie,blackpearl,tea_Hot,tea_Iced,dessert]
    self.divNum=[0]*12 #카테고리별로 지정된 음료 잔수에 대한 리스트
    self.totalDict={} #'음료': n잔 쌍으로 이루어진 dict, 중복 거름

  def setQuan(self): # setting divNum array -> 총 잔 수를 음료 카테고리별로 랜덤 분배하기 
    while(sum(self.divNum)<self.totalNum):
      index=int(random.choices(list(range(0,12)),[20,10,20,10,5,15,5,10,10,15,5,5])[0]) #음료 카테고리를 랜덤으로 뽑기
      if(self.totalNum>=4):
        q=random.randint(1,int(self.totalNum*0.6)) #그 카테고리에 지정될 잔 수 랜덤 뽑기(1~총 잔수의 80%)까지 가능
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
          menuToAdd=random.choice(list(menu[index])) # 잔 수를 추가할 음료메뉴 선정
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




orders=200

f=open("빽다방 메뉴 연습 "+str(orders)+"개.hwp","w",encoding='utf-8')
# f = open(str(orders)+'orders.hwp','w', encoding='utf-8') # 로그 저장할 file open 
i=0
while(i<orders):
  i+=1
  NewOrder=Order()
  NewOrder.setQuan()
  NewOrder.setMenu()
  NewOrder.print(f,i)  
  f.write('\n\n\n\n')
  print('\n')
print(('File of '+str(orders)+' orders created').center(50,'='))

print(NewOrder.totalDict)
f.close()
# for n in range(1,201):
#   total=random.choices(range(2,11),weights=[10,15,10,10,2,2,2,2,1])
#   total=total[0]
#   current=0
#   order=[]
#   while(current<total):
#     # [coffee_Hot,coffee_Iced,nonCoffee_Hot,nonCoffee_Iced,juiceAde,paiksccino,icecream,smoothie,blackpearl,tea_Hot,tea_Iced,dessert]
#     cIdx=random.choices(range(0,11),weights=[20,10,20,10,5,15,5,10,10,15,5,5])
#     cIdx=cIdx[0]
#     selectedMenu=random.choice(menu[cIdx])
#     if(selectedMenu not in order):
#       order.append(selectedMenu)
#       current+=1
  
#   f.write("Order No.{}".format(n).center(26,'='))
#   f.write('\n')
#   for elem in order:
#     f.write(elem)
#     f.write('\n')
#   f.write('\n')
#   f.write("\n")
#   f.write('\n')
  

