def safe_divide(numerator, denominator):
    try:
        # Try converting both inputs to float
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            raise ZeroDivisionError
        
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"Other error: {e}"
