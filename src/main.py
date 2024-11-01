from wrapper import *

def main():
    request: Request = Request("https://www.google.com")
    print(request.get_data().status_code)
    print(request.get_data().text)

if __name__ == "__main__":
    main()