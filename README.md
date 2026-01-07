# python-fastapi-test-api

Servicio backend de ejemplo para **punk-records**, construido con **Python + FastAPI**.

Este proyecto funciona como **plantilla de referencia** para servicios backend:
- deployables con Docker
- integrables en Caddy
- actualizables automáticamente vía cron (pull-based)

---

## 🎯 Objetivo

- Proveer un backend HTTP simple
- Exponer un endpoint `/health`
- Servir como **modelo de estructura ideal** para futuros servicios Python

---

## 🧱 Estructura del proyecto

```
python-fastapi-test-api/
├── app/
│   └── main.py          # aplicación FastAPI
├── docker/
│   └── Dockerfile       # imagen del servicio
├── requirements.txt     # dependencias Python
├── deploy.sh            # levantar/recrear container (server)
├── update.sh            # git pull + build + deploy (server)
├── cron.log             # logs de cron (no versionado)
├── .gitignore
└── README.md
```

---

## 🚀 Endpoints

### Health check

```
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok",
  "service": "python-fastapi-test-api"
}
```

---

## 🐳 Docker

### Build local (opcional)

```bash
docker build -t python-fastapi-test-api:local -f docker/Dockerfile .
```

### Run local (opcional)

```bash
docker run --rm -p 8000:8000 python-fastapi-test-api:local
```

```bash
curl http://127.0.0.1:8000/health
```

---

## 🧠 Integración con punk-records

Este servicio está pensado para integrarse en:

```
/srv/punk-records/services/python-fastapi-test-api
```

### docker-compose

Agregar en `/srv/punk-records/infra/docker-compose.yml`:

```yaml
python-fastapi-test-api:
  build:
    context: /srv/punk-records/services/python-fastapi-test-api
    dockerfile: docker/Dockerfile
  container_name: python-fastapi-test-api
  restart: unless-stopped
  networks:
    - punk-net
```

---

### Caddy

Agregar en `/srv/punk-records/infra/caddy/Caddyfile`:

```caddy
handle_path /api/python/* {
    reverse_proxy python-fastapi-test-api:8000
}
```

---

## 🔁 CI/CD local-first

El server ejecuta periódicamente:

```bash
./update.sh
```

Este script:
- detecta cambios en GitHub
- hace `git pull`
- rebuilda la imagen
- redeploya el servicio

Sin:
- webhooks
- GitHub Actions
- IP pública

---

## 📌 Principios del proyecto

- un repo = un proceso deployable
- Caddy es la única puerta de entrada
- los containers se comunican por nombre de servicio
- el server **pull**, nunca recibe pushes

---

## 🧪 Estado

- ✔️ funcional
- ✔️ reproducible
- ✔️ documentado
- ✔️ alineado con punk-records
