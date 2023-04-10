import schedule
from decouple import config

import notifier
import scanner

# bot and chat ids
# <your bot API >
# '6218757409:AAHgyBeaUhUr_Do0px2vbgwiyHCPGbs3JkY'
botApiToken = config('BOT_API_TOKEN')
chat_id = config('CHAT_ID')  # '77418456'  # <your chat id >
eggSummaryPage = config('EGG_PAGE')  # 'https://netcup-eier.deployn.de/'


def process():
    results = scanner.scan(
        eggSummaryPage, ['RS 1000', 'RS 2000'])
    if len(results) > 0:
        notifier.send_message(botId=botApiToken, chat_id=chat_id,
                              text='Found easteregg(s) for you: ' + ''.join(results))

    print("process completed")


# schedule crawler
schedule.every(60).seconds.do(process)


# run script infinitely
while True:
    schedule.run_pending()
