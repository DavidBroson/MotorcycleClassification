ggf. ergänzen sodass container instanz weiter läuft
 && tail -f /dev/null"


docker volume create ai_system

docker compose down
docker compose up -d
