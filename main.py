import secrets
import json
from datetime import date

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["secret_key"] = secrets.token_urlsafe(16)


class new:
  def newfile(self):
    with open(f"data/{date.today()}.csv", "x") as file:
      file.close()
    with open(f"data/{date.today()}.csv", "a") as file:
      file.write("name, osis, organizationn, email, date\n")
      file.close()
    return

  def date(self):
    return date.today()

alex = new()




@app.route("/")
def home():
  info_str = request.args.get('info')
  infostr = json.loads(info_str) if info_str else None
  if info_str:
    return render_template("index.html", success=True, info=infostr)
  return render_template("index.html")


#The logging method (function)
@app.route("/log", methods=["GET", "POST"])
def log():
  if request.method == "POST":
    info = {
      "name":request.form.get("name", "N/A"),
      "osis":request.form.get("osis", "Non-DOE"),
      "organization":request.form.get("school", "N/A"),
      "email":request.form.get("email", "N/A")
      }
    print(info["organization"])
    for key,value in info.items():
      if value == "N/A":
        return render_template("index.html", error=f"{key} is not filled.")


    with open(f'data/{date.today()}.csv', 'a') as file:
      file.write(f"{info['name']}, {info['osis']}, {info['organization']}, {info['email']}, {date.today()}\n")
      file.close()
    info_str = json.dumps(info)
    return redirect(url_for("home", info=info_str))

  return "Internet protocal error. Please try again later."



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
