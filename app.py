from flask import Flask, request, url_for, render_template, redirect
from recommender import get_recommendation

app = Flask(__name__)


@app.route("/recommender", methods=["GET", "POST"])
def index():
    if request.method == "POST" and request.form["hhkey"]:
        hhkey = int(request.form["hhkey"])
        try:
            recommended_products = get_recommendation(hhkey)
            return render_template(
                "layout.html", recommended_products=recommended_products
            )
        except Exception:
            return render_template("layout.html", error_message=True)
    else:
        return render_template("layout.html")


if __name__ == "__main__":
    app.run(debug=True)
