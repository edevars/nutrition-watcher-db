# Nutritrion Watcher

- El **usuario** podrá iniciar sesión y registrarse
- El **usuario** podrá ingresar un r**egistro diario**, el cual le permitirá ingresar su peso y tallas de la mañana. También llevará un conteo total de las calorías de ese día.  
- Una vez creado el registro se harán recomendaciones de **recetas**.
- Cada **receta** tendrá **ingredientes** y **pasos** para realizar la receta.
- Una vez creado el **registro diario** se mostrará la opción de agregar las recetas a una lista de comida. 
- Las comidas mostrarán si fueron completadas o no. 
- Habrá una opción de seleccionar cuantos **vasos de agua** se tomaron a lo largo del día. 
- Se mostrarán estadísticas detalladas del progreso. 
- Se mostrarán mensajes de motivación aleatorios para continuar con la dieta.  



## Entidades

**Usuarios**

- *Id*

- Nombre
- Foto
- correo electrónico
- contraseña

**Registros diario**

- id

- Peso
- Talla de cintura
- *Fecha*
- Vasos de agua
- Conteo de calorías

**Receta**s

- *Id*

- Calorías
- Foto

**Ingredientes**

- *Id*

- Nombre
- Calorías totales 
- Medida

**Pasos**

- id

- Orden
- Descripción



## Relaciones

- Un **usuario** tiene muchos **registros diarios**.
- Un **registro diario tiene muchas recetas** y una **receta** puede tener muchos **registros diarios**.
- Una **receta tiene** muchos **ingredientes** y un **ingrediente** tiene muchas **recetas**
- Una **receta** tiene muchos **pasos**