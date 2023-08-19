import sys
import requests

def check_directory(target, directory):
    url = f"{target}/{directory}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Directory found: {url}")
    else:
        print(f"Directory not found: {url}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <target> <wordlist>")
        sys.exit(1)

    target = sys.argv[1]
    wordlist_file = sys.argv[2]

    with open(wordlist_file, 'r') as file:
        wordlist = file.read().splitlines()

    for directory in wordlist:
        check_directory(target, directory)

if __name__ == "__main__":
    main()
