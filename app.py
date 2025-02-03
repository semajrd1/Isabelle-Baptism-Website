from flask import Flask, request, render_template, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure session settings
app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Configure session settings
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://user:password@localhost/invitees'
app.config['SECRET_KEY'] = 'the random string' 

# Initialize the database
db = SQLAlchemy(app) 

# Define the Invitees model
class Invitees(db.Model):
    __tablename__='invitees'
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each invitee
    keyx = db.Column(db.String(200), nullable=False)  # Unique key for authentication
    name = db.Column(db.String(200), nullable=False)  # Name of the invitee
    lang = db.Column(db.String(200))  # Language preference
    regi = db.Column(db.String(200))  # Registration status ('yes' or 'no')
    email = db.Column(db.String(200))  # Email address
    
    total_given = db.Column(db.Integer)  # Total number of people allowed
    name_extra_people = db.Column(db.String(200))  # Names of extra guests
    total_selected = db.Column(db.Integer)  # Number of people actually attending
    food = db.Column(db.Integer)  # Number of vegetarian meals requested

    # Constructor to initialize invitee details
    def __init__(self, keyx, name, lang, regi, email, total_given, name_extra_people, total_selected, food):
        self.keyx = keyx
        self.name = name
        self.lang = lang
        self.regi = regi
        self.email = email
        self.total_given = total_given
        self.name_extra_people = name_extra_people
        self.total_selected = total_selected
        self.food = food

# Route for the home page
@app.route("/")
def index():
    plus = {}
    invitee = access_check()  # Verify invitee access
    
    if invitee.name == None:
        return render_template("poem.html")  # Redirect to poem page if no invitee
    else:
        named_extra = invitee.name_extra_people
        if named_extra == None:
            if invitee.total_given == 1:
                plus["name"] = ""
            else:
                plus["name"] = "(+"+str(invitee.total_given-1)+")"
        else:
            plus["name"] = "and {name}".format(name = invitee.name_extra_people)
        return render_template("index.html", name=invitee.name, plus=plus)

# Route for the information page
@app.route("/info")
def info():
    invitee = access_check()
    if invitee.name == None:
        return render_template("poem.html")
    else:
        return render_template("info.html")

# Route for registration
@app.route("/register", methods=["GET", "POST"])
def register():
    invitee = access_check()
    if invitee.name == None:
        return render_template("poem.html")
    else:
        group_name = str(invitee.name)+"'s Group"
        email = str(invitee.email)
        
        if invitee.regi == "no":
            regi_message = "We're sorry to hear that you're not coming!"
        if invitee.regi == "yes":
            regi_message = "Thanks for letting us know you're coming!"

        # If no registration status, show form
        if invitee.regi == None:
            if request.method == "POST":
                if not request.form.get("going_or_not"):
                    return "Must declare whether you're going!"
                else:
                    if request.form.get("going_or_not") == 'going':
                        invitee.regi = 'yes'
                        invitee.total_selected = request.form.get("number_of_people")
                        invitee.food = request.form.get("number_of_veggies")
                        invitee.email = request.form.get("email")
                        try:
                            db.session.commit()
                            regi_message = "Thanks for letting us know you're coming!"
                            return render_template("already_registered.html", regi_message=regi_message)
                        except:
                            return 'Try again!'
                    else:
                        invitee.regi = 'no'
                        invitee.total_selected = '0'
                        invitee.food = '0'
                        invitee.email = request.form.get("email")
                        try:
                            db.session.commit()
                            regi_message = "We're sorry to hear that you're not coming!"
                            return render_template("already_registered.html", regi_message=regi_message)
                        except:
                            return 'Try again!'
            else:
                return render_template("register.html", group_name=group_name, number_of_people_alloc=invitee.total_given)
        else:
            return render_template("already_registered.html", regi_message=regi_message)

# Route for deregistration
@app.route("/deregister", methods=["POST"])
def deregister():
    invitee = access_check()
    if invitee.name == None:
        return render_template("poem.html")
    else:
        invitee.regi = None  # Reset registration status
        invitee.total_selected = '0'
        invitee.food = '0'
        db.session.commit()
        return redirect("/register")

# Function to check invitee access
def access_check():
    class Object(object):
        pass

    invitee = Object()
    invitee.name = None
    invitee.total_given = None
    
    if "keyx" in request.args:
        session["keyx"] = request.args.get("keyx", "")
        keyx1 = session["keyx"]
        invitee = db.session.query(Invitees).filter(Invitees.keyx == keyx1).first()
        print(invitee)
    elif session.get("keyx") is not None:
        keyx1 = session["keyx"]
        invitee = db.session.query(Invitees).filter(Invitees.keyx == keyx1).first()
        print(invitee)
    
    return invitee
