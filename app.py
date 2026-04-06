from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

# Demo amacli bellek ici yorum listeleri
# Vulnerable page: yorumlar dogrudan gosterilir
# Safe page: yorumlar escape edilerek gosterilir
vulnerable_comments = []
safe_comments = []


@app.route("/")
def home():
    # Ana giris sayfasi
    return render_template("index.html")


@app.route("/vulnerable", methods=["GET", "POST"])
def vulnerable():
    # Guvensiz ornek:
    # kullanici girdisi oldugu gibi saklanir ve render edilir
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        comment = request.form.get("comment", "").strip()

        # Bos veri eklenmesini engelle
        if username and comment:
            vulnerable_comments.append({
                "username": username,
                "comment": comment
            })

        return redirect(url_for("vulnerable"))

    return render_template("vulnerable.html", comments=vulnerable_comments)


@app.route("/safe", methods=["GET", "POST"])
def safe():
    # Guvenli ornek:
    # kullanici girdisi escape() ile zararsiz hale getirilir
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        comment = request.form.get("comment", "").strip()

        # Bos veri eklenmesini engelle
        if username and comment:
            safe_comments.append({
                "username": escape(username),
                "comment": escape(comment)
            })

        return redirect(url_for("safe"))

    return render_template("safe.html", comments=safe_comments)


@app.route("/reset")
def reset():
    # Demo verilerini temizle
    vulnerable_comments.clear()
    safe_comments.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    # Flask gelistirme sunucusunu baslat
    app.run(debug=True)
