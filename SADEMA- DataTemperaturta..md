
#SADEMA-DataTemperatura.

### Rutas:


### Descripción/historia:

Se necesita generar una nueva vista en SADEM, para el control de temperaturas, la idea de esta nueva vista es responder a que cada especie cuenta con una temperatura para su proceso de prefirió diferente, por lo tanto se hace necesario crear un mantenedor que se encargue de registrar los rangos de temperatura mínimos y máximos para cada especie.

### Requisito:

- [ ]  Se exige simplicidad en el desarrollo no sobre extender el requerimiento.

- [x] La Base de datos debe tener seguir el mismo estilo o orden que las demás de Sadema para este caso sadema_data_temperaturas dejo un ejemplo de otro modelo: sadema_prefrios_muestras_temperaturas

- [x] La tabla además de los datos por defecto debe tener los siguientes datos:
      - especie      ->varchar
      - especie_id ->integer
      - temp_min   -> decimal 5.1
      - temp_max   -> decimal 5.1
  
  - [ ] las reglas para la validación son las siguientes:
	  - Max no debe ser menor que Min
	  - Min no debe ser mayor que Max
	  - debemos normalizar de , a .
	  - debemos manejar los valores como numéricos. 

- [x]  Menu dentro de SADEMA/DATA/Temperaturas
  
  