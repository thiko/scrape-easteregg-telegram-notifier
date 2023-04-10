import requests


def send_message(botId, chat_id, text):
    '''
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot, 
          text = string; crawled text to be sent
    Returns: None
    '''

    parameters = {'chat_id': chat_id, 'text': text}
    apiURL = f'https://api.telegram.org/bot{botId}/sendMessage'
    message = requests.post(apiURL, data=parameters)
