from flask import Flask, render_template, request, Response, send_from_directory
import qrcode
import base64
import io

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None

    if request.method == "POST":
        data = request.form["data"]

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")

        qr_image = base64.b64encode(
            buffer.getvalue()
        ).decode("utf-8")

    return render_template("index.html", qr_image=qr_image)


@app.route("/robots.txt")
def robots():
    return Response(
        """User-agent: *
Allow: /
Sitemap: https://qr-code-generator-vu7q.onrender.com/sitemap.xml
""",
        mimetype="text/plain"
    )

@app.route("/sitemap.xml")
def sitemap():
    return Response(
        """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://qr-code-generator-vu7q.onrender.com/</loc>
    </url>
</urlset>
""",
        mimetype="application/xml"
    )

@app.route("/google92f273bbe2a325e0.html")
def google_verification():
    return send_from_directory(".", "google92f273bbe2a325e0.html")

if __name__ == "__main__":
        app.run()
