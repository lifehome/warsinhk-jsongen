mkdir -p data/

echo "Downloading..."
python3 ./transformers/alerts.py
python3 ./transformers/case-history.py
python3 ./transformers/case-location.py
python3 ./transformers/case-relationship.py
python3 ./transformers/disruptions-master.py
python3 ./transformers/disruptions-description.py
python3 ./transformers/important-information.py
python3 ./transformers/travel-alert.py
python3 ./transformers/latest-figures.py
python3 ./transformers/dubious-shop.py
python3 ./transformers/hygiene-tips.py
python3 ./transformers/friendly-links.py
python3 ./transformers/site-i18n.py
echo "Download script exiting... code: " $?