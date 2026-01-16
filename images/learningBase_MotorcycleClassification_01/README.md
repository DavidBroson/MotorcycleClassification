docker compose up -d --build

prüfen ob Dateien existieren:

docker run --rm -v ai_system:/tmp busybox sh -c "find /tmp -maxdepth 6 -type f -print | sort"