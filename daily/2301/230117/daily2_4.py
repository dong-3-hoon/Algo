# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

price=int(input())
vat=int(price*0.15)
total=int(price+vat)
print(f"스테이크: {price}\n+VAT: {vat}\n총계: {total}")
#print(f"스테이크: {price:>5}\n+VAT: {vat}\n총계: {total}")
#print(f"스테이크: {price:>10}\n+VAT: {vat}\n총계: {total}")

'''
:>len 오른쪽정렬, len 만큼 칸을 확보
:<len 왼쪽 정렬, len 만큼 칸을 확보
:^len 가운데 정렬 len만큼 칸을 확보
'''