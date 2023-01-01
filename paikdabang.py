import random
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
  '코코넛카페라떼',
  '더블에스프레소',
  '에스프레소콤프레또'
]
for i in range(0,11):
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
  '코코넛카페라떼',
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
for i in range(0,16):
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
# f=open("메뉴 리스트.hwp","w")
# for row in menu:
#   for item in row:
#     f.write(item)
#     f.write('\n')
#   f.write('\n')

# f.close()

f=open("빽다방 메뉴 연습_new.hwp","w")
for n in range(1,201):
  total=random.choices(range(2,11),weights=[10,15,10,10,2,2,2,2,1])
  total=total[0]
  current=0
  order=[]
  while(current<total):
    # [coffee_Hot,coffee_Iced,nonCoffee_Hot,nonCoffee_Iced,juiceAde,paiksccino,icecream,smoothie,blackpearl,tea_Hot,tea_Iced,dessert]
    cIdx=random.choices(range(0,11),weights=[20,10,20,10,5,15,5,10,10,15,5,5])
    cIdx=cIdx[0]
    selectedMenu=random.choice(menu[cIdx])
    if(selectedMenu not in order):
      order.append(selectedMenu)
      current+=1
  
  f.write("Order No.{}".format(n).center(26,'='))
  f.write('\n')
  for elem in order:
    f.write(elem)
    f.write('\n')
  f.write('\n')
  f.write("\n")
  f.write('\n')
  

