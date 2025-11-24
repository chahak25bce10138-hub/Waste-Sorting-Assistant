# ----------------------------------------------
# Intelligent Waste Sorting Assistant (IWSA)
# ----------------------------------------------

def detect_category(item):
    item = item.lower()

    recyclable_keywords = ["plastic", "glass", "bottle", "paper", "cardboard", "metal", "can"]
    organic_keywords = ["food", "banana", "apple", "vegetable", "leaf", "peel", "leftover"]
    hazardous_keywords = ["battery", "chemical", "acid", "paint", "medical", "syringe"]
    general_keywords = ["tissue", "wrapper", "dust", "cloth"]

    if any(word in item for word in recyclable_keywords):
        return "Recyclable"
    elif any(word in item for word in organic_keywords):
        return "Organic"
    elif any(word in item for word in hazardous_keywords):
        return "Hazardous"
    elif any(word in item for word in general_keywords):
        return "General Waste"
    else:
        return "Unknown"


def get_instructions(category):
    instructions = {
        "Recyclable": "Place in the recycling bin. Do not crush bottles.",
        "Organic": "Place in the compost or organic waste bin.",
        "Hazardous": "Take to a hazardous waste center. Do NOT throw in regular bins.",
        "General Waste": "Dispose of in the general waste bin.",
        "Unknown": "Category not recognized. Search manually for proper disposal."
    }
    return instructions[category]


def display_result(item, category, instruction):
    print("\n---------------------------------")
    print(f"Item: {item}")
    print(f"Category: {category}")
    print(f"Disposal Method: {instruction}")
    print("---------------------------------\n")


def show_summary(history):
    print("\n========== WASTE SORTING SUMMARY ==========")
    if not history:
        print("No items were sorted.")
    else:
        for h in history:
            print(f"- {h['item']} → {h['category']}")
    print("===========================================\n")


def main_menu():
    history = []

    print("===== Intelligent Waste Sorting Assistant =====\n")

    while True:
        item = input("Enter waste item (or type 'exit'): ")

        if item.lower() == "exit":
            break

        category = detect_category(item)
        instruction = get_instructions(category)
        display_result(item, category, instruction)

        history.append({"item": item, "category": category})

    show_summary(history)
    print("Thank you for helping keep the environment clean!\n")


# Run the program
main_menu()
