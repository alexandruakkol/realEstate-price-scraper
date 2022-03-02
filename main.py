from scraper import scrape
from flask import Flask

app = Flask(__name__)
all_data = scrape()

apartmentRent = {'apartmentRent': all_data['apartmentRent']}
apartmentSale = {'apartmentSale': all_data['apartmentSale']}
studioRent = {'studioRent': all_data['studioRent']}
studioSale = {'studioSale': all_data['studioSale']}

@app.route('/')
def homepage():
    return 'try /apartments-for-rent, /apartments-for-sale, /studios-for-rent, or /studios-for-sale'

@app.route('/apartments-for-rent')
def apartmentRentPage():
    return apartmentRent

@app.route('/apartments-for-sale')
def apartmentSalePage():
    return apartmentSale

@app.route('/studios-for-rent')
def studioRentPage():
    return studioRent

@app.route('/studios-for-sale')
def studioSalePage():
    return studioSale

if __name__=='__main__':
    app.run()

