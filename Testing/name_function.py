def get_formatted_name(first, last):
    """Build a formatted full name."""
    try:
        # Check if first or last name is empty or contains only whitespace characters.
        if not first.strip() or not last.strip():
            raise ValueError("Both first name and last name must be provided.")
        
        # Format the full name and return it.
        full_name = first.strip() + " " + last.strip()
        return full_name.title()
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"An error occurred: {e}"
