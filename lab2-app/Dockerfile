# Imagen base ligera de Python
FROM python:3.9-slim
# Directorio de trabajo
WORKDIR /app
# Instalar dependencias
RUN pip install --no-cache-dir flask
# Copiar el código fuente
COPY app.py .
# Exponer el puerto de la aplicación
EXPOSE 5000
# Comando de inicio
CMD ["python", "app.py"]