from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

db = [
    {"id": 1, "name": "photo1"},
    {"id": 2, "name": "photo2"},
    {"id": 3, "name": "photo3"},
]

@app.route("/")
def index():
    return render_template("index.html", photos=db)

@app.route("/photos", methods=["GET", "POST"])
def photos():
    if request.method == "POST":
        # 假设这是保存照片的逻辑
        new_id = len(db) + 1
        new_name = request.form.get('name', 'default_name')
        db.append({"id": new_id, "name": new_name})
        return redirect(url_for('photos'))
    return render_template("photos.html", photos=db)

@app.route("/photos/new", methods=["GET"])
def new_photos():
    return render_template("new_photo.html")

@app.route("/photos/<int:id>", methods=["GET", "PUT", "DELETE"])
def show_photo(id):
    photo = next((photo for photo in db if photo['id'] == id), None)
    if not photo:
        return "Photo not found", 404
    if request.method == "GET":
        return render_template("photo_details.html", photo=photo)
    elif request.method == "PUT":
        # 更新照片逻辑
        return "Photo updated", 200
    elif request.method == "DELETE":
        # 删除照片逻辑
        return "Photo deleted", 200

@app.route("/photos/<int:id>/edit", methods=["GET"])
def edit_photo(id):
    photo = next((photo for photo in db if photo['id'] == id), None)
    if not photo:
        return "Photo not found", 404
    return render_template("edit_photo.html", photo=photo)

if __name__ == "__main__":
    app.run(debug=True)
