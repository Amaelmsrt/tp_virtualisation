FROM php:8.1-apache
COPY index.php /var/www/html/
RUN docker-php-ext-install mysqli
RUN pecl install redis && docker-php-ext-enable redis