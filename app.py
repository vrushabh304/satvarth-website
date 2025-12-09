from flask import Flask, render_template, request, jsonify, url_for , redirect , session
from flask_mail import Mail
from config import Config          # Import settings
from email_utils import send_contact_email 
from datetime import datetime
from newsletter_utils import send_newsletter_email

# Import the email logic
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



@app.route('/case_studies')
def case_studies():
    return render_template('case_studies.html')

@app.route('/case_studies_detail')
def case_studies_detail():
    return render_template('case_studies_detail.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/team_detail')
def team_detail():
    return "Team detiled"


@app.route('/page_left_sidebar')
def page_left_sidebar():
    return render_template('page_left_sidebar.html')
##############################################################################################
# Blog pages start
@app.route('/blog')
def blog():
    return render_template('blog/blog.html')

@app.route('/blog_detail_marketing_1')
def blog_detail_marketing_1():
    return render_template('blog/blog_detail_marketing_1.html')

@app.route('/blog_detail_operations')
def blog_detail_operations():
    return render_template('blog/blog_detail_operations.html')

@app.route('/blog_detail_marketing_2')
def blog_detail_marketing_2():
    return render_template('blog/blog_detail_marketing_2.html')

@app.route('/blog_detail_creative')
def blog_detail_creative():
    return render_template('blog/blog_detail_creative.html')

@app.route('/blog_detail_business')
def blog_detail_business():
    return render_template('blog/blog_detail_business.html')

@app.route('/blog_detail_development')
def blog_detail_development():
    return render_template('blog/blog_detail_development.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')

# @app.route('/blog_detail_marketing')
# def blog_detail_marketing():
#     return render_template('blog/blog_detail_marketing.html')


#################################################################################################

@app.route('/page_right_sidebar')
def page_right_sidebar():
    return render_template('page_right_sidebar.html')

@app.route('/service_detail')
def service_detail():
    return render_template('service_detail.html')

#team member start
@app.route('/anne_smith')#1
def anne_smith():
    return render_template('team/anne_smith.html')

@app.route('/john_doe')#2
def john_doe():
    return render_template('team/john_doe.html')

@app.route('/mellissa_doe')#3
def mellissa_doe():
    return render_template('team/mellissa_doe.html')

@app.route('/paul_flavius')#4
def paul_flavius():
    return render_template('team/paul_flavius.html')

@app.route('/michael_davis')#5
def michael_davis():
    return render_template('team/michael_davis.html')

@app.route('/samantha_brown')#6
def samantha_brown():
    return render_template('team/samantha_brown.html')

@app.route('/kevin_lee')#7
def kevin_lee():
    return render_template('team/kevin_lee.html')

@app.route('/ashley_williams')#8
def ashley_williams():
    return render_template('team/ashley_williams.html')

#team member finsh
#aboutus in owner
@app.route('/o_james_smith')#8
def o_james_smith():
    return render_template('about/o_james_smith.html')

@app.route('/o_devid_johnson')#8
def o_devid_johnson():
    return render_template('about/o_devid_johnson.html')

@app.route('/o_mellissa_doe')#8
def o_mellissa_doe():
    return render_template('about/o_mellissa_doe.html')

@app.route('/o_paul_flavius')#8
def o_paul_flavius():
    return render_template('about/o_paul_flavius.html')

#Finish

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/typography')
def typography():
    return render_template('typography.html')

@app.route('/our_vision')
def our_vision():
    return render_template('our_vision.html')

@app.route('/our_mission')
def our_mission():
    return render_template('our_mission.html')


@app.route('/custom_web_app ')
def custom_web_app():
    return render_template('service/custom_web_app.html')

@app.route('/mobile_app_development')
def mobile_app_development():
    return render_template('service/mobile_app_development.html')

@app.route('/ui_ux_design')
def ui_ux_design():
    return render_template('service/ui_ux_design.html')

@app.route('/three_d_web_experiences')
def three_d_web_experiences():
    return render_template('service/three_d_web_experiences.html')

@app.route('/ecommerce_solutions')
def ecommerce_solutions():
    return render_template('service/ecommerce_solutions.html')

@app.route('/api_development_integration')
def api_development_integration():
    return render_template('service/api_development_integration.html')

@app.route('/custom_cms_erp_systems')
def custom_cms_erp_systems():
    return render_template('service/custom_cms_erp_systems.html')

@app.route('/maintenance_support')
def maintenance_support():
    return render_template('service/maintenance_support.html')

# @app.route('/custom_cms_erp_systems')
# def custom_cms_erp_systems():
#     return render_template('service/custom_cms_erp_systems.html')

@app.route('/form')
def form():
    return render_template('form.html')

# Coming-Soon page start and timer on ------------------------------------------------------------------------------------------------------


@app.route("/coming_soon")
def coming_soon():
    # 1) If you want countdown: set a real launch date
    # Example: 31 Dec 2025, 10:00 AM
    launch_date = datetime(2026, 1, 11, 10, 0, 0)# year , month , day , hours , min , sec

    # 2) If you DON'T want countdown, only message:
    # launch_date = None
    return render_template("coming_soon.html", launch_date=launch_date)


#-----------------------------------------------------------------------------------------------------------------------------------------------
#footer email working

@app.route("/newsletter", methods=["POST"])
def newsletter():
    user_email = request.form.get("email")

    if not user_email:
        return "Invalid email", 400

    # Send emails (admin + user)
    send_newsletter_email(
        mail=mail,
        admin_email=Config.RECIPIENT_EMAIL,
        user_email=user_email
    )

    # Redirect to thank-you page
    return redirect(url_for("newsletter_thankyou"))

@app.route("/newsletter-thankyou")
def newsletter_thankyou():
    return render_template("newsletter_thankyou.html")


# @app.route('/ ')
# def ():
#     return render_template('  .html')

# @app.route('/ ')
# def ():
#     return render_template('  .html')

# @app.route('/ ')
# def ():
#     return render_template('  .html')

# @app.route('/ ')
# def ():
#     return render_template('  .html')

# @app.route('/ ')
# def ():
#     return render_template('  .html')

# @app.route('/ ')
# def ():
#     return render_template('  .html')


# @app.route('/ ')
# def ():
#     return render_template('  .html')

if __name__ == '__main__':
    app.run(debug=True) 