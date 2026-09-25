# 📘 Wiki PHP – Capítulo 9: Manejo de Archivos

## 9.1 🔹 Permisos y Conceptos

Antes de trabajar con archivos:

- El servidor debe tener **permisos de lectura y/o escritura** en la carpeta.
    
- Archivos comunes: `.txt`, `.csv`, `.json`, imágenes.
    
- PHP usa funciones nativas para abrir, leer, escribir y cerrar.
    

---

## 9.2 🔹 Abrir y Cerrar Archivos

Se usa `fopen()` para abrir y `fclose()` para cerrar.

👉 Sintaxis:

`$archivo = fopen("miarchivo.txt", "r"); // r = solo lectura fclose($archivo);`

📌 Modos comunes:

- `"r"` → leer.
    
- `"w"` → escribir (borra contenido anterior).
    
- `"a"` → añadir al final.
    
- `"x"` → crear nuevo, error si existe.
    

---

## 9.3 🔹 Leer Archivos

### Leer línea por línea

`$archivo = fopen("texto.txt", "r");  while(!feof($archivo)) {     echo fgets($archivo) . "<br>"; }  fclose($archivo);`

### Leer todo el archivo

`echo file_get_contents("texto.txt");`

---

## 9.4 🔹 Escribir Archivos

### Sobrescribir (`w`)

`$archivo = fopen("nuevo.txt", "w"); fwrite($archivo, "Hola Mundo\n"); fclose($archivo);`

### Añadir al final (`a`)

`$archivo = fopen("nuevo.txt", "a"); fwrite($archivo, "Nueva línea añadida\n"); fclose($archivo);`

---

## 9.5 🔹 Borrar o Renombrar Archivos

`unlink("archivo.txt");       // eliminar rename("viejo.txt", "nuevo.txt"); // renombrar`

---

## 9.6 🔹 Manejo de Directorios

`mkdir("carpeta");  // crear rmdir("carpeta");  // eliminar`

📌 En Laravel se usa `Storage::makeDirectory()` en vez de funciones crudas.

---

## 9.7 🔹 JSON en PHP

JSON es un formato muy usado en APIs y bases de datos.

### Guardar array en JSON

`$datos = ["nombre" => "Nye", "edad" => 33]; $json = json_encode($datos);  file_put_contents("datos.json", $json);`

### Leer JSON

`$json = file_get_contents("datos.json"); $datos = json_decode($json, true);  echo $datos["nombre"]; // Nye`

📌 `json_decode(..., true)` convierte en array asociativo.  
📌 Sin el `true`, devuelve objeto.

---

## 9.8 🔹 CSV (Excel simple)

Archivos separados por comas (o `;`).

### Leer CSV

`if (($archivo = fopen("data.csv", "r")) !== false) {     while (($fila = fgetcsv($archivo, 1000, ",")) !== false) {         print_r($fila);     }     fclose($archivo); }`

### Escribir CSV

`$archivo = fopen("data.csv", "w"); fputcsv($archivo, ["nombre", "edad"]); fputcsv($archivo, ["Nye", 33]); fclose($archivo);`

---

## 9.9 🔹 Ejemplo Integrador

Supongamos que tenemos un archivo `usuarios.txt` y queremos registrar usuarios nuevos.

`// Guardar usuario $archivo = fopen("usuarios.txt", "a"); fwrite($archivo, "Nye,33\n"); fclose($archivo);  // Leer usuarios $contenido = file_get_contents("usuarios.txt"); echo nl2br($contenido); // muestra con saltos de línea`

---

## ✅ Resumen del Capítulo 9

- **fopen/fclose** → abrir y cerrar archivos.
    
- **fgets / feof** → leer línea por línea.
    
- **file_get_contents** → leer todo de una vez.
    
- **fwrite / file_put_contents** → escribir en archivos.
    
- **unlink / rename / mkdir** → manipular archivos y directorios.
    
- **JSON** → `json_encode` / `json_decode`.
    
- **CSV** → `fgetcsv` / `fputcsv`.
    

---

📌 Con esto ya puedes manejar archivos de texto, JSON y CSV en PHP.  
En **Laravel** esto se simplifica con `Storage`, pero la base sigue siendo la misma.