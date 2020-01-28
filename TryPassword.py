
#密碼重試程式

#password = 'a123456'
# while True:
#     password = input('請輸入密碼: ')
#     if password != 'a123456':
#        print ('密碼錯誤!')
#     else:
#        print('登入成功')
#        break
# ---------------------------------------------
# ---------------------------------------------

# 用"while True的寫法"
# x = 3 
# while True:
#     password = input('請輸入密碼: ')
#     if password != 'a123456':
#          x = x - 1
#          print('密碼錯誤! 還有', x, '次機會')
#          if x ==0:
#             break

#     else:
#        print('登入成功')
#        break

# ---------------------------------------------
# ---------------------------------------------

#把"while True"拿掉,變成 while+條件的寫法
x = 3 
while x > 0:
        password = input('請輸入密碼: ')
        if password != 'a123456':
           x = x - 1
           print('密碼錯誤! 還有', x, '次機會')
        else:
          print('登入成功')
          break