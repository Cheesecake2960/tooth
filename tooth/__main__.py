from .main import Tooth

def main():
    tooth = Tooth()
    while True:
        input_text = input(">> ")
        answer_text = tooth.generate(input_text)
        print(answer_text)

if __name__ == "__main__":
    main()