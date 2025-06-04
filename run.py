from app import app

if __name__ == "__main__":
    print(app.config["PORT"])
    app.run(host=app.config["HOST"], debug=app.config["DEBUG"], port=app.config["PORT"])
