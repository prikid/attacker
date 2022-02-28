#bash
count=$1
if [ -z "$count" ]; then
  count=10
fi
docker-compose up --build -d --scale app=$count
