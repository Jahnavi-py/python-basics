#Write a Python script to simulate a TimeoutError by raising it manually and handling it gracefully.
def simulate_timeout(Condition):
    if Condition:
        raise TimeoutError("The operation timed out. Please try again later.")
    else:
        print("Operation completed successfully.")
def main():
    #Condition = input("Simulate timeout? (yes/no): ").strip().lower() == "yes"
    try:
        simulate_timeout(Condition=True)
        #simulate_timeout(Condition)
    except TimeoutError as e:
        print(f"Error: {e}")
    else:
        print("No errors encountered.")
    finally:
        print("Execution completed. Cleaning up resources if needed.")
main()