from analytics.tools.formatter import format_data

def write_data(data):
    formatted = format_data(data)
    return f"written: {formatted}"