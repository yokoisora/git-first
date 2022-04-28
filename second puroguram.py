num = int(input())
if num % 7 == 0 and num > 0:
    print('正の7の倍数')
    
elif num % 7 == 0 and num < 0:
    print('負の７の倍数')
    
elif num % 7 == 1 or num % 7 == 6:
    print('7の倍数のニアピンです')
    
else:
    print('7の倍数ではありません')
exit()