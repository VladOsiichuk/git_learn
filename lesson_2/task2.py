#task2
def main():

    num = input("Введіть число: ") #user numbers
    num = float(num)

    result = ((num+1)**2) - ((num-1)**2) #calculation

    print("Відповідь:", result) #output
if __name__=="__main__":
    main()