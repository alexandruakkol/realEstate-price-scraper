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
    return ("""
    <style>
    *{text-align:center;
    list-style:none;}
    h1{
    font-size:calc(12px + 3vw);
    }
    ul{
    font-size:calc(12px + 2vw);}
    </style>
    
    <h1>Bucharest real estate prices API</h1>
    <ul>
        <li><a href="/apartments-for-rent">Apartments for rent API</a></li>
        <li><a href="/apartments-for-sale">Apartments for sale API</a></li>
        <li><a href="/studios-for-rent">Studios for rent API</a></li>
        <li><a href="/studios-for-sale">Studios for sale API</a></li>
    </ul>
    <p style="display:block;height:70vh;">Data format: €/m²</p>
    <footer>
    Data from compariimobiliare.ro
    </footer>
    """)
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

