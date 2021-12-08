def contador(frase):
    count = 0
    for palabra in frase:
        if palabra == " ":
            count += 1
    
    return count + 1



def run():
    frase = input("¿En qué estas pensando?\n")
    print(contador(frase))


if __name__ == "__main__":
    run()