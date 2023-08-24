import telebot
import random
import time

# Set up the bot
TOKEN = "6551266015:AAF42H87DRXfMcIMcSDMzb46Y6LstHcUW00"
bot = telebot.TeleBot(TOKEN)

# Emojis for outcomes
WIN_EMOJI = "🎉"
LOSE_EMOJI = "😞"
TIE_EMOJI = "🤝"

# Rock-paper-scissors images
IMAGE_URLS = {
    "rock": "https://pixabay.com/vectors/rock-paper-scissors-rock-hand-296854/",
    "paper": "https://pixabay.com/vectors/rock-paper-scissors-paper-hand-296855/",
    "scissors": "https://pixabay.com/vectors/rock-paper-scissors-scissors-hand-296853/"
}

# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        telebot.types.InlineKeyboardButton(text='Rock', callback_data='rock'),
        telebot.types.InlineKeyboardButton(text='Paper', callback_data='paper'),
        telebot.types.InlineKeyboardButton(text='Scissors', callback_data='scissors')
    )
    bot.reply_to(message, "Welcome to Rock-Paper-Scissors!\nChoose your move:", reply_markup=markup)

# Handle callback queries
@bot.callback_query_handler(func=lambda call: call.data in ['rock', 'paper', 'scissors'])
def callback_query(call):
    user_choice = call.data
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = get_winner(user_choice, computer_choice)
    response = f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}"
    user_choice_photo = IMAGE_URLS[user_choice]
    computer_choice_photo = IMAGE_URLS[computer_choice]

    bot.send_photo(call.message.chat.id, user_choice_photo)
    bot.send_photo(call.message.chat.id, computer_choice_photo)
    bot.send_message(call.message.chat.id, response)

def get_winner(user_choice, computer_choice):
    time.sleep(1)  # Simulate a delay for a simple animation

    user_emoji = ""
    computer_emoji = ""
    outcome = ""

    if user_choice == computer_choice:
        outcome = "It's a tie!"
        user_emoji = computer_emoji = TIE_EMOJI
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        outcome = "You win!"
        user_emoji = WIN_EMOJI
        computer_emoji = LOSE_EMOJI
    else:
        outcome = "Computer wins!"
        user_emoji = LOSE_EMOJI
        computer_emoji = WIN_EMOJI

    return f"{user_choice.upper()} {user_emoji} vs {computer_choice.upper()} {computer_emoji}\n{outcome}"

if __name__ == "__main__":
    bot.polling()
