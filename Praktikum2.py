# Praktikum 2 - Komputasi Numerik B - Kelompok 12
# Anggota :
# Adhira Riyanti Amanda - 5025211102
# Gabriella Natasya Br Ginting  - 5025211081
# Cavel Ferrari - 5025211198

import numpy as np
import tabulate as tb

# Membuat Array untuk nilai r,xr,fr
r_list = np.array([])
xr_list = np.array([])
fr_list = np.array([])

# Mendefinisikan fungsi persamaan
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
    
    # Tabel titik-titik di dalam selang (a,b)
    while(h*i<=b):
        xr_list = np.insert(xr_list,i, h*i)
        fr_list = np.insert(fr_list,i,f(h*i))
        i+=1

    # Tabel Romberg
    for k in range(0, n):

        arr[k, 0] = ctr(a, b, 2**k)

        for j in range(0, k):
            arr[k, j+1] = (4**(j+1) * arr[k, j] - arr[k-1, j]) / (4**(j+1) - 1)

    return arr

# Input batas integral, fungsi, dan n
print ('Input the Integral Range:')
a = int(input ('Lower Bound = '))
b = int(input ('Upper Bound = '))
function = input('Input the Function = ')
n = int(input('Input n value = '))

rombergTable = rombergIntegration(a, b, n) 
result = round(rombergTable[n-1, n-1],5)

# Menampilkan tabel titik-titik di dalam selang
set_value = {'Xr': xr_list, 'Fr': fr_list}
print(tb.tabulate(set_value, headers = 'keys', tablefmt='fancy_grid', numalign = 'center', showindex=range(0,len(xr_list))))

# Menampilkan tabel hasil integrasi romberg
print("Result Table:")
print(tb.tabulate(rombergTable, tablefmt='fancy_grid',numalign='center',showindex=range(0,n)))
print("Final Result: ", result)