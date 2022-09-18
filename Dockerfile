FROM conda/miniconda3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@admin.com
ENV DJANGO_SUPERUSER_PASSWORD=abc123xyz
WORKDIR /app
COPY . /app/
RUN conda env create -f environment.yaml
EXPOSE 8000
ENTRYPOINT ["/bin/bash", "-c", "conda init bash \
&& source /root/.bashrc \
&& conda activate django-product-review-app \
&& python3 src/manage.py migrate \
&& python3 src/manage.py createsuperuser --no-input \
&& python3 src/manage.py runserver 0.0.0.0:8000"]
