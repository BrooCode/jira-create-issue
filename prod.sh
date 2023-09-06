#!/home/ubuntu/
cd jira

docker stop app1
echo "y" |docker system prune -a
docker build -t app1 .
docker run -d -p 5050:5050 --name app1 app1
