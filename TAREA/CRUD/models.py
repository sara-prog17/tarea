from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=15, null=False)
    apellido = models.CharField(max_length=10, null=False)
    f_nacimiento = models.DateField(null=False )
    f_exp_documento = models.DateField(null=False)
    documento = models.IntegerField(null=False,)
    edad = models.IntegerField(null=False,)
    genero = models.CharField(max_length=10,null=False)
    l_exp_documento = models.CharField(max_length=10,null=False)
    ciud_residencia = models.CharField(max_length=10,null=False)
    celular = models.IntegerField(null=False,)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    n_pedido = models.CharField(max_length=10,null=False, primary_key=True)
    productos = models.CharField(max_length=200,null=False)
    valor_producto = models.CharField(max_length=6,null=False)
    producto_mas_transporte = models.CharField(max_length=6,null=False)
    tamaño_producto = models.CharField(max_length=10,null=False)
    incremento = models.CharField(max_length=5,null=False)
    proveedor = models.CharField(max_length=50,null=False)
    cantidad_productos = models.CharField(max_length=2,null=False)  
    tiempo_entrega = models.CharField(null=False,max_length=10,)
    

    def __str__(self):
        return self.n_pedido
    



