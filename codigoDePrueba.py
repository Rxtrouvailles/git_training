# input=open('/home/JC/Escritorio/entrada','r')
# output=open('/home/JC/Escritorio/salida','w')

# inputline=input.readline()

# # print(type(inputline))

# print(inputline.split())
# print('--------*--------')


# while (inputline):
#   print(inputline)
#   inputline=input.readline()
  

# print('-----------------')
# print(inputline.split())


# crea una matriz de n elementos



# m=int(input('valos de filas?: '))
# n=int(input("valor de columnas?: "))
# arreglo=[[0] * n for i in range (0,m)]

# for i in range(0,n)


# print(arreglo[2][3])


# import tkinter

# root=tkinter.Tk().mainloop()
# # root.mainloop()

""" import tkinter as tk

from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Hola MG! \n Dame un abrazito!\n si me lo das maybe dios te perdone tus pecados").grid(column=0, row=0)
ttk.Button(frm, text="si", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="quien es dios?", command=root.destroy).grid(column=1, row=1)

root.mainloop() """


# matriz3d=[[[0]8*3]]*5

m=[[0]*5]*8

print(m)


for i in range(0,30):
    m.extend([5])
    print(m)

print(type(m))


