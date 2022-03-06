from scraper import scrape
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
all_data = scrape()

apartmentRent = {'data': all_data['apartmentRent']}
apartmentSale = {'data': all_data['apartmentSale']}
studioRent = {'data': all_data['studioRent']}
studioSale = {'data': all_data['studioSale']}

@app.route('/')
@cross_origin()
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
@cross_origin()
def apartmentRentPage():
    return apartmentRent

@app.route('/apartments-for-sale')
@cross_origin()
def apartmentSalePage():
    return apartmentSale

@app.route('/studios-for-rent')
@cross_origin()
def studioRentPage():
    return studioRent

@app.route('/studios-for-sale')
@cross_origin()
def studioSalePage():
    return studioSale

if __name__=='__main__':
    app.run()

