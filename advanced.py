from flask import Flask,render_template,request
app=Flask(__name__)
data={"login":True,"id":"hello"}
@app.route("/",methods=["POST","GET"])
def main():
    if request.method=="POST":
        title=request.form.get("title")
        blog=request.form.get("blog")
        if "," in title:
            title=title.split(",")
            title="|!|".join(title)
        if "," in blog:
            blog=blog.split(",")
            blog="|!|".join(blog)
        f=open("data.csv","a")
        f.write(f"\n{title},{blog},{data['id']}")
        f.close()
        return render_template("index.html",data=data)
    return render_template("index.html",data=data)
@app.route("/login")
def login():
    return render_template("login.html",data=data)
@app.route("/signup")
def signup():
    return render_template("signup.html",data=data)
@app.route("/account")
def account():
    return render_template("account.html",data=data)
app.run(debug=True)