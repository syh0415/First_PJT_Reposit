import sys
from playwright.sync_api import Playwright, sync_playwright
import telegram
import asyncio
import time

sys.stdout.reconfigure(encoding='utf-8')

# 봇 토큰과 채팅 ID 설정
# BOT_TOKEN = '7505977485:AAGv24lXugrL6gb5RlisRX9NvB3Zvc-QEAs'
# CHAT_ID = '7589059359'
bot_message = ""

#N = int(input())
#A = list(map(int,input().split()))
#l,r = 0,N-1
#ans = 2000000000
#p1,p2 = -1,-1
#while l<r and ans>0:
#	val = A[l]+A[r]
#	if abs(val)<ans:
#		ans = abs(val)
#		p1=l
#		p2=r
#	if val<0:
#		l+=1
#	else: 
#		r-=1
#print("good")
# print(p1,p2)

async def send_bot_message_for_test():
    message = "hello telegram, I am Yongho Shin"
    print("bot msg - " + message)
    bot = telegram.Bot(token=BOT_TOKEN)
    await bot.send_message(CHAT_ID, message, "MARKDOWN")

# asyncio.run(send_bot_message_with_numbers())  # 봇 실행하는 코드
asyncio.run(send_bot_message_for_test())
