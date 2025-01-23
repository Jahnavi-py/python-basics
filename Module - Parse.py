#Write a program to parse command-line arguments using the argparse module.
import argparse
def main():
    parser = argparse.ArgumentParser(description="A program to parse command-line arguments.")
    parser.add_argument("filename", type=str, help="The name of the file to process.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode.")
    parser.add_argument("--lines", type=int, default=10, help="Number of lines to process (default is 10).")
    args = parser.parse_args()
    print(f"Processing file: {args.filename}")
    if args.verbose:
        print("Verbose mode enabled.")
    print(f"Number of lines to process: {args.lines}")
    try:
        with open(args.filename, "r") as file:
            for i, line in enumerate(file):
                if i >= args.lines:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
if __name__ == "__main__":
    main()
