
# 21 nov

Al comparar `nvidia-smi` con `pythorch profiler` obtenemos que:

* la utilizacion de la memoria de nvida-smi se ve afectada x el uso base del sistema, siendo en mi caso de unos 540 mb adicionales.

* En el caso de Vanilla concuerda con eso, mientras que en los de TRT no veo relacion.

* La utilizacion de SM se ve afectada en unos 20 puntos, aunque no puedo determinar la causa, ya que segun nvtop, en idle se tiene 0%

comparaciones: 

| MODEL    | SM % (profiler)  |   Memory mb (profiler)  |SM % (nvidia-smi)  |   Memory mb (nvidia-smi)  |
|----------|------------------|-------------------------|-------------------|---------------------------|
| Vanilla  | none             | 1138                    | 80                | 1791                      |
| TRT fp32 | 50               | 40                      | 60                | 1201                      |
| TRT fp16 | 27               | 40                      | 44                | 931                       |
| TRT int8 | 14               | 40                      | 35                | 760                       |

obs: valores bien aprox

Notas: 

se genero el shell script `gen_tables.sh` que corre diferentes instanciaciones de `main_all.sh` que a su vez corre instancias de `build_all.sh`, el cual genera los `.engine` asi como el `main.py` para generar la tabla.

Meti las tablas generadas en `outputs/table_outputs/` para dejar más limpio todo.

