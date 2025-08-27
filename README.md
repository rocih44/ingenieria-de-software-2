# 🧩 Sistema de Gestión de Stock

### Ingeniería de Software II – Trabajo Colaborativo | Grupo 1

---

## Datos académicos

- 📅 Año académico: 2025
- 🏛️ Materia: Ingeniería de Software II
- 👨‍🏫 Docente: Víctor Contreras
- 🏫 Institución: UNPAZ
- 💻Desarrollo:  10 Semanas

---

## Integrantes del equipo

- 👤 Muñoz Codazzi Martin Nahuel  (Líder)
- 👤 Decima Natahel Aaron
- 👤 Brizuela Miguel Angel Jesus
- 👤 Matalla Iván Ezequiel
- 👤 Herrera Rocio Agustina
- 👤 Islas Leonardo Agustín

---

## 🔎Objetivo del proyecto

El propósito consiste en simular el desarrollo profesional de un sistema backend completo, desde su análisis inicial hasta su ejecución  en Docker.

El equipo trabajara colaborativamente durante todo el cuatrimestre para diseñar e implementar un sistema de gestión de stock, enfocado en el control de productos, movimientos de entrada/salida, pruebas automatizadas y registro de usuarios.

---

## 📌 ¿Qué hace el proyecto?

El Sistema de Gestión de Stock con Depósitos permite:

- Gestionar depósitos y productos de forma centralizada.
- Controlar ingresos y salidas de stock.
- Definir niveles mínimos y generar alertas de stock crítico.
- Registrar cada acción con usuario, rol y timestamp.
- Consultar reportes, historial y movimientos.
- Contar con una interfaz web básica generada con Jinja2.
- Brindar una API REST documentada con Swagger para futuras integraciones.

---

## 📚 Material Académico vinculado al Proyecto

Durante la cursada cuatrimestral de Ingeniería de Software II, se verán 5 unidades aplicadas directamente al desarrollo:

- Unidad 1 – Medición y Métricas del Software
- Unidad 2 – Gestión del Riesgo en Ingeniería de Software
- Unidad 3 – Diseño Arquitectónico y Patrones
- Unidad 4 – Prueba de Software
- Unidad 5 – Administración de la Configuración

---

## 👣Pasos para la instalación del proyecto

### Primero hacemos git clone del proyecto o descomprimimos el .zip

```bash
git clone https://github.com/MartinMCodazzi/IS2-2025-grupo1.git
```
---

### Luego, nos dirigimos a la carpeta donde descargamos el proyecto.

```bash
cd ./inventario-2025
```
---

### Abrimos una terminal, y para trabajar con el proyecto en VSCode, copiamos lo siguiente:

```bash
code .
```
---

### La primera vez que usemos este Repositorio debemos escribir:

```bash
git remote add origin https://github.com/MartinMCodazzi/IS2-2025-grupo1.git
```
---

### Al abrirse VSCode, creamos una nueva terminal y escribimos el siguiente comando:

```bash
python -m venv venv
```
---

### Activamos el entorno virtual (**en Windows**)

```bash
.\venv\Scripts\Activate
```
---

### Si aparece un ***mensaje de error***, diciendo que Powershell no tiene permisos de ejecución, podemos usar para chequear si Powershell tiene permisos de ejecución de scripts:

```bash
Get-ExecutionPolicy
```
---

### Si el resultado dice "***Restricted***" podemos activar el virtual environment usando:

```bash
Set-ExecutionPolicy RemoteSigned -Scope Process; .\venv\Scripts\Activate
```
---

### Ahora, debemos ***instalar paquetes base***:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
```
---

### Es recomendable ***instalar las dependencias***, siempre que actualicemos el proyecto. Esto se hace con:

```bash
pip install -r ./requirements.txt
```
---

### Una vez actualizadas/instaladas las dependencias, podemos ejecutar el backend en ***modo desarrollo***:

```bash
fastapi dev ./backend/app/main.py
```
---

La API responderá en [http://127.0.0.1:8000](http://127.0.0.1:8000/) , siempre y cuando no cerremos la terminal.

---

## 🤝 Cómo contribuir

1. Crear una rama nueva en la terminal Bash de VsCode para el desarrollo propio:
```bash	
git branch (nombre de la nueva rama)

git bash - verificar que se creo.

git checkout (nombre de la nueva rama) - para utilizar la nueva rama creada.

git bash - verifica: Ahora el asterisco no esta en la rama 'main', sino en la 'nueva rama', lista para ser utilizada.
```
 
2. Hacer commits claros y descriptivos.
3. Abrir un Pull Request (PR) hacia la rama principal (`main`).
4. El líder del grupo revisará y aprobará los cambios.

---

## 📅 Plan de 10 semanas (iterativo y guiado)

| Semana | Enfoque |
| --- | --- |
| 1 | Setup del entorno, Git y análisis inicial del problema |
| 2 | Diseño de modelo de dominio y estructura del backend |
| 3 | CRUD de productos y depósitos, validaciones |
| 4 | Gestión de movimientos, reglas de negocio |
| 5 | Autenticación y autorización (JWT, roles) |
| 6 | Pruebas de integración + documentación Swagger |
| 7 | Introducción de vistas web con Jinja2 |
| 8 | Formularios y validaciones desde frontend |
| 9 | Reportes y alertas (web y backend) |
| 10 | Docker + CI/CD simulado con GitHub Actions |
---

## 🛠️ Tecnologías usadas

- Editor de código: Visual Studio Code
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Base de datos: SQLite
- Frontend: Plantillas Jinja2
- Pruebas: Pytest + Httpx
- Documentación API: Swagger / OpenAPI (integrado en FastAPI)
- Despliegue en la nube:  (Railway, Render, Vercel, Netlify).
- Seguridad: JWT y roles.
- CI/CD: GitHub Actions
- Contenedores: Docker
- Control de versiones: Git + GitHub

---

## ☑️Finalidad general del sistema

- Controlar ingresos y salidas de productos del inventario.
- Llevar registro detallado de movimientos (stock in / stock out).
- Alertar cuando un producto llega a un  mínimo de stock.
- Ofrecer una API REST para su futura integración con interfaces gráficas.
- Persistir datos en una base relacional (SQLite).
- Ser completamente dockerizable, portable y escalable.
