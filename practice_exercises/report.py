def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))



def create_report(spacecraft):   
    return f"""

    ========= REPORT =========
    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU

    ==========================
    """


if __name__ == "__main__":
    main()