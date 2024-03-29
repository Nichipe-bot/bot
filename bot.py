import discord
from discord.ext import commands
import os

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("ㄹㅇㅋㅋ")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        # message.content = message의 내용
        if "ㄹㅇㅋㅋ" in message.content:
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㄹㅇㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if "됬" in message.content:
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "'됬'은 서버 금지어입니다"
            # msg에 지정된 내용대로 메시지를 전송
            await message.delete()
            await channel.send(msg)
            return None
        
        if "<:fdzz:828259889461461022>" in message.content:
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 
            # msg에 지정된 내용대로 메시지를 전송
            # emoji = get(bot.get_all_emojis(), name='fdzz') # 이모지 객체
            await channel.send("<:fdzz:828259889461461022>")
            return None
        


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(os.environ['token'])
