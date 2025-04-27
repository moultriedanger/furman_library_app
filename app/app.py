from flask import Flask, render_template
import oracledb

app = Flask(__name__)

# Oracle DB connection config
dsn = oracledb.makedsn('csdb.fu.campus', 1521, sid='cs40')
connection = oracledb.connect(user='agardner', password='Agar1324', dsn=dsn)

@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/artist_info')
def artist_info():
    return render_template('artist_info.html')

# Route for Artist Form Page
@app.route('/artist')
def artist_form():
    return render_template('artist_form.html')

# Collector Information Form Page
@app.route('/collector_form')
def collector_form():
    return render_template('collector_form.html')

# Collector Information Form Page
@app.route('/collector_info')
def collector_info():
    return render_template('collector_info.html')

# Artwork Information Form Page
@app.route('/artwork')
def artwork_form():
    return render_template('artwork_form.html')

# Sale Invoice Form Page
@app.route('/sale')
def sale_form():
    return render_template('sale_form.html')


if __name__ == '__main__':
    app.run(debug=True)
