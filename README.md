# Proyecto sistema de recomendación
Proyecto del curso Inteligencia Artificial.
<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Recomendación de productos usando Word2tovect</h3>

  <p align="center">
    Isidora Vasconcellos
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Índice</h2></summary>
  <ol>
    <li>
      <a href="#Sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#run">Como hacerlo funcionar</a></li>
      </ul>
    </li>
    <li>
      <a href="#Como-empezar">Como empezar</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- SOBRE EL PROYECTO -->
## Sobre el proyecto

Este proyecto utiliza el sistema Word2tovect para crear recomendaciones de productos. Este programa recepta los datos sobre el historial de compra de los clientes  a traves de un dataframe para poder evaluar las similitudes con los productos nuevos elegidos y poder devolver una recomendacion de los 5 articulos más similares y los 5 articulos que es mas probable que necesite. 

### Como hacerlo funcionar

* Abrir el archivo similarproducts.py cargar el dataframe de ventas arreglar la variables segun corresponda, y correr el programa. *En este caso no podemos subir el dataframe utilizado en el programa ya que contiene información confidencial de clientes*
* *Id* corresponde a código de producto 
* *Group* corresponde a la categoria del producto 
* *Cliente* Corresponde al código de cliente 

<!-- COMO EMPEZAR-->
## Como Empezar
Creamos un entorno virtual, ya sea con dockers o anaconda con los siguientes requisitos:

### Prerequisitos
-Crear un entorno virtual en anaconda o docker con las siguientes versiones:
* Python 3.9
* Pandas 1.4.0
* gensim 4.1.2
* Numpy 1.22.1
