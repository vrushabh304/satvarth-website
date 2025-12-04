from flask import Flask, render_template, request, jsonify, url_for
from flask_mail import Mail
from config import Config          # Import settings
from email_utils import send_contact_email  # Import the email logic
app = Flask(__name__)


# Load configuration from config.py
app.config.from_object(Config)

# Initialize Mail
mail = Mail(app)
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/sidepanel')
def sidepanel():
    return render_template('sidepanel.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

#Dropdown menu 
@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')

@app.route('/manufacturing')
def manufacturing():
    return render_template('manufacturing.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/real_estate')
def real_estate():
    return render_template('real_estate.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/logistics')
def logistics():
    return render_template('logistics.html')

@app.route('/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # 1. Get data from the form
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'subject': request.form.get('subject'),
            'message': request.form.get('message')
        }

        # 2. Basic Validation
        if not form_data['name'] or len(form_data['name']) < 2:
            return jsonify({'success': False, 'message': 'Name is required (min 2 chars).'})
        if not form_data['email'] or '@' not in form_data['email']:
            return jsonify({'success': False, 'message': 'Valid email is required.'})
        if not form_data['message'] or len(form_data['message']) < 10:
            return jsonify({'success': False, 'message': 'Message must be at least 10 chars.'})

        # 3. Call the external email function
        # We pass the 'mail' object and the recipient from Config
        result = send_contact_email(mail, app.config['RECIPIENT_EMAIL'], form_data)
        
        return jsonify(result)

    # Render the HTML page for GET requests
    return render_template('contact.html')


 ###################################33

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/error_404')
def error_404():
    return render_template('error_404.html')

@app.route('/coming_soon')
def coming_soon():
    return render_template('coming_soon.html')

@app.route('/case_studies')
def case_studies():
    return render_template('case_studies.html')

@app.route('/case_studies_detail')
def case_studies_detail():
    return render_template('case_studies_detail.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/index_02')
def index_02():
    return render_template('index_02.html')


@app.route('/team_detail')
def team_detail():
    return "Team detiled"

@app.route('/index_03')
def index_03():
    return render_template('index_03.html')

@app.route('/page_left_sidebar')
def page_left_sidebar():
    return render_template('page_left_sidebar.html')

@app.route('/blog_detail')
def blog_detail():
    return "Blog detiled"

@app.route('/page_right_sidebar')
def page_right_sidebar():
    return render_template('page_right_sidebar.html')

@app.route('/service_detail')
def service_detail():
    return render_template('service_detail.html')

@app.route('/team_single')
def team_single():
    return render_template('team_single.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/typography')
def typography():
    return render_template('typography.html')

# @app.route('/case_studies_detail')
# def case_studies_detail():
#     return render_template('case_studies_detail.html')

# @app.route('/case_studies_detail')
# def case_studies_detail():
#     return render_template('case_studies_detail.html')

if __name__ == '__main__':
    app.run(debug=True) 