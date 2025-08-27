# 📑 Documento de Casos de Uso  
En este documento redactaremos los casos de uso clave del proyecto *Sistema de Inventario con Depósitos*.  
Cada caso de uso identifica a los actores principales, su objetivo, y las condiciones necesarias antes y después de su ejecución.



## 📌 Índice

- [Casos de uso](#casos-de-uso)
  - [CU 1: ABM de productos y depósitos](#cu-1-abm-de-productos-y-depósitos)
  - [CU 2: Movimiento de stock](#cu-2-movimiento-de-stock)
  - [CU 3: Login y permisos](#cu-3-login-y-permisos)
  - [CU 4: Consulta de stock](#cu-4-consulta-de-stock)
  - [CU 5: Alertas](#cu-5-alertas)



## 🌀Casos de uso

### CU 1: ABM de productos y depósitos

- ***Actor Principal:*** Administrador, Sistema  
- ***Objetivo:*** El administrador puede crear, editar y eliminar productos y depósitos en el sistema. Para los productos, se registran atributos como nombre, SKU, categoría, descripción y unidad de medida. Para los depósitos, se registra su ubicación y capacidad máxima de almacenamiento. El sistema verifica que no se dupliquen identificadores y que se respeten las reglas definidas, asegurando que la información sea precisa y esté actualizada. De esta forma, se mantiene una base de datos controlada y confiable. El stock total de cada producto se calcula automáticamente sumando el stock en cada depósito.  
- ***Precondición:*** El administrador debe estar logueado y con permisos activos.  
- ***Postcondición:*** Se actualiza la base de datos con los cambios aplicados a productos o depósitos.  

---

### CU 2: Movimiento de stock

- ***Actor Principal:*** Operador de depósito  
- ***Objetivo:***  El operador debe registrar las entradas y salidas de productos en cada depósito, indicando el tipo de movimiento, la cantidad de productos, la fecha, el usuario responsable y el motivo del movimiento. El sistema verifica que no se intente retirar más productos de los que hay disponibles en el depósito y actualiza automáticamente los niveles de stock por producto y depósito. Cada acción queda registrada para poder rastrear y controlar el historial de movimientos. De esta forma, se puede monitorear constantemente la disponibilidad de productos y tener un mejor control logístico.  
- ***Precondición:*** Deben existir productos y depósitos previamente creados.  
- ***Postcondición:*** El stock del producto se actualiza en el depósito correspondiente.  

---

### CU 3: Login y permisos

- ***Actor Principal:*** Usuario (Administrador u Operador de depósito)  
- ***Objetivo:*** Para acceder al sistema, el usuario debe ingresar con su usuario y contraseña vinculados a sus credenciales válidas. Una vez autenticado, el sistema asigna un token de seguridad (JWT) que define los permisos correspondientes, qué puede hacer y qué no. Los administradores pueden gestionar productos, depósitos y usuarios, mientras que los operadores se encargan de los movimientos. El sistema asegura que cada acción quede vinculada con el usuario que la realizó y la fecha/hora exacta (timestamp) en que se ejecutó. De esta forma, se garantiza la seguridad y se evita el acceso no autorizado, protegiendo la integridad del sistema.  
- ***Precondición:*** El usuario debe estar registrado en el sistema con un rol definido.  
- ***Postcondición:*** El usuario obtiene acceso al sistema con permisos según su rol.  

---

### CU 4: Consulta de stock

- ***Actor Principal:*** Administrador u Operador de depósito  
- ***Objetivo:***  El usuario puede ver el stock total disponible por producto y por cada depósito. El sistema muestra la información de manera clara y organizada, permitiendo filtrar por fechas, usuario, tipo. De esta forma, se puede conocer rápidamente la cantidad total de stock y dónde se encuentra. Además, se puede revisar el historial de movimientos del producto para tomar decisiones informadas sobre reposición o traslado. El sistema asegura que la información sea precisa y esté actualizada.  
- ***Precondición:*** Deben existir movimientos y productos previamente cargados.  
- ***Postcondición:*** El sistema muestra un reporte del stock solicitado.  

---

### CU 5: Alertas

- ***Actor Principal:*** Sistema  
- ***Objetivo:*** El sistema genera alertas automáticas cuando el stock de un producto en un depósito alcanza el nivel mínimo establecido. Esto permite anticipar y prevenir quiebres de stock, asegurando que las operaciones sigan funcionando sin problemas. El administrador puede configurar los niveles mínimos para cada producto y recibir notificaciones cuando se acerque al límite. De esta forma, puede tomar medidas rápidas para reponer o comprar productos, reduciendo los riesgos logísticos y mejorando la eficiencia.  
- ***Precondición:*** El producto debe tener configurado un nivel mínimo de stock.  
- ***Postcondición:*** El sistema emite la alerta y la registra el movimiento hecho.