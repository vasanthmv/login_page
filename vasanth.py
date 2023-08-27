from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def login():
    check=""
    if request.method=="POST":
        if request.form["email-address"]=="vasanth@gmail.com" and request.form["passcode"]=="asdf123":
            print("login success")
            return render_template("home.html") 
        else:
            print("Bad credentials")
            check="err"      
    return render_template("vasanthm.html",msg=check)

if __name__=="__main__":
    
    
    app.run(debug=True)

