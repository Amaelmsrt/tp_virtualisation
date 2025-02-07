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