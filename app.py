from flask import Flask, render_template, request
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


if __name__ == "__main__":
        app.run()