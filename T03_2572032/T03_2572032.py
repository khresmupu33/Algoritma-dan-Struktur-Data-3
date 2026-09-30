## Definisi Kelas ##
## Definisi Kelas ADTArray
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032
## Definisi Atribut:
# Nmax  : kapasitas maksimum array data (integer)
# data : array/list untuk menyimpan elemen 
#         data bertipe integer (array of integer)
# top     : banyaknya elemen dalam array yang 
#           sudah terisi (integer)
class ADTArray:
    def __init__(self, size):
        self.Nmax = size
        self.data = [None] * size
        self.top = -1
    def isFull(self):
        if self.top == self.Nmax-1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    # X: sebagai nilai yang akan dinput(INT)
    def push(self):
        if self.isFull()==True:
            print("Maafsudah Penuh")
        else:
            X=int(input("Bilangan yang dimasukkan :"))
            self.top+=1
            self.data[self.top]=X
            self.printStack()
    def printStack(self):
        for i in range(self.top+1):
            if i==(self.top) :
                print(f"{self.data[i]} ",end="")
            else:
                print(f"{self.data[i]},",end="")
        print()
    def pop(self):
        if self.isEmpty()==True:
            print("Stack masih kosong")
        else:
            print("Pop: ", self.data[self.top])
            self.data[self.top]=None
            self.top-=1
            self.printStack()
            
    def infoMid(self):
        if self.isEmpty()==True:
            print("Stack masih kosong")
        if self.top<2:
            self.printStack()
        else:
            if (self.top+1)%2==0:
                p=(self.top+1)/2
                for i in range(self.top):
                    if p-1 == i or p==i:
                        print(f"{self.data[i]} ",end="")
            else:
                p=(self.top)//2
                for i in range(self.top):
                    if p == i:
                        print(f"{self.data[i]} ",end="")
            print()
    def clearStack(self):
        if self.isEmpty()==True:
            print("Stack masih kosong")
        else:
            while self.isEmpty()==False:
                self.pop()
            print("Stack telah dibersihkan")
# Kamus Data (Main Program):
#   n           : ukuran dari array.
#   x          : objek instance dari kelas 
#                ADTArray dengan kapasitas 
#                n (ADTArray)
#   tanya       : nilai integer yang ingin 
#               dicari posisinya di dalam 
#               array (integer)
def main():
    n=int(input("N: "))
    x = ADTArray(n)
    print("==== ADT Stack ====")
    print("1. Push")
    print("2. Pop")
    print("3. Info Element Mid")
    print("4. Clear Stack")
    print("0. Exit")
    print("—------------------")
    tanya=int(input("Menu: "))
    while tanya!=0:
        if tanya>-1 and tanya <5:
            if tanya==1:
                x.push()
            if tanya==2:
                x.pop()
            if tanya==3:
                x.infoMid()
            if tanya==4:
                x.clearStack()
        else:
            print("Tolong masukkan pilihan yang valid..")
        tanya=int(input("Menu: "))
    
if __name__ == '__main__':
    main()