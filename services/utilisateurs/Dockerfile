FROM php:7.4-apache

# Mise à jour et installation des outils nécessaires
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libonig-dev \
    libzip-dev \
    unzip \
    && docker-php-ext-install mysqli

# Installation de Redis si non installé
RUN pecl install redis && docker-php-ext-enable redis

# Copier le fichier index.php dans le dossier web
COPY index.php /var/www/html/

# Exposer le port 80 pour Apache
EXPOSE 80
