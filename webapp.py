import random
import datetime
from flask import Flask, request, redirect, render_template, send_file
app = Flask(__name__)

# creating a dummy database of users for demonstration purposes
users = {
    "user1": "password1",
    "user2": "password2"
}

# routes for handling the login and logout pages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username] == password:
        return redirect("/welcome")
    return render_template("index.html", message="Invalid username or password")


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# create a list of breakfast items
breakfast = ["Eggs", "Croissants", "Saussage", "Bagel", "Toast", "Oatmeal"]

# create a list of days of the week
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

# create a list of fruits
fruits = ["Apple", "Banana", "Orange", "Grape",
          "Strawberry", "Blueberry", "Raspberry"]

# create a list of beverages
beverages = ["Coffee", "Tea", "Milk", "Water", "Juice"]


"""def choose_random_item_without_repeating(array1):
    # create a copy of the array so the original is not modified
    items = array1[:]
    #items2 = array2[:]
    # create an empty list to store the chosen items
    chosen_items = []
    while items:
        # get a random index from the array
        index = random.randint(0, len(items) - 1)
        ##index2 = random.randint(0,len(items2) - 1)
        # add the item at the randomly chosen index to the list of chosen items
        chosen_items.append(items[index])
        # remove the item from the list of available items
        items.pop(index)
    return chosen_items """


# If the user goes to the root path, return a string with 1 breakfast item,  1 day of the week, and 1 fruit, and 1 beverage
# If the user goes to the /dontrepeat path, return a string with 2 breakfast items
# If the user goes to the /tired path, return a string with 1 breakfast item and 1 beverage
# If the user goes to the /<dayoftheweek> path, return a string that says "You can eat anything you want today!" if it's Saturday, "Let's nourish up with some fruits before the start of the week" if it's Sunday, and "It's oatmeal today!"

# create a route for the root path

@app.route("/breakfast")
# create a function that returns a string with 1 breakfast item,  1 day of the week, and 1 fruit, and 1 beverage
def breakfastfun():
    return " It's " + datetime.datetime.now().date().strftime("%A") + ". Your breakfast is " + breakfast[random.randint(0, len(breakfast) - 1)] + " with an " + fruits[0] + " and " + beverages[1] + "."

# create a route for the /dontrepeat path


@app.route("/breakfast/dontrepeat")
# create a function that returns a string with 2 breakfast items
def norepeat():
    return "Ok here is something new for you. Your breakfast is " + breakfast[2] + " and " + breakfast[3] + "."

# create a route for the /tired path


@app.route("/breakfast/tired")
# create a function that returns a string with 1 breakfast item and 1 beverage
def caffein():
    return "Your breakfast is " + breakfast[4] + " and " + beverages[1] + " because you're tired"

# create a route for the /<dayoftheweek> path


@app.route("/breakfast/<day>")
# create a function that returns a string that says "You can eat anything you want today!" if it's Saturday, "Let's nourish up with some fruits before the start of the week" if it's Sunday, and "It's oatmeal today!"
def weekend(day):
    # loop through the days of the week and print out the day of the week and the breakfast item for that day of the week
    if day == "Monday":
        return "On " + days[0] + ". Your breakfast will be " + breakfast[0] + " and " + fruits[0]
    if day == "Tuesday":
        return "On " + days[1] + ". Your breakfast is " + breakfast[1] + " and" + fruits[1]
    if day == "Wednesday":
        return "On " + days[2] + ". Your breakfast is " + breakfast[2] + " and " + fruits[2]
    if day == "Thursday":
        return "On " + days[3] + ". Your breakfast is " + breakfast[3] + " and " + fruits[3]
    if day == "Friday":
        return "On " + days[4] + ". Your breakfast is " + breakfast[4] + " and " + fruits[4]
    if day == "Saturday":
        return "On " + days[5] + ". Your breakfast is " + breakfast[5] + " and " + fruits[5]
    else:
        return "It's oatmeal today! You didn't specify what you want so I'm giving you oatmeal."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
