rm .env
cp example.env .env
rm -rf web/static/v1.0_fake_products
mkdir web/static/v1.0_fake_products
cp -R ../v1.0_fake_products web/static/v1.0_fake_products

python3 ingest.py