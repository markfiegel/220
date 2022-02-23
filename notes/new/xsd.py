def main():
    words = input("enter a sentence to convert to pig latin: ").split()
    for word in words:
        wordes = word[1:] + word[0]
        print(wordes+"ay", end=" ")

main()