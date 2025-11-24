# -----------------------------------------------------------
# 🌱 Waste Sorting Helper
# A simple, friendly assistant to help you figure out
# where to throw your waste items.
# -----------------------------------------------------------

def figure_out_category(item_name):
    """
    Checks the item name and guesses which waste category it belongs to.
    """
    item_name = item_name.lower()

    recyclable_words = ["plastic", "glass", "bottle", "paper", "cardboard", "metal", "can"]
    organic_words = ["food", "banana", "apple", "vegetable", "leaf", "peel", "leftover"]
    hazardous_words = ["battery", "chemical", "acid", "paint", "medical", "syringe"]
    general_words = ["tissue", "wrapper", "dust", "cloth"]

    if any(word in item_name for word in recyclable_words):
        return "Recyclable"
    elif any(word in item_name for word in organic_words):
        return "Organic"
    elif any(word in item_name for word in hazardous_words):
        return "Hazardous"
    elif any(word in item_name for word in general_words):
        return "General Waste"
    else:
        return "Unknown"


def how_to_dispose(category_name):
    """
    Gives a simple instruction on how to deal with the waste.
    """
    tips = {
        "Recyclable": "Great! Put this in your recycling bin. Make sure it's clean if you can.",
        "Organic": "Yum! Compost this or put it in the organic waste bin.",
        "Hazardous": "Be careful! Take this to a hazardous waste center. Don't throw it in normal trash.",
        "General Waste": "Just toss it in the regular trash bin.",
        "Unknown": "Hmm… not sure about this one. Maybe check online for proper disposal."
    }
    return tips[category_name]


def show_item_result(item_name, category_name, instructions):
    """
    Prints out the item info in a friendly, easy-to-read format.
    """
    print("\n---------------------------------------------")
    print(f"Item: {item_name}")
    print(f"Looks like it's: {category_name}")
    print(f"What to do: {instructions}")
    print("---------------------------------------------\n")


def show_overall_summary(sorted_items):
    """
    At the end, give the user a summary of everything they sorted.
    """
    print("\n===== Here's a summary of your session =====")
    if not sorted_items:
        print("You didn't sort anything this time.")
    else:
        for entry in sorted_items:
            print(f"- {entry['item']} went into {entry['category']}")
    print("============================================\n")


def main():
    """
    Runs the main interactive loop.
    """
    history = []

    print("🌿 Hey there! Welcome to your friendly Waste Sorting Helper!")
    print("I'll help you figure out where your items should go.\n")

    while True:
        user_input = input("Type the name of a waste item (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        category = figure_out_category(user_input)
        instructions = how_to_dispose(category)
        show_item_result(user_input, category, instructions)

        history.append({"item": user_input, "category": category})

    show_overall_summary(history)
    print("Thanks for sorting responsibly! Every little bit helps 🌍💚")


# Start the assistant
main()
