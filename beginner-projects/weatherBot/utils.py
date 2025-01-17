import datetime

# Log errors to a file
def log_error(error_message):
    with open("error_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {error_message}\n")
