from utils import Mine_Image

domain = "prnt.sc"

def main():
    print("Welcome to 'Lightshot' Image-Miner!\n")
    n=int(input('Images to Mine: '))
    for x in range(n):
        print(str(x+1) + "/" + str(n) + ": " + Mine_Image(domain))

main()