import json
import random

bad_beans = ["Piss",
             "Barf",
             "Toothpaste",
             "Booger",
             "Rotten Egg",
             "Baby Wipes",
             "Black Pepper",
             "Skunk Spray",
             "Moldy Cheese",
             "Willow's Coochie",
             "Motor Oil",
             "Dried Blood",
             "Ear Wax",
             "Pencil Shavings",
             "Canned Dog Food",
             "Centipede",
             "Stinky Socks",
             "Lawn Clippings",
             "Spoiled Milk",
             "Dead Fish",
             "Stink Bug",
             "Dirty Dishwater",
             "Old Bandage",
             "Liver & Onion",
             "Evil Coconut",
             "Benry",
             "Cum"]

good_beans = ["Water Gate Salad", "Cream Cheese", "Lemon", "Peach", "Berry Blue", "Juicy Pear", "Buttered Popcorn", "Coconut", "Plum", "Licorice",
              "Caramel Corn", "Lime", "Cafe Latte", "Chocolate Pudding", "Strawberry Jam",
              "Tutti-Frutti", "Strawberry Banana Smoothie", "Toasted Marshmallow", "Birthday Cake", "Pomegranate",
              "Cappuccino"]


def bean_picker_9000():
    bean_pick = ["Bad", "Good"]
    with open("Bean/beanlist.json", encoding="UTF-8") as bean_list:
        bean_list = json.load(bean_list)
    bean_pick = random.choice(list(bean_pick))
    if bean_pick == "Bad":
        picked_bean = random.choice(list(bad_beans))
        bean_descript = bean_list["Bad"][0][picked_bean].lower()
        return f"The unforunate bean picked: {picked_bean}. \nDescription: {bean_descript}."
    else:
        picked_bean = random.choice(list(good_beans))
        bean_descript = bean_list["Good"][0][picked_bean].lower()
        return f"The lucky bean picked: {picked_bean}. \nDescription: {bean_descript}"


bean_picker_9000()

# with open("Bean/beanlist.json", encoding="UTF-8") as bean_list:
#     bean_list = json.load(bean_list)
#
#     print(bean_list["Good"][0])
