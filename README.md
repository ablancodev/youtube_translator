
# YouTube Translator

## Descripción
YouTube Translator es una herramienta que permite a los usuarios descargar el audio de videos de YouTube, 
transcribir este audio a texto y luego traducir el texto a otro idioma. Este proyecto utiliza el API de OpenAI 
para las funciones de transcripción y traducción.

## Requisitos
- Python 3.x
- Bibliotecas de Python: `pytube`, `openai`
- API Key de OpenAI

## Instalación
Instalar las dependencias necesarias:
   ```
   pip install pytube openai
   ```

## Uso
Para usar el script, necesitas pasar el ID del video de YouTube como argumento:
```
python youtube_translator.py [YouTube Video ID]
```

## Configuración
Es necesario configurar tu API Key de OpenAI en el script. Asegúrate de reemplazar `openai_api_key` con tu propia clave:
```python
openai_api_key = 'tu_api_key'
```

## Contribuciones
Las contribuciones son bienvenidas, así que dale a la estrellita y comparte.
