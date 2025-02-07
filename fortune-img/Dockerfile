FROM php:7.4-apache

RUN apt update && \
    apt install -y --no-install-recommends fortune imagemagick && \
    rm -rf /var/lib/apt/lists/*

COPY index.php /var/www/html/
COPY images /var/www/html/images
COPY convert.sh /root/convert.sh

RUN chmod +x /root/convert.sh && /root/convert.sh

EXPOSE 80
