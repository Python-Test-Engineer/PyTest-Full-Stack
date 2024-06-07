import argparse


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A simple greeting application")

    # Add arguments
    parser.add_argument("--name", help="The name of the person")
    parser.add_argument("--age", type=int, help="The age of the person")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Access the argument and print the greeting
    if args.age:
        print(f"Hello, {args.name}! You are {args.age} years old.")
    else:
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
