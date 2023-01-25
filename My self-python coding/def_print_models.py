def print_models(unprinted_designs, completed_models):
    """the function simulates model printing until the list is empty"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Printing 3D simulation
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Display information about all printed models"""
    print("\nThe following models have been printed: ")
    print("_______________________________________")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "watch strap"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
