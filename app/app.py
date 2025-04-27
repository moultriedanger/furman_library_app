from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing.html')

#Artist Information Form Page
@app.route('/artist')
def artist_form():
    return render_template('artist_info.html')

# Collector Information Form Page
@app.route('/collector')
def collector_form():
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
