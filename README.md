# Pabrikskuy
Tugas Besar II3160 - Teknologi Sistem Terintegrasi http://pabrikskuy.dze3e9ekb7fxh6dz.southeastasia.azurecontainer.io/docs

# Membuat Virtual Environtment
`python -m venv env`

# Installation
`pip install fastapi uvicorn`

# Run Code
`uvicorn sneakersconsult:app --reload`

# Menggunakan Docker
```
# Menggunakan Python image resmi dari Docker Hub
FROM python:3`

# Menentukan directory dalam container
ADD <file_name.py> .

# Menyalin konten directory saat ini ke container di /app
COPY . /<folder_name>
WORKDIR /<folder_name>

# Menginstall dependencies yang dibutuhkan
RUN pip install fastapi uvicorn <other packages>

# Command untuk run FastAPI server saat container dimulai
CMD ["uvicorn", "<folder_name>", "--host", "0.0.0.0", "--port", "80"]
```

# Deploy in Microsoft Azure
1. Buatlah Azure Container Registry Service
2. Buka directory ini, Login ke Azure Server Container Registry menggunakan Docker
`docker login <container_server> -u <container_username> -p <container_password>`
3. Buatlah Docker Image
`docker build -t <container_server>/<image_name>:<image_tag> .`
4. Push Docker Image
`docker push <container_server>/<image_name>:<image_tag>`
5. Buatlah Azure Container Instance
