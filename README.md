# P2_Komnum_B_12

**Praktikum 2 Komputasi Numerik**  
**Kelas Komputasi Numerik (B)**

**Kelompok 12**
| **No** | **Nama** | **NRP** | 
| :-------------: | ------------- | :---------: |
| 1 | Adhira Riyanti Amanda  | 5025211102 | 
| 2 | Gabriella Natasya Br Ginting | 5025211081 |
| 3 | Cavel Ferrari | 5025211198 |


## Metode Integrasi Romberg

 Integrasi Romberg merupakan teknik yang digunakan dalam integrasi numerik untuk Integrasi Romberg merupakan teknik yang digunakan dalam integrasi numerik untuk menganalisis kasus dimana fungsi yang akan diintegrasikan tersedia. Teknik ini memiliki menganalisis kasus dimana fungsi yang akan diintegrasikan tersedia. Teknik ini memiliki keunggulan untuk menghasilkan nilai-nilai dari fungsi yang digunakan untuk mengembangkan keunggulan untuk menghasilkan nilai-nilai dari fungsi yang digunakan untuk mengembangkan skema yang efisien bagi pengintegrasian secara numerik. Integrasi Romberg didasarkan pada skema yang efisien bagi pengintegrasian secara numerik. Integrasi Romberg didasarkan pada [*ekstrapolasi Richardson*](https://en.wikipedia.org/wiki/Richardson_extrapolation), yaitu metode untuk mengkombinasikan dua perkiraan integral secara numerik untuk memperoleh nilai ketiga, yang lebih akurat.
 
 ## Implementasi Romberg pada Program Python
 
 Pertama-tama, Membuat Array untuk nilai r,xr,fr 
 ```py
 r_list = np.array([])
xr_list = np.array([])
fr_list = np.array([])
```
lalu mendefinisikan fungsi persamaanya dan tabelnya.
 ```py
 def f(x):
    f = eval(function)
    return f

def ctr(a, b, n):

    h = (b - a) / n
    x = a

    sum = 0
    for i in range(1, n):
        x += h
        sum += 2*f(x)

    return h*0.5*(f(a) + sum + f(b))

def rombergIntegration(a,b,n):

    global r_list, xr_list, fr_list
    
    h = (b - a) / n
    i = 0
    arr = np.zeros((n, n))
  
    while(h*i<=b):
        xr_list = np.insert(xr_list,i, h*i)
        fr_list = np.insert(fr_list,i,f(h*i))
        i+=1
        
    for k in range(0, n):

        arr[k, 0] = ctr(a, b, 2**k)

        for j in range(0, k):
            arr[k, j+1] = (4**(j+1) * arr[k, j] - arr[k-1, j]) / (4**(j+1) - 1)

    return arr

 ```
Setelah itu kita dapat memasukan batas integral, fungsi, dan n yang akan dihitung

```py
print ('Input the Integral Range:')
a = int(input ('Lower Bound = '))
b = int(input ('Upper Bound = '))
function = input('Input the Function = ')
n = int(input('Input n value = '))

rombergTable = rombergIntegration(a, b, n) 
result = round(rombergTable[n-1, n-1],5)
```
Dan tampilkan hasilnya

```py
print("Result Table:")
print(tb.tabulate(rombergTable, tablefmt='fancy_grid',numalign='center',showindex=range(0,n)))
print("Final Result: ", result)
```
