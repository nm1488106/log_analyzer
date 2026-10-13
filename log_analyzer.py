def analyze_logs(filename):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(filename, "r") as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    return counts


if __name__ == "__main__":
    result = analyze_logs("sample.log")

    print("Log Analysis Results")
    print("--------------------")
    print("INFO messages:", result["INFO"])
    print("WARNING messages:", result["WARNING"])
    print("ERROR messages:", result["ERROR"])

    if result["ERROR"] > 0:
        print("Application Health: ATTENTION REQUIRED")
    else:
        print("Application Health: NORMAL")

        