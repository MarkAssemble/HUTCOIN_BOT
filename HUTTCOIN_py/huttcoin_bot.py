from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 봇 토큰과 채널 ID 설정
TOKEN = "7835117755:AAEZS39HlkciLSw3xFUeSGJeQNFreYkI-Qw"
CHANNEL_ID = "-1002604713189"  # HUTTCOIN 채널 ID

# 환영 메시지 전송 함수
async def send_welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome_text = """🎉 환영합니다! 

이곳은 **HUTTCOIN 커뮤니티**입니다.
HUTTCOIN은 헛짓거리와 재미를 추구하는 코인입니다.

✅ 사용 가능한 명령어 안내:
- /start : 환영 메시지 보기 👋
- /chart : HUTTCOIN 가격 변동 차트 보기 📈
- /x : HUTTCOIN의 최신 정보 확인 🔍
- /homepage : 공식 홈페이지 방문 🌐

💬 커뮤니티 규칙:
1. 헛짓거리를 즐기되, 서로를 존중해주세요.
2. 자유롭게 의견을 나누고, 아이디어를 공유하세요!

지금 바로 /chart, /x, /homepage 명령어를 입력하여 더 많은 정보를 확인해보세요! 🚀"""

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=welcome_text
        )
        print(f"✅ 환영 메시지 전송 완료!")
    except Exception as e:
        print(f"오류 발생: {e}")

# 명령어 처리 함수
async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 HUTTCOIN 차트 페이지: https://huttcoin.com/chart")

async def x(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 HUTTCOIN 최신 정보: https://huttcoin.com/info")

async def homepage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌐 HUTTCOIN 공식 홈페이지: https://huttcoin.netlify.app")

# 채널 명령어 처리 함수
async def handle_channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        text = update.channel_post.text
        print(f"✅ 채널 명령어 수신: {text}")

        if text.startswith('/chart'):
            await update.channel_post.reply_text("📈 HUTTCOIN 차트 페이지: https://huttcoin.com/chart")
        elif text.startswith('/x'):
            await update.channel_post.reply_text("🔍 HUTTCOIN 최신 정보: https://huttcoin.com/info")
        elif text.startswith('/homepage'):
            await update.channel_post.reply_text("🌐 HUTTCOIN 공식 홈페이지: https://huttcoin.netlify.app")
        elif text == "/start":
            await send_welcome_message(update, context)
        else:
            await update.message.reply_text("❗ 알 수 없는 명령어입니다.")
# 그룹 명령어 처리 함수
async def handle_group_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(f"✅ 그룹 명령어 수신: {text}")

    if text == "/chart":
        await update.message.reply_text("📈 HUTTCOIN 차트 페이지: https://huttcoin.com/chart")
    elif text == "/x":
        await update.message.reply_text("🔍 HUTTCOIN 최신 정보: https://huttcoin.com/info")
    elif text == "/homepage":
        await update.message.reply_text("🌐 HUTTCOIN 공식 홈페이지: https://huttcoin.netlify.app")
    elif text == "/start":
        await send_welcome_message(update, context)
    else:
        await update.message.reply_text("❗ 알 수 없는 명령어입니다.")

# 봇 실행 메인 함수
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # 명령어 핸들러 추가
    application.add_handler(CommandHandler("start", send_welcome_message))
    application.add_handler(CommandHandler("chart", chart))
    application.add_handler(CommandHandler("x", x))
    application.add_handler(CommandHandler("homepage", homepage))

    # 채널 명령어 핸들러 추가
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL & filters.TEXT, handle_channel_command))
    # 그룹 명령어 핸들러 추가
    application.add_handler(MessageHandler(filters.ChatType.GROUP & filters.TEXT, handle_group_command))

    # 폴링 방식으로 실행
    print("✅ HUTTCOIN 봇이 실행 중입니다...")
    application.run_polling()

# 실행 시작
if __name__ == "__main__":
    main()