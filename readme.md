pip3 freeze > requirements.txt
pip3 install -r requirements.txt -v

fastapi dev app/main.py

SELECT p.id, p.barcode, p.title product, c.title category, b.title brand FROM product p
    LEFT JOIN category c ON c.id = p.category_id
    LEFT JOIN brand b ON b.id = p.brand_id;
