trigger: initial commit to activate workflow
check bot
# school_manage_backend
school_manage_backend

echo "init trigger" >> trigger.txt
git add .
git commit -m "🟢 Initial commit to activate cron schedule"
git push origin main

