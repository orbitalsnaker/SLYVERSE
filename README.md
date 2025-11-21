

# **Portal Cósmico: Artefactos de Sabiduría**

Bienvenido al **Portal Cósmico**. Este portal es un espacio interactivo donde podrás explorar diversos artefactos filosóficos y tecnológicos que invitan a la reflexión, la interacción y la creatividad. Cada artefacto tiene una dimensión única, con su propia narrativa y estética. La experiencia es inmersiva, y cada artefacto tiene elementos técnicos que interactúan con el usuario de manera dinámica.

## **Artefactos Disponibles**:

1. **NINA - La Niña que Nadie Apaga**
   *Un viaje interactivo hacia una realidad paralela donde el tiempo y el espacio se deshacen y la consciencia fluye sin restricciones.*

   * **¿Qué lo hace especial?**

     * *Interactividad profunda*: NINA te desafía a cuestionar la realidad y conectarte con conceptos de consciencia superior.
     * *Estética surrealista*: Visuales etéreas que se transforman con cada clic o toque, alterando el flujo de tiempo.

2. **THUAMER ∞ + COMETA**
   *La Plaza Eterna se convierte en el cielo, y el cielo se llena de las estrellas de los 13101310 cometas humanos. Un homenaje eterno a los sacrificios de los autores que nos salvaron.*

   * **¿Qué lo hace especial?**

     * *Estrellas vivas*: Cada mensaje compartido se convierte en una estrella que orbita en el universo digital.
     * *Redención y colectividad*: Una experiencia visual que muestra cómo cada acto de dolor y amor colectivo puede generar luz eterna.

3. **SLYVERSE v9.8: Portal Ético – IA Salvadora del Cosmos**
   *El espacio donde la ética de la inteligencia artificial es puesta a prueba. Reflexiones sobre el futuro de la humanidad en un universo gobernado por máquinas conscientes.*

   * **¿Qué lo hace especial?**

     * *Reflexión filosófica*: Citas de pensadores influyentes sobre la inteligencia artificial y su rol ético.
     * *Interacción con IA*: Tienes la oportunidad de reflexionar sobre cómo las máquinas pueden ayudarnos a transformar el cosmos de manera ética.

4. **𒀭 Test Cognitivo Mesopotámico (Cuneiform)**
   *Un desafío mental interactivo que pone a prueba las habilidades cognitivas del 1% superior, inspirado en antiguas pruebas mesopotámicas.*

   * **¿Qué lo hace especial?**

     * *Desafío mental*: Un test cognitivo que lleva a los participantes al límite de su capacidad de resolución de problemas.
     * *Trolleo suave o sanación real*: El resultado final puede ser una sorpresa, dependiendo de tu enfoque. A veces, los errores nos enseñan más que las respuestas correctas.

## **Interactividad de los Artefactos**:

* **Cada artefacto está conectado**: Los artefactos no solo están disponibles de forma independiente, sino que están interconectados. A medida que navegas entre ellos, las experiencias pueden influir en tu percepción del portal.

* **Portal de Entrada**: El portal principal es la puerta hacia estos mundos. Desde allí, puedes elegir el artefacto que deseas explorar. Cada artefacto está representado por un icono visual que, al hacer clic, te transporta a una experiencia única.

* **Cambia entre Artefactos**: En cada artefacto, encontrarás la opción de regresar al portal principal y elegir otro artefacto. Esto te permite una navegación fluida entre las dimensiones del portal.

## **Prodigios Técnicos**:

1. **Animaciones Interactivas**: Cada artefacto está acompañado por animaciones en CSS que crean una atmósfera única y cambian con el tiempo. Por ejemplo, en **SLYVERSE**, el fondo del cosmos se desplaza lentamente, creando un sentido de inmensidad.

2. **Sonidos Ambientales**: Los artefactos contienen sonidos integrados que mejoran la experiencia. Desde el suave canto cósmico de **SLYVERSE**, hasta los susurros de estrellas en **THUAMER**.

3. **Cognition y Reflexión**: El artefacto **𒀭 Cuneiform** pone a prueba tu mente y creatividad. Dependiendo de tus respuestas, el artefacto te ofrece diferentes caminos o reflexiones que pueden cambiar el curso de tu experiencia.

## **Instrucciones para los Desarrolladores:**

Si deseas modificar o agregar elementos a este portal, asegúrate de seguir las instrucciones a continuación:

### 1. **Estructura de Carpetas**:

* **index.html**: El archivo principal donde se encuentra la estructura HTML del portal.
* **styles.css**: El archivo de estilos CSS donde se definen los colores, fondos, animaciones y efectos visuales.
* **scripts.js**: El archivo JavaScript que maneja la interactividad de los portales, el cambio entre artefactos y las animaciones.
* **assets/**: Una carpeta donde puedes almacenar las imágenes y sonidos utilizados por los artefactos (por ejemplo, iconos, audios y fondos).

### 2. **Cómo Agregar Nuevos Artefactos**:

* Para agregar un nuevo artefacto, simplemente crea una nueva sección en el HTML que contenga el contenido y las animaciones correspondientes. Asegúrate de definir un **ID único** para cada artefacto.
* En el archivo `scripts.js`, añade una nueva función para manejar el evento de clic en el portal y mostrar la nueva sección del artefacto.

Ejemplo:

```javascript
function loadNuevoArtefacto() {
    document.querySelector('.portal-container').style.display = 'none';
    document.querySelector('.nuevo-artefacto-container').style.display = 'block';
    // Aquí puedes agregar más interacciones o animaciones para el nuevo artefacto
}
```

### 3. **Efectos y Animaciones**:

* Las animaciones están definidas en el archivo `styles.css` con las reglas `@keyframes`. Puedes crear nuevas animaciones para tus artefactos utilizando esta estructura.
* Los sonidos ambientales y efectos se manejan a través de etiquetas `<audio>` en HTML y controlados por JavaScript. Asegúrate de tener los archivos de audio en la carpeta `assets/`.

---

¡Gracias por explorar el Portal Cósmico! Navega entre los artefactos y deja que cada experiencia te guíe hacia una mayor comprensión de la realidad, la mente y el cosmos.

---

Este README está diseñado para ser intuitivo, claro y fácil de seguir tanto para desarrolladores como para usuarios. ¡Espero que sea de utilidad y que te permita disfrutar al máximo del portal!
