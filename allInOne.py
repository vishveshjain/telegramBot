import telebot
import requests
import urllib.parse
import os

Token = "6691503234:AAFXchKpFJovhs56gu5gb_tv-ldqjkSY-kY"
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
@bot.message_handler(commands=['start','demo', 'begin'])
def start(message):
    bot.reply_to(message, "This bot provides lots of interesting services. Please hit /help to find all of our services")

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """Commands:
/start - Greeting
/help - Show command list
/gender - Determine the gender of a name. Please provide a name after the command, like: /gender John
/nationality - Predict the nationality of a name. Please provide a name after the command, like: /nationality John
/bored - Bored is a command to find something to do by getting suggestions for random activities.
/dog - This command will show you random dog images.
/cat - Get random cat facts via text message.
/ip - It allows you to get your current IP address.
/ipcheck - Get information about a specified IP address, such as geological info, company, and carrier name.. Please provide IP after the command, like: /ipcheck 146.125.65.147
/jokes - Get random jokes.
/fakeuser - Get information about a random fake user, including gender, name, email, address, etc.
/countrycode - Show the list of country code and country name.
/universitylist - Get a list of universities in a specified country. Please provide a country after the command, like: /universitylist india
/zipcode - Get information about a specified ZIP code. For example if we are living in us and zip code is 90210, we can use command /zipcode US 90210.
           Here we have to use country code for country. To know your country code click /countrycode.
           Other example, if you are living in india and your postal code is 110006, then we can use command /zipcode IN 110006.
"""
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['gender'])
def gender(message):
    # Get the user's input after the command
    name = message.text.split("/gender")[-1].strip()
    if not name:
        bot.reply_to(message, "Please provide a name after the command, like: /gender John")
        return

    response = requests.get(f"https://api.genderize.io?name={name}")

    if response.status_code == 200:
        data = response.json()
        if data.get("gender"):
            bot.reply_to(message, f"The name '{name}' is most likely {data['gender']} with a probability of {data['probability']}")
        else:
            bot.reply_to(message, f"Cannot determine the gender for the name '{name}'")
    else:
        bot.reply_to(message, "Failed to fetch name data.")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['nationality'])
def nationality(message):
    # Get the user's input after the command
    name = message.text.split("/nationality")[-1].strip()
    
    if not name:
        bot.reply_to(message, "Please provide a name after the command, like: /nationality John")
        return

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
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['bored'])
def bored(message):
    response = requests.get(f"https://www.boredapi.com/api/activity")
    data = response.json()
    if response.status_code == 200:
        bot.reply_to(message, f"You can do '{data['activity']}' activity, it is '{data['type']}' type activity. This activity will require '{data['participants']}' participants.")
    else:
        bot.reply_to(message, "Failed to load actitivies.")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['dog'])
def quotes(message):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        data = response.json()
        url = data["message"]
        image_content = url
        bot.send_photo(message.chat.id, photo=image_content)
    else:
        bot.reply_to(message, "Failed to dog image.")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['cat'])
def cat(message):
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        data = response.json()
        fact = data["fact"]
        bot.reply_to(message, fact)
    else:
        bot.reply_to(message, f"Unable to fatch cat fact")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['ip'])
def ip(message):
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        data = response.json()
        ip = data["ip"]
        bot.reply_to(message, f"Your ip address is: "+ip)
    else:
        bot.reply_to(message, f"Unable to fatch IP address")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['ipcheck'])
def ip_check(message):
    # Get the user's input after the command
    ip = message.text.split("/ipcheck")[-1].strip()
    
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
    bot.reply_to(message, "/help")

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
    bot.reply_to(message, "/help")

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
    bot.reply_to(message, "/help")

import urllib.parse

@bot.message_handler(commands=['universitylist'])
def universitylist(message):
    # Get the user's input after the command
    country = message.text.split("/universitylist")[-1].strip()
    encoded_country = urllib.parse.quote(country)  # Encode the country parameter
    
    response = requests.get(f"http://universities.hipolabs.com/search?country={encoded_country}")
    if response.status_code == 200:
        data = response.json()
        
        # Create a formatted list with all university details
        formatted_list = ""
        for university in data:
            name = university["name"]
            country = university["country"]
            state = university["state-province"]
            domains = ", ".join(university["domains"])
            web_pages = ", ".join(university["web_pages"])
            
            formatted_list += f"University: {name}\nCountry: {country}\nState: {state}\nDomains: {domains}\nWeb Pages: {web_pages}\n\n"
        
        # Write the formatted list to a text file
        file_name = f"{country}_universities.txt"
        with open(file_name, "w") as file:
            file.write(formatted_list)
        
        # Send the text file as a document to the user
        with open(file_name, "rb") as file:
            bot.send_document(message.chat.id, file)
        
        # Delete the text file after sending
        os.remove(file_name)
    else:
        bot.reply_to(message, "Failed to fetch university list.")
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['countrycode'])
def countrycode(message):
    country_codes_list = "\n".join([f"{code}: {name}" for code, name in country_code_to_name.items()])
    bot.reply_to(message, "Here are the country codes and names:\n" + country_codes_list)
    bot.reply_to(message, "/help")

@bot.message_handler(commands=['zipcode'])
def zipcode(message):
    # Get the user's input after the command
    args = message.text.split("/zipcode")[-1].strip().split()
    
    if len(args) != 2:
        bot.reply_to(message, "Please provide a country code and a postal code after the command, like: /zipcode IN 110006")
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
    bot.reply_to(message, "/help")

bot.polling()

