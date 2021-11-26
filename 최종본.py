juice = '''

            *******************************
             **                             **
              *                            *
                *                        *
             *                              *
            *                                *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *           delicious juice         *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *                                   *
          *********************************

'''

menu = '''

                     싱글싱글 국산 생과일 100%
                            주스 키오스크

                             - 메 뉴 -
                      
      1 : 오렌지 주스 + 바나나 주스  3800원 - 오렌지(국산), 바나나(국산)
      2 : 딸기 주스 + 블루베리 주스 4600원 - 딸기(국산), 블루베리(국산)
      3 : 멜론 주스 + 키위 주스 5200원 - 멜론(국산), 키위(국산)

      * 수제쿠키 = 하루에 20개씩만 판매합니다. (한 사람당 한 개씩만 구매 가능합니다!

'''

print(juice)
print(menu)
print("=" * 70)

juice_price = 0 # 주스 한 잔의 가격
total_price = 0 # 총 주문 금액
change = 0 # 거스름돈

order = int( input("주스  종류를 선택하세요. 번호 입력 >>>> "))

if order == 1 :
    juice_price = 3800
elif order == 2 :
    juice_price = 4600
elif order == 3 :
    juice_price = 5200


cups = int( input("몇 잔을 드릴까요? >>>> "))
total_price = juice_price * cups

received = int( input(f"총 금액은 {total_price}원 입니다. 돈을 투입해 주세요 >>>> "))

if received >= total_price:
    change = received - total_price
    print(f"{received}원을 받았습니다. 거스름돈은 {change}원입니다.")
    
else:
     print("금액이 부족합니다. 주문이 취소되었습니다.")
    
