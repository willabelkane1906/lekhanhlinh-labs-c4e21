from gmail import GMail, Message
mail = GMail('linhmeo99ht@gmail.com','@fre3dOm')
body = '''
Sếp ơi , hôm nay em bị ốm nên sếp cho em nghỉ buổi hôm nay nhé!
Em sẽ hoàn thành công việc ngay sau khi trở lại.'''
msg = Message('Khánh Linh - Xin nghỉ phép',to='lekhanhlinh811@gmail.com',html=body)

import datetime
now = datetime.datetime.now()
while True:
    h = now.hour
       if h == 7:
        mail.send(msg)
        break

print("done")