import telebot
import config
import requests
import urllib.parse
import os
import random
import time
import threading
from telebot import types
import urllib.parse
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#token
Token = config.EverthingToken
bot = telebot.TeleBot(Token)

country_code_to_name = {
  "AF": "Afghanistan",
  "AX": "Åland Islands",
  "AL": "Albania",
  "DZ": "Algeria",
  "AS": "American Samoa",
  "AD": "AndorrA",
  "AO": "Angola",
  "AI": "Anguilla",
  "AQ": "Antarctica",
  "AG": "Antigua and Barbuda",
  "AR": "Argentina",
  "AM": "Armenia",
  "AW": "Aruba",
  "AU": "Australia",
  "AT": "Austria",
  "AZ": "Azerbaijan",
  "BS": "Bahamas",
  "BH": "Bahrain",
  "BD": "Bangladesh",
  "BB": "Barbados",
  "BY": "Belarus",
  "BE": "Belgium",
  "BZ": "Belize",
  "BJ": "Benin",
  "BM": "Bermuda",
  "BT": "Bhutan",
  "BO": "Bolivia",
  "BA": "Bosnia and Herzegovina",
  "BW": "Botswana",
  "BV": "Bouvet Island",
  "BR": "Brazil",
  "IO": "British Indian Ocean Territory",
  "BN": "Brunei Darussalam",
  "BG": "Bulgaria",
  "BF": "Burkina Faso",
  "BI": "Burundi",
  "KH": "Cambodia",
  "CM": "Cameroon",
  "CA": "Canada",
  "CV": "Cape Verde",
  "KY": "Cayman Islands",
  "CF": "Central African Republic",
  "TD": "Chad",
  "CL": "Chile",
  "CN": "China",
  "CX": "Christmas Island",
  "CC": "Cocos (Keeling) Islands",
  "CO": "Colombia",
  "KM": "Comoros",
  "CG": "Congo",
  "CD": "Congo, The Democratic Republic of the",
  "CK": "Cook Islands",
  "CR": "Costa Rica",
  "CI": "Cote D'Ivoire",
  "HR": "Croatia",
  "CU": "Cuba",
  "CY": "Cyprus",
  "CZ": "Czech Republic",
  "DK": "Denmark",
  "DJ": "Djibouti",
  "DM": "Dominica",
  "DO": "Dominican Republic",
  "EC": "Ecuador",
  "EG": "Egypt",
  "SV": "El Salvador",
  "GQ": "Equatorial Guinea",
  "ER": "Eritrea",
  "EE": "Estonia",
  "ET": "Ethiopia",
  "FK": "Falkland Islands (Malvinas)",
  "FO": "Faroe Islands",
  "FJ": "Fiji",
  "FI": "Finland",
  "FR": "France",
  "GF": "French Guiana",
  "PF": "French Polynesia",
  "TF": "French Southern Territories",
  "GA": "Gabon",
  "GM": "Gambia",
  "GE": "Georgia",
  "DE": "Germany",
  "GH": "Ghana",
  "GI": "Gibraltar",
  "GR": "Greece",
  "GL": "Greenland",
  "GD": "Grenada",
  "GP": "Guadeloupe",
  "GU": "Guam",
  "GT": "Guatemala",
  "GG": "Guernsey",
  "GN": "Guinea",
  "GW": "Guinea-Bissau",
  "GY": "Guyana",
  "HT": "Haiti",
  "HM": "Heard Island and Mcdonald Islands",
  "VA": "Holy See (Vatican City State)",
  "HN": "Honduras",
  "HK": "Hong Kong",
  "HU": "Hungary",
  "IS": "Iceland",
  "IN": "India",
  "ID": "Indonesia",
  "IR": "Iran, Islamic Republic Of",
  "IQ": "Iraq",
  "IE": "Ireland",
  "IM": "Isle of Man",
  "IL": "Israel",
  "IT": "Italy",
  "JM": "Jamaica",
  "JP": "Japan",
  "JE": "Jersey",
  "JO": "Jordan",
  "KZ": "Kazakhstan",
  "KE": "Kenya",
  "KI": "Kiribati",
  "KP": "Korea, Democratic People'S Republic of",
  "KR": "Korea, Republic of",
  "KW": "Kuwait",
  "KG": "Kyrgyzstan",
  "LA": "Lao People'S Democratic Republic",
  "LV": "Latvia",
  "LB": "Lebanon",
  "LS": "Lesotho",
  "LR": "Liberia",
  "LY": "Libyan Arab Jamahiriya",
  "LI": "Liechtenstein",
  "LT": "Lithuania",
  "LU": "Luxembourg",
  "MO": "Macao",
  "MK": "Macedonia, The Former Yugoslav Republic of",
  "MG": "Madagascar",
  "MW": "Malawi",
  "MY": "Malaysia",
  "MV": "Maldives",
  "ML": "Mali",
  "MT": "Malta",
  "MH": "Marshall Islands",
  "MQ": "Martinique",
  "MR": "Mauritania",
  "MU": "Mauritius",
  "YT": "Mayotte",
  "MX": "Mexico",
  "FM": "Micronesia, Federated States of",
  "MD": "Moldova, Republic of",
  "MC": "Monaco",
  "MN": "Mongolia",
  "MS": "Montserrat",
  "MA": "Morocco",
  "MZ": "Mozambique",
  "MM": "Myanmar",
  "NA": "Namibia",
  "NR": "Nauru",
  "NP": "Nepal",
  "NL": "Netherlands",
  "AN": "Netherlands Antilles",
  "NC": "New Caledonia",
  "NZ": "New Zealand",
  "NI": "Nicaragua",
  "NE": "Niger",
  "NG": "Nigeria",
  "NU": "Niue",
  "NF": "Norfolk Island",
  "MP": "Northern Mariana Islands",
  "NO": "Norway",
  "OM": "Oman",
  "PK": "Pakistan",
  "PW": "Palau",
  "PS": "Palestinian Territory, Occupied",
  "PA": "Panama",
  "PG": "Papua New Guinea",
  "PY": "Paraguay",
  "PE": "Peru",
  "PH": "Philippines",
  "PN": "Pitcairn",
  "PL": "Poland",
  "PT": "Portugal",
  "PR": "Puerto Rico",
  "QA": "Qatar",
  "RE": "Reunion",
  "RO": "Romania",
  "RU": "Russian Federation",
  "RW": "RWANDA",
  "SH": "Saint Helena",
  "KN": "Saint Kitts and Nevis",
  "LC": "Saint Lucia",
  "PM": "Saint Pierre and Miquelon",
  "VC": "Saint Vincent and the Grenadines",
  "WS": "Samoa",
  "SM": "San Marino",
  "ST": "Sao Tome and Principe",
  "SA": "Saudi Arabia",
  "SN": "Senegal",
  "CS": "Serbia and Montenegro",
  "SC": "Seychelles",
  "SL": "Sierra Leone",
  "SG": "Singapore",
  "SK": "Slovakia",
  "SI": "Slovenia",
  "SB": "Solomon Islands",
  "SO": "Somalia",
  "ZA": "South Africa",
  "GS": "South Georgia and the South Sandwich Islands",
  "ES": "Spain",
  "LK": "Sri Lanka",
  "SD": "Sudan",
  "SR": "Suriname",
  "SJ": "Svalbard and Jan Mayen",
  "SZ": "Swaziland",
  "SE": "Sweden",
  "CH": "Switzerland",
  "SY": "Syrian Arab Republic",
  "TW": "Taiwan, Province of China",
  "TJ": "Tajikistan",
  "TZ": "Tanzania, United Republic of",
  "TH": "Thailand",
  "TL": "Timor-Leste",
  "TG": "Togo",
  "TK": "Tokelau",
  "TO": "Tonga",
  "TT": "Trinidad and Tobago",
  "TN": "Tunisia",
  "TR": "Turkey",
  "TM": "Turkmenistan",
  "TC": "Turks and Caicos Islands",
  "TV": "Tuvalu",
  "UG": "Uganda",
  "UA": "Ukraine",
  "AE": "United Arab Emirates",
  "GB": "United Kingdom",
  "US": "United States",
  "UM": "United States Minor Outlying Islands",
  "UY": "Uruguay",
  "UZ": "Uzbekistan",
  "VU": "Vanuatu",
  "VE": "Venezuela",
  "VN": "Viet Nam",
  "VG": "Virgin Islands, British",
  "VI": "Virgin Islands, U.S.",
  "WF": "Wallis and Futuna",
  "EH": "Western Sahara",
  "YE": "Yemen",
  "ZM": "Zambia",
  "ZW": "Zimbabwe"
}

# Dictionary containing command descriptions
command_descriptions = {
    "start": "Greeting",
    "help": "Show command list",
    "gender": "Determine the gender of a name.",
    "nationality": "Predict the nationality of a name.",
    "bored": "Bored is a command to find something to do by getting suggestions for random activities.",
    "dog": "This command will show you random dog images.",
    "cat": "Get random cat facts via text message.",
    "ip": "It allows you to get your current IP address.",
    "ipcheck": "Get information about a specified IP address, such as geological info, company, and carrier name.",
    "jokes": "Get random jokes.",
    "fakeuser": "Get information about a random fake user, including gender, name, email, address, etc.",
    "countrycode": "Show the list of country code and country name.",
    "universitylist": "Get a list of universities in a specified country.",
    "zipcode": "Get information about a specified ZIP/pin code. We have to provide country code and pin/zipcode for this. To check your coutry code click one /countrycode",
    "rolldice": "Roll a dice",
    "flipcoin": "Flip a coin.",
    "stopwatch": "To start and stop stopwatch.",
    "timer": "Users can start a timer using the timer command, provide a duration in seconds, and the bot will send a message when the timer is up.",
    "canceltimer": "Users can also cancel an ongoing timer using the /canceltimer command.",
}

# Create an inline keyboard for the start menu
start_keyboard = types.InlineKeyboardMarkup(row_width=1)
start_keyboard.add(types.InlineKeyboardButton("Show Commands", callback_data="show_commands"))


# Handle the /start command
@bot.message_handler(commands=['start', 'begin', 'demo'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    start_btn = types.KeyboardButton('/start')
    help_btn = types.KeyboardButton('/help')
    markup.add(start_btn, help_btn)
    bot.reply_to(message, "Welcome to the bot! Use the buttons below to explore:", reply_markup=markup)

# Handle the /help command
@bot.message_handler(commands=['help'])
def help(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    command_descriptions = {
        "gender": "Determine the gender of a name.",
        "nationality": "Predict the nationality of a name.",
        "bored": "Get suggestions for random activities.",
        "dog": "View random dog images.",
        "cat": "Receive random cat facts.",
        "ip": "Get your current IP address.",
        "ipcheck": "Get information about a specified IP address.",
        "jokes": "Get random jokes.",
        "fakeuser": "Generate information about a random fake user.",
        "countrycode": "Show the list of country codes and names.",
        "universitylist": "Get a list of universities in a specified country.",
        "zipcode": "Get information about a specified ZIP code.",
        "rolldice": "Roll a dice.",
        "flipcoin": "Flip a coin.",
        "stopwatch": "Start and stop stopwatch.",
        "timer": "Start a timer.",
        "canceltimer": "Cancel an ongoing timer."
    }
    
    for command, description in command_descriptions.items():
        markup.add(types.InlineKeyboardButton(description, callback_data=f"{command}"))
    
    markup.add(types.InlineKeyboardButton("Show Commands", callback_data="show_commands"))
    
    bot.reply_to(message, "Here are the available commands:", reply_markup=markup)

# ... (rest of your code)


# Handle inline keyboard button callbacks
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    command = call.data
    
    if command == "show_commands":
        # Create an inline keyboard for command buttons
        command_keyboard = types.InlineKeyboardMarkup(row_width=2)
        
        # Add buttons for each command with descriptions
        for cmd, description in command_descriptions.items():
            button = types.InlineKeyboardButton(f"/{cmd}", callback_data=f"command_{cmd}")
            command_keyboard.add(button)
        
        bot.edit_message_text("Here are the available commands:", call.message.chat.id, call.message.message_id, reply_markup=command_keyboard)
    
    elif command.startswith("command_"):
        cmd = command.split("command_")[-1]
        description = command_descriptions.get(cmd, "No description available.")
        bot.edit_message_text(f"**/{cmd} Command:**\n\n{description}", call.message.chat.id, call.message.message_id)

    else:
        if command == "gender":
            gender(call.message)
        elif command == "nationality":
            nationality(call.message)
        elif command == "bored":
            bored(call.message)
        elif command == "dog":
            dog(call.message)
        elif command == "cat":
            cat(call.message)  
        elif command == "ip":
            ip(call.message)  
        elif command == "ipcheck":
            ipcheck(call.message) 
        elif command == "jokes":
            jokes(call.message)  
        elif command == "fakeuser":
            fakeuser(call.message)
        elif command == "countrycode":
            countrycode(call.message)
        elif command == "universitylist":
            universitylist(call.message)
        elif command == "zipcode":
            zipcode(call.message)
        elif command == "rolldice":
            rolldice(call.message)
        elif command == "flipcoin":
            flipcoin(call.message)
        elif command == "stopwatch":
            stopwatch(call.message)
        elif command == "timer":
            timer(call.message)
        elif command == "canceltimer":
            canceltimer(call.message)
        else:
            bot.reply_to(call.message, "Unknown command or button.")


# @bot.message_handler(commands=['help'])
# def help(message):
#     help_text = """Commands:
# /start - Greeting
# /help - Show command list
# /gender - Determine the gender of a name. Please provide a name after the command, like: /gender John
# /nationality - Predict the nationality of a name. Please provide a name after the command, like: /nationality John
# /bored - Bored is a command to find something to do by getting suggestions for random activities.
# /dog - This command will show you random dog images.
# /cat - Get random cat facts via text message.
# /ip - It allows you to get your current IP address.
# /ipcheck - Get information about a specified IP address, such as geological info, company, and carrier name.. Please provide IP after the command, like: /ipcheck 146.125.65.147
# /jokes - Get random jokes.
# /fakeuser - Get information about a random fake user, including gender, name, email, address, etc.
# /countrycode - Show the list of country code and country name.
# /universitylist - Get a list of universities in a specified country. Please provide a country after the command, like: /universitylist india
# /zipcode - Get information about a specified ZIP code. For example if we are living in us and zip code is 90210, we can use command /zipcode US 90210.
#            Here we have to use country code for country. To know your country code click /countrycode.
#            Other example, if you are living in india and your postal code is 110006, then we can use command /zipcode IN 110006.
# /rolldice - To roll a dice
# /flipcoin - To flip a coin.  
# /timer - Users can start a timer using the timer command, provide a duration in seconds, and the bot will send a message when the timer is up.      
# /canceltimer - Users can also cancel an ongoing timer using the /canceltimer command.   
# """
#     bot.reply_to(message, help_text)

@bot.message_handler(commands=['gender'])
def gender(message):
    # Send a message to get the user's input
    bot.reply_to(message, "Please provide a name to determine its likely gender:")
    
    # Define a state to keep track of the conversation state
    bot.register_next_step_handler(message, process_gender_input)

def process_gender_input(message):
    name = message.text.strip()
    
    response = requests.get(f"https://api.genderize.io?name={name}")

    if response.status_code == 200:
        data = response.json()
        if data.get("gender"):
            bot.reply_to(message, f"The name '{name}' is most likely {data['gender']} with a probability of {data['probability']}")
        else:
            bot.reply_to(message, f"Cannot determine the gender for the name '{name}'")
    else:
        bot.reply_to(message, "Failed to fetch name data.")
        
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['nationality'])
def nationality(message):
    # Send a message to get the user's input
    bot.reply_to(message, "Please provide a name to determine its nationality:")
    
    # Define a state to keep track of the conversation state
    bot.register_next_step_handler(message, process_nationality_input)

def process_nationality_input(message):
    name = message.text.strip()
    
    response = requests.get(f"https://api.nationalize.io/?name={name}")
    
    if response.status_code == 200:
        data = response.json()
        if data.get("country"):
            top_country = data['country'][0]
            country_id = top_country['country_id']
            probability = top_country['probability']
            
            bot.reply_to(message, f"The name '{name}' is most likely from {country_code_to_name[country_id]} with a probability of {probability}")
        else:
            bot.reply_to(message, f"Cannot determine the nationality for the name '{name}'")
    else:
        bot.reply_to(message, "Failed to fetch nationality.")
        
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['bored'])
def bored(message):
    response = requests.get(f"https://www.boredapi.com/api/activity")
    data = response.json()
    if response.status_code == 200:
        bot.reply_to(message, f"You can do '{data['activity']}' activity, it is '{data['type']}' type activity. This activity will require '{data['participants']}' participants.")
    else:
        bot.reply_to(message, "Failed to load actitivies.")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['dog'])
def dog(message):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        data = response.json()
        url = data["message"]
        image_content = url
        bot.send_photo(message.chat.id, photo=image_content)
    else:
        bot.reply_to(message, "Failed to dog image.")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['cat'])
def cat(message):
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        data = response.json()
        fact = data["fact"]
        bot.reply_to(message, fact)
    else:
        bot.reply_to(message, f"Unable to fatch cat fact")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['ip'])
def ip(message):
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        data = response.json()
        ip = data["ip"]
        bot.reply_to(message, f"Your ip address is: "+ip)
    else:
        bot.reply_to(message, f"Unable to fatch IP address")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['ipcheck'])
def ipcheck(message):
    # Send a message to get the user's input
    bot.reply_to(message, "Please provide an IP address to check:")

    # Define a state to keep track of the conversation state
    bot.register_next_step_handler(message, process_ipcheck_input)

def process_ipcheck_input(message):
    ip = message.text.strip()
    
    # Check if the message is from the bot itself
    if message.from_user.id == bot.get_me().id:
        return
    
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    if response.status_code == 200:
        data = response.json()
        
        # Collect key-value pairs in a list excluding the last one
        info_list = [f"{x} = {y}" for index, (x, y) in enumerate(data.items()) if index != len(data) - 1]
        
        # Join the list items into a single reply
        reply_text = "\n".join(info_list)
        bot.reply_to(message, reply_text)
    else:
        bot.reply_to(message, "Unable to fetch IP address information.")

    time.sleep(25)
    help(message)

@bot.message_handler(commands=['jokes'])
def jokes(message):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
        type1 = data["type"]
        setup = data['setup']
        punchline = data['punchline']
        bot.reply_to(message, f"This is a {type1} joke.\n{setup} \n   {punchline} 😂😂")
    else:
        bot.reply_to(message, "Failed to dog image.")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['fakeuser'])
def fakeuser(message):
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()
        results = data["results"][0]

        gender = results["gender"]
        title = results["name"]["title"]
        first_name = results["name"]["first"]
        last_name = results["name"]["last"]
        street = results["location"]["street"]["name"]
        street_number = results["location"]["street"]["number"]
        city = results["location"]["city"]
        state = results["location"]["state"]
        country = results["location"]["country"]
        postcode = results["location"]["postcode"]
        email = results["email"]
        username = results["login"]["username"]
        dob = results["dob"]["date"].split("T")[0]
        registered_date = results["registered"]["date"].split("T")[0]
        phone = results["phone"]
        cell = results["cell"]
        picture = results["picture"]["large"]

        formatted_data = (
            f"Gender: {gender}\n"
            f"Name: {title} {first_name} {last_name}\n"
            f"Location: {street_number} {street}, {city}, {state}, {country}, {postcode}\n"
            f"Email: {email}\n"
            f"Username: {username}\n"
            f"Date of Birth: {dob}\n"
            f"Registered Date: {registered_date}\n"
            f"Phone: {phone}\n"
            f"Cell: {cell}\n"
        )

        bot.send_photo(message.chat.id, photo=picture, caption=formatted_data)
    else:
        bot.reply_to(message, "Failed to fetch fake user data.")
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['universitylist'])
def universitylist(message):
    # Send a message to get the user's input
    bot.reply_to(message, "Please provide a country for university list:")

    # Define a state to keep track of the conversation state
    bot.register_next_step_handler(message, process_country_input)

def process_country_input(message):
    country = message.text.strip()
    encoded_country = urllib.parse.quote(country)  # Encode the country parameter
    
    response = requests.get(f"http://universities.hipolabs.com/search?country={encoded_country}")
    if response.status_code == 200:
        data = response.json()
        
        if not data:
            bot.reply_to(message, f"No universities found for {country}.")
            return
        
        formatted_list = ""
        for university in data:
            name = university["name"]
            country = university["country"]
            state = university["state-province"]
            domains = ", ".join(university["domains"])
            web_pages = ", ".join(university["web_pages"])
            
            formatted_list += f"University: {name}\nCountry: {country}\nState: {state}\nDomains: {domains}\nWeb Pages: {web_pages}\n\n"
        
        file_name = f"{country}_universities.txt"
        with open(file_name, "w") as file:
            file.write(formatted_list)
        
        with open(file_name, "rb") as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(file_name)
    else:
        bot.reply_to(message, "Failed to fetch university list.")
        
    time.sleep(25)
    help(message)


@bot.message_handler(commands=['countrycode'])
def countrycode(message):
    country_codes_list = "\n".join([f"{code}: {name}" for code, name in country_code_to_name.items()])
    bot.reply_to(message, "Here are the country codes and names:\n" + country_codes_list)
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['zipcode'])
def zipcode(message):
    # Send a message to get the user's input
    bot.reply_to(message, "Please provide a country code and a postal code like: IN 110006")

    # Define a state to keep track of the conversation state
    bot.register_next_step_handler(message, process_zipcode_input)

def process_zipcode_input(message):
    args = message.text.strip().split()

    if len(args) != 2:
        bot.reply_to(message, "Please provide a country code and a postal code after the command, like: IN 110006")
        return
    
    country_code = args[0]
    postal_code = args[1]
    
    response = requests.get(f"https://api.zippopotam.us/{country_code}/{postal_code}")
    if response.status_code == 200:
        data = response.json()
        
        country = data["country"]
        places = data["places"]
        
        formatted_list = ""
        for place in places:
            place_name = place["place name"]
            state = place["state"]
            longitude = place["longitude"]
            latitude = place["latitude"]
            
            formatted_list += f"Place Name: {place_name}\nState: {state}\nLongitude: {longitude}\nLatitude: {latitude}\n\n"
        
        info = f"Postal Code: {postal_code}\nCountry: {country}\n\n{formatted_list}"
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, "Failed to fetch postal code information.")
        
    time.sleep(25)
    help(message)

@bot.message_handler(commands=['rolldice'])
def rolldice(message):
    try:
        roll_result = random.randint(1, 6)
        bot.reply_to(message, f"You rolled a {roll_result} on a 6-sided dice.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

    time.sleep(25)
    help(message)

@bot.message_handler(commands=['flipcoin'])
def flipcoin(message):
    try:
        coin_result = random.choice(["Heads", "Tails"])
        bot.reply_to(message, f"The coin landed on: {coin_result}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")
    time.sleep(25)
    help(message)

stopwatch_data = {}

@bot.message_handler(commands=['stopwatch'])
def stopwatch(message):
    chat_id = message.chat.id
    if chat_id not in stopwatch_data:
        stopwatch_data[chat_id] = {"running": True, "start_time": time.time()}
        bot.reply_to(message, "Stopwatch started. Use /stopwatch again to stop.")
    else:
        if stopwatch_data[chat_id]["running"]:
            elapsed_time = time.time() - stopwatch_data[chat_id]["start_time"]
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            bot.reply_to(message, f"Stopwatch stopped. Time: {formatted_time}")
        else:
            bot.reply_to(message, "Stopwatch is not running. Use /stopwatch again to start.")

        stopwatch_data[chat_id]["running"] = not stopwatch_data[chat_id]["running"]

    time.sleep(25)
    help(message)


timer_data = {}

def timer_callback(chat_id):
    bot.send_message(chat_id, "Timer is up!")

@bot.message_handler(commands=['timer'])
def timer(message):
    chat_id = message.chat.id

    if chat_id in timer_data and timer_data[chat_id]["running"]:
        bot.reply_to(message, "A timer is already running. Use /canceltimer to cancel it.")
        return

    bot.reply_to(message, "Enter the timer duration in seconds:")
    timer_data[chat_id] = {"running": True, "timer_thread": None}

@bot.message_handler(func=lambda message: message.text.isdigit() and int(message.text) > 0)
def timer_duration(message):
    chat_id = message.chat.id
    duration = int(message.text)

    if chat_id in timer_data and timer_data[chat_id]["running"]:
        if timer_data[chat_id]["timer_thread"]:
            timer_data[chat_id]["timer_thread"].cancel()

        timer_data[chat_id]["timer_thread"] = threading.Timer(duration, timer_callback, args=[chat_id])
        timer_data[chat_id]["timer_thread"].start()

        bot.reply_to(message, f"Timer set for {duration} seconds. Use /canceltimer to cancel it.")
    else:
        bot.reply_to(message, "Timer was not started. Use /timer to start a new timer.")

@bot.message_handler(commands=['canceltimer'])
def canceltimer(message):
    chat_id = message.chat.id

    if chat_id in timer_data and timer_data[chat_id]["running"] and timer_data[chat_id]["timer_thread"]:
        timer_data[chat_id]["timer_thread"].cancel()
        timer_data[chat_id]["timer_thread"] = None
        timer_data[chat_id]["running"] = False
        bot.reply_to(message, "Timer has been canceled.")
    else:
        bot.reply_to(message, "No active timer to cancel.")

    time.sleep(25)
    help(message)

# Run the bot
bot.polling()



