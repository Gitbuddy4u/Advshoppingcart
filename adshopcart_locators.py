import datetime
from faker import Faker
fake = Faker(locale='en_CA')

# ----------------- Moodle Web App DATA PARAMETERS ----------------------
app = 'advantageonlineshopping'
adv_shop_cart_url = 'https://advantageonlineshopping.com/#/'
adv_shop_cart_home_page_title = '\xa0Advantage Shopping'

username = fake.user_name()[0:14]
email = fake.email()
password = fake.password()
# confirm_password = fake.confirm_password()
phone_number = fake.phone_number()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'

country = fake.current_country()
city = fake.city()
address = fake.address().replace("\n"," ")[0: 50]
province = fake.province()[0: 10]
postal_code = fake.postalcode()

subject = f'--Todays date is:-  {datetime.datetime.now()}. '









