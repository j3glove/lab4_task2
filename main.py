import random
import time

def printmatrix(matrix):
    print("\n")
    for i in matrix:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()
def summatrix(matrix1,matrix2): #Сложение матриц
    summa=[[0]*len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            summa[i][j]=matrix1[i][j]+matrix2[i][j]
    return summa

def diffmatrix(matrix1, matrix2): #Разница матриц
    diff = [[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            diff[i][j] = matrix1[i][j] - matrix2[i][j]
    return diff

def multimatrix(matrix1, matrix2): #Умножение двух матриц
    multi = [[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for u in range(len(matrix1)):
            for j in range(len(matrix1)):
                multi[i][u] += matrix1[i][j] * matrix2[j][u]
    return multi

def multidigit(matrix1,K): #Умножение матрицы на число
    mdigit=[[0] * len(matrix1) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            mdigit[i][j] = matrix1[i][j]*K
    return mdigit

        #пользовательский ввод
while True:    #Ввод числа N
    N = input("Введите число N без пробелов в диапазоне от 6 до 1000 включительно:    ")
    if N.isdigit():
        N=int(N)
        if N >= 6 and N <= 1000:
            break
        else:
            print("Вы ввели число не входящее в диапазон")
    else:
        print("Вы некорректно ввели число")


while True: #Ввод числа K
    minusflag = False
    K = input("Введите K число без пробелов   ")
    K=K.strip()
    if K[0]=="+" or K[0]=="-":
        if K[0]=="-":
            K = K.replace("-","")
            minusflag=True
        else:
            K = K.replace("+","")
    if K.isdigit():
        if minusflag == True:
            K = - int(K)
            break
        else:
            K=int(K)
            break
    else:
        print("Вы неккоректно ввели число")

startpoint=0 #Переменная которая помогает нам разделять на области матрицы
finishpoint=N//2 #Переменная которая помогает нам разделять на области матрицы
count2=0 # Счетчик положительных элементов в четных столбцах матрицы C во второй области
count4=0 # Счетчик отрицательных элементов в нечетных столбцах матрицы C в четвертой области


try:
    start=time.time()
    A=[[0]*N for i in range(N)] # создание матрицы A
    for i in range(N):
        for j in range(N):
            A[i][j] = random.randint(-10,10)
    print("Матрица: A")
    printmatrix(A)

    B = [[0]*int(N//2) for i in range(N//2)] # создание матрицы B
    for i in range(int(len(A)//2)):
        for j in range(int((len(A))//2)):
            B[i][j]=A[i][j]
    print("Матрица: B")
    printmatrix(B)
    C = [[0]*int(N//2) for i in range(N//2)] # создание матрицы C
    for i in range(int(len(A)//2)):
        for j in range(int((len(A)+1)//2),len(A)):
            C[i][j-int((N+1)/2)]=A[i][j]
    print("Матрица: C")
    printmatrix(C)
    E = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы E
    for i in range((int(len(A)+1) // 2),len(A)):
        for j in range(int((len(A) + 1) // 2), len(A)):
            E[i - int((N+1)/2)][j - int((N + 1) / 2)] = A[i][j]
    print("Матрица: E")
    printmatrix(E)
    D = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы D
    for i in range(int(len(A) // 2),len(A)):
        for j in range(int((len(A)) // 2)):
            D[i-int((N+1)/2)][j] = A[i][j]
    print("Матрица: D")
    printmatrix(D)
    Atransp=[[0]*N for i in range(N)] # создание матрицы A транспонированной
    for i in range(N):
        for j in range(N):
            Atransp[i][j]=A[j][i]
    print("Матрица: Atransp")
    printmatrix(Atransp)
    F = [[0] * N for i in range(N)]  #Создание матрицы F равной A
    for i in range(N):
        for j in range(N):
            F[i][j] = A[i][j]
    print("Матрица: F")
    printmatrix(F)
    for i in range(N//2): # Счетчик положительных элементов в четных столбцах матрицы C во второй области
        for j in range(startpoint,finishpoint):
            if j%2==0 and C[i][j]>0:
                count2+=1
                startpoint+=1
                finishpoint-=1

    startpoint=0
    finishpoint=N//2

    for i in range(N//2): # Счетчик отрицательных элементов в нечетных столбцах матрицы C в четвертой области
        for j in range(finishpoint-1,startpoint,-1):
            if j%2==1 and C[i][j] < 0:
                count4+=1
                startpoint+=1
                finishpoint-=1



    startpoint=0
    finishpoint=N//2
    if count2 > count4: # При выполнении этого условия мы меняем 1 и 3 области местами
        for i in range(N//4):
            for j in range(startpoint,finishpoint):
                C[j][i],C[j][N//2-i-1] = C[j][N//2-i-1],C[j][i]
            startpoint+=1
            finishpoint-=1
        for i in range(N//2):
            for j in range((N+1)//2,N):
                F[i][j]=C[i][j-N//2-N%2]
    else:
        for i in range(N//2):
            for j in range((N+1)//2,N):
                F[i][j]=E[i][j-N//2-N%2]
        for i in range((N+1)//2,N):
            for j in range((N+1)//2,N):
                F[i][j]=C[i-N//2-N%2][j-N//2-N%2]
    print("Преобразованная Матрица F:")
    printmatrix(F)

    result=[[0]*N for i in range(N)] #Итоговая матрица
    result=diffmatrix(multimatrix(summatrix(F,A),Atransp),multidigit(F,K))
    print("Результат")
    printmatrix(result)
    finish=time.time()
    print("Время работы программы: ",finish-start," sec.")
except ValueError:
    pass
