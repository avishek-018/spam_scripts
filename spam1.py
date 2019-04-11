from fbchat import Client
from fbchat.models import *

email='your_fb_email'
passwd='password'

client = Client(email, passwd)
th_id='thread_id'
'''
in your pc, goto fb inbox, and hover your mouse over a friend's conversation,
you will see the th_id at the bottom_left of your browser
ex: https://www.facebook.com/messages/t/100011123456789
th_id = '100011123456789'
'''
start=1
end  =100 #no of time to repeat the same message
while(start!=end+1):
    client.send(Message(text='Happy Spamming '+str(start)), thread_id=th_id, thread_type=ThreadType.USER)
    start+=1