Hay notas utiles de como resolver problemas q tuve con las instalaciones en el [proyecto](https://github.com/users/Juanx65/projects/2) del repositorio, q voy anotando a diario.

# Avances 10 nov

Siguiendo la [documentacion](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#engine-inspector), escribi el script en  `param_counter.py` que suma la totalidad de pesos por capa para entregar el total de parametros de el engine.

luego, comprobando que la cantidad de parametros de pytorch y onnx son las mismas usando [la herramienta onnx-opcounter](https://github.com/gmalivenko/onnx-opcounter); por ejemplo, la cantidad de parametros de [yolov8n-cls](https://docs.ultralytics.com/models/yolov8/#supported-modes) es de 2.7M, mientras que [ onnx-opcounter](https://github.com/gmalivenko/onnx-opcounter) da como resultado 2715880.

Finalmente, usando `param_counter.py` tenemos el resultado de 2711472 parametros para el yolov8n.engine.
 
--- 

Notas: 

Segun la informacion disponible en enlaces como [este](https://stackoverflow.com/questions/70097798/number-of-parameters-and-flops-in-onnx-and-tensorrt-model#:~:text=1,onnx%20model%20here), al optimizar con tesnorRT no cambia el numero de parametros ni de FLOPS amenos de que existan ramas redindantes en la red [almenos para los flops segun esto](https://forums.developer.nvidia.com/t/number-of-operations-in-a-tensorrt-model/77687).

De todas formas [aca](https://stackoverflow.com/questions/70097798/number-of-parameters-and-flops-in-onnx-and-tensorrt-model#:~:text=1,onnx%20model%20here) solo se demuestra que la cantidad de parametros es igual de pytorch a onnx usando esta [herramienta: onnx-opcounter](https://github.com/gmalivenko/onnx-opcounter), la cual solo permite extraer la cantidad de parametros de redes en el formato onnx, no asi de un engine.

Se demostro entonces que la cantidad de parametros de pytorch a onnx a tensorrt son iguales. se suguiere usar texec, herramienta que debido a que incluye el builder para construir el engine no planeo usar.

# Avances 1 nov

det pose con yolov8m-pose
Speed: 1.9ms preprocess, 10.4ms inference, 1.2ms postprocess per image at shape (1, 3, 640, 384)

det pose con fp32
Speed: 2.2ms preprocess, 12.3ms inference, 1.4ms postprocess per image at shape (1, 3, 640, 640)

det pose con fp16
Speed: 2.1ms preprocess, 4.2ms inference, 1.6ms postprocess per image at shape (1, 3, 640, 640)

# Avances 26/oct

* Comparación de tiempos y precisiones entre "sync" y "no sync" (tablas).

    En donde:
    - No se encuentran cambios en la precisión de los modelos.
    - El tiempo de los modelos TRT no cambia significativamente.
    - La latencia del modelo Vanilla ahora sigue la tendencia esperada (ser mayor que la de TRT).

    Cabe notar que:
    - El cambio en el tamaño se debe a que escribí una función que revisara automáticamente el tamaño de los archivos, los cuales antes anotaba revisando según lo visto en "Folders". No lo actualicé en las tablas no-sync, pero deberían ser iguales.
    - Los tiempos a veces varían más, dependiendo de cada ejecución de la validación.

<details><summary>  ResNet152 </summary> 

### Batch Size 1

|  Model          |Latency-all (ms)|Latency-model (ms)|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-----------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla         |    8.1 / 16.3  |  6.0 / 15.9      |241.7      |82.34                 |95.92                |
| TRT fp32-static |    5.5 / 10.0  |  5.1 / 9.5       |243.3      |82.34                 |95.92                |
| TRT fp16-static |    2.2 / 8.6   |  1.8 / 8.1       |122.6      |82.32                 |95.90                |
| TRT int8-static |    1.5 / 4.3   |  1.2 / 3.9       |65.5       |79.99                 |95.74                |


### Batch Size 1 - sync

|  Model          |Latency-all (ms)|Latency-model (ms)|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-----------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla         |  9.3 / 13.6    |  8.8 / 13.0      | 230.5     | 82.34                | 95.92               |
| TRT fp32       |  5.7 / 9.7  |  5.2 / 9.0  | 293.2   | 82.34                | 95.92               |
| TRT fp16       |  2.2 / 3.4  |  1.8 / 2.5  | 116.8   | 82.34                | 95.91               |
| TRT int8       |  1.6 / 5.8  |  1.2 / 5.3  | 62.2    | 79.99                | 95.74               |

### Batch Size 32 

|  Model      |Latency-all (ms)|Latency-model (ms)| size (MB) | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla     | 141 / 181      |  6.3 / 12.3      |241.7      |82.34                 |95.93                |
| TRT fp32    | 75.6 / 96.2    |   69.3 / 89.8    |243.3      |82.34                 |95.92                |
| TRT fp16    | 30.6 / 55.1    | 24.2 / 48.8      |123.0      |82.32                 |95.91                |
| TRT int8    | 18.1 / 36.4    |  11.6 / 25.0     |64.6       |80.01                 |95.79                |

### Batch Size 32 - sync

|  Model          |Latency-all (ms)|Latency-model (ms)|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-----------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla         | 161.5 / 185.2  | 154.9 / 177.9    | 230.5     | 82.35                | 95.93               |
| resnet152       | 73.6 / 84.5 | 67.2 / 78.1 | 231.2   | 82.34                | 95.92               |
| TRT fp16        | 33.2 / 46.0    | 26.4 / 34.1      | 117.7     | 82.34                | 95.90               |

### Batch Size 64

|  Model      |Latency-all (ms)|Latency-model (ms)|size (MB) | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla     | 283  / 355     |  6.3 / 11.1      |241.7      |82.34                 |95.93                |
| TRT fp32    |135.2 / 161.4   |  122.9 / 149.1   |243.3      |82.34                 |95.92                |
| TRT fp16    | 59.4 / 83.4    |  46.8 / 65.3     |123.0      |82.32                 |95.91                |

### Batch Size 64 - sync

|  Model          |Latency-all (ms)|Latency-model (ms)|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-----------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla       | 297.8 / 335.1 | 285.1 / 322.2 | 230.5   | 82.35                | 95.93               |
| TRT fp32       | 136.3 / 163.5 | 123.9 / 150.9 | 231.2   | 82.34                | 95.92               |
| TRT fp16        | 60.3 / 74.4    | 47.4 / 60.6      | 117.7     | 82.34                | 95.90               |

### Batch Size 128

|  Model      |Latency-all (ms)|Latency-model (ms)| size (MB) | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla     | 555.1 / 620    |  6.0 / 9.5       |241.7      |82.39                 |95.93                |
| TRT fp32    | 269.3 / 336.2  |  244.9 / 311.7   |243.3      |82.38                 |95.93                |
| TRT fp16    | 108.3 / 127.8  |   83.4 / 100.0   |123.0      |82.36                 |95.91                |

### Batch Size 128 - sync

|  Model          |Latency-all (ms)|Latency-model (ms)|size (MB)  | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-----------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla         | 530.7 / 623.1  | 506.3 / 598.5    | 230.5     | 82.39                | 95.93               |
| TRT fp32        | 267.9 / 325.2 | 243.5 / 300.6 | 231.2   | 82.38                | 95.92               |
| TRT fp16        | 113.6 / 130.9  | 88.4 / 103.8     | 117.7     | 82.38                | 95.90               |

### Batch Size 256

|  Model      |Latency-all (ms)|Latency-model (ms)| size (MB) | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla     | 1072/1145      |  5.9 / 8.6       |241.7      |82.38                 |95.93                |
| TRT fp32    | 592 / 689      |  543 / 641       |243.3      |82.38                 |95.92                |
| TRT fp16    | 215.2 / 258.3  |  165.7 / 208.3   |123.0      |82.36                 |95.91                |

### Batch Size 256 - sync

|  Model      |Latency-all (ms)|Latency-model (ms)| size (MB) | accuracy (Prec@1) (%)|accuracy (Prec@5) (%)|
|-------------|----------------|------------------|-----------|----------------------|---------------------|
| Vanilla     | 1068.7 / 1229.6| 1020.1 / 1179.9  | 230.5     | 82.38                | 95.93               |
| TRT fp32    | 593.7 / 693.7  |  541.2 / 643.2   | 231.8     |82.38                 |95.92                |
| TRT fp16    | 244.0 / 294.6  | 193.4 / 235.6    | 117.7     | 82.38                | 95.90               |

</details>

* Programe un script que permita evaluar tanto los pesos preentrenados Vanilla para la segmentación de salmones, como el engine optimizado TRT en fp16 y fp32.

    Cabe notar que:
    - Hasta el momento, no ha sido posible generar los engines optimizados utilizando mi propio flujo de trabajo. En su lugar, optimicé la red usando las herramientas disponibles en Ultralytics. Estas herramientas permiten usar fp32, fp16, batch size estático y dinámico. Sin embargo, el uso del batch size dinámico es más limitado, ya que no me permite generar en fp16. Aún estoy revisando sus parámetros (flags).

## batch size 1 (map sobre mask)

|  Model      |Latency (ms)| size (MB) | mAP50 (%) |mAP50-95 (%) |
|-------------|------------|-----------|-----------|-------------|
| Vanilla     | 23.4       | 54.8      | 51.7      | 25.2        |
| TRT fp32    | 14.6       | 157.2     | 50.7      | 25.1        |
| TRT fp16    | 4.9        | 58.6      | 51.2      | 25.2        |