### Rutas:


```php
	Route::get('Aplicadores/VerificacionAgua/Index',                   'Aplicadores\VerificacionAguaController@Index')->name('aplicadores.verificacionAgua.index');
```


### Descripción/historia:

Se Necesita revisar rango de PH (6,5 - 7,5) y MV (750 - 1.000). generar alerta para parámetros fuera de esos rangos 

### Requisito:

- [ ] Generar alerta para rangos de PH y MV

- [ ] Nada de esto debe ser complejo solón necesitamos definí rangos y pintar los inputs.