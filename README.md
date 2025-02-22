# TP VIRTUALISATION

## Création du cluster swarm

```bash
docker swarm init
```

![Etat du docker](./img/docker_node.png)

## Les services

Nous avons besoin de créer les images pour les services à faire.

### Site web de **Reprise Contact**

On commence par déployer l'image :

```bash
docker build -t utilisateurs_web_image:latest ./services/utilisateurs/
```

Ensuite, on crée le réseau traefik public :

```bash
docker network create --driver overlay traefik-public
```

Et on crée le service :

```bash
docker network create --driver overlay web-utilisateurs
```

Après cela, on peut déployer le service :

```bash
docker stack deploy -c docker-compose.yml traefik
```

Nous en faisons alors un curl ensuite pour vérifier que le service est bien en place :

![Curl du service utilisateurs](./img/curl_utilisateurs.png)

### Site web de **Cluster avec Swarm**

On commence par déployer l'image :

```bash
docker build -t clusterswarm_web_image:latest ./services/clusterswarm/
```

On crée le service :

```bash
docker network create --driver overlay web-clusterswarm
```

Et on déploie le service à nouveau.

Voici le curl pour vérifier que le service est bien en place :

![Curl du service clusterswarm](./img/curl_clusterswarm.png)

### Application **Fortune Image**

On commence par déployer l'image :

```bash
docker build -t fortune_web_image:latest ./services/fortune/
```

On crée le service :

```bash
docker network create --driver overlay web-fortuneapp
```

Et on déploie le service à nouveau.

Voici le curl pour vérifier que le service est bien en place :

![Curl du service fortuneapp](./img/curl_fortune.png)

### Recherche perso

On commence par déployer l'image :

```bash
docker build -t apache_web_image:latest ./services/apache/
```

On crée le service :

```bash
docker network create --driver overlay web-apache
```

Et on déploie le service à nouveau.

Voici le curl pour vérifier que le service est bien en place :

![Curl du service apache](./img/curl_apache.png)