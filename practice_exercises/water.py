from soil import sample  # Uncommented the import

def main():
    moisture = sample()  # Get the initial moisture value
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()  # Re-sample the moisture level
        print(f"Moisture is {moisture}%")

    print("Time to water!")    

main()
