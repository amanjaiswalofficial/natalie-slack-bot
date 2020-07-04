# shell script to push news everyday

last_updated_date=$(date +%s)
today_date=$(date +%s)

# check if last_updated file exist, meaning this was called before
if [ -e last_updated ]
then
  last_updated_date=$(cat last_updated.txt)
fi

date_diff_in_days=$(( (today_date-last_updated_date)/86400 ))

# if the difference is at least 1 day or more,
if [ $date_diff_in_days -ge 1 ]
then
  # execute python script to push news
  source venv/bin/activate
  python3 update_news_channels.py
fi

# if the script executed successfully, update the last_updated.txt file
if [ $? -eq 0 ]
then
  echo "${today_date}" > last_updated.txt
fi
