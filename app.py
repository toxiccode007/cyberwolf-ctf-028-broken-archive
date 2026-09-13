from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    return send_from_directory(
        os.path.join(app.root_path, "challenge_files"),
        "recovered_archive.zip",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
