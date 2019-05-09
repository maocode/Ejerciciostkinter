#!/usr/bin/env python
# coding: utf-8

# ## Ventana Basica con tkinter

# Importamos la Biblioteca

# In[6]:


from tkinter import *


# Declaramos una variable y le asignamos la funcion Tk()

# In[7]:


v=Tk()


# Le agregamos el titulo a la ventana con la propiedad title

# In[8]:


v.title("GUI CON TKINTER")


# Colocamos la propiedad geometry para darle posicion a la ventana

# In[9]:


v.geometry("600x400+600+400")


# Le asignamos a nuestra ventana un bucle infinito para ejecutarla

# In[10]:


v.mainloop()


# In[ ]:




