INSERT INTO brand
(title, description, url, logo)
VALUES 
('PROКУДРИ', 'Описание PROКУДРИ', 'url PROКУДРИ', 'logo PROКУДРИ'),
('BEAUTIFIC', 'Описание BEAUTIFIC', 'url BEAUTIFIC', 'logo BEAUTIFIC'),
('KERAPROOF', 'Описание KERAPROOF', 'url KERAPROOF', 'logo KERAPROOF')
;

INSERT INTO category
(title, description)
VALUES
('Стайлинг', 'Описание Стайлинг'),
('Шампунь', 'Описание Шампунь'),
('Бальзам', 'Описание Бальзам')
;

INSERT INTO product
(barcode, TITLE, URL, components, brand_id, category_id)
VALUES
(111, 'CURL ME ON Гель-кастард для кудрявых и волнистых волос', 'u1', 'AQUA, COCO-CAPRYLATE CAPRATE, CETEARYL ALCOHOL, GLYCERIN, BEHENTRIMONIUM METHOSULFATE, GLYCINE SOJA (SOYBEAN) OIL, PERSEA GRATISSIMA (AVOCADO) OIL, CAPRYLIC/CAPRIC TRIGLYCERIDE, ARGANIA SPINOSA (ARGAN) KERNEL OIL, PANHTENOL, HYDROLYZED SILK, LINUM USITATISSIMUM SEED EXTRACT, HYDROLYZED KERATIN, TOCOPHEROL, HELIANTHUS ANNUSS (SUNFLOWER) SEED OIL, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, ARGININE,  PHENOXYETHANOl, TETRASODIUM GLUTAMATE DIACETATE, ETHYLHEXYLGLYCERIN, SODIUM BENZOATE, POTASSIUM SORBATE, SODIUM HYDROXIDE, PARFUM, BUTYLPHENYL METHYLPROPIONAL, HEXYL CINNAMAL, LINALOOL, CITRONELLOL, GERANIOL, LIMONENE.', 1, 1),
(222, 'Шампунь для кудрявых и волнистых волос', 'u2', 'AQUA (WATER), VP/VA COPOLYMER, XANTHAN GUM, GLYCERIN, ALOE BARBADENSIS (ALOE VERA) LEAF JUICE, QUERCUS ALBA BARK EXTRACT, POLYSORBATE-20, PEG-40 HYDROGENATED CASTOR OIL, HUMULUS LUPULUS (HOPS) EXTRACT, HYDROLYZED SILK, LINUM USITATISSIMUM (LINSEED) SEED EXTRACT, COCO-CAPRYLATE/ CAPRATE, PECTIN, ZEA MAYS (CORN) STARCH, MALTODEXTRIN, PANTHENOL, CITRIC ACID, TETRASODIUM GLUTAMATE DIACETATE, SODIUM HYDROXIDE, PHENOXYETHANOL, ETHYLHEXYLGLYCERIN, POTASSIUM SORBATE, SODIUM BENZOATE, PARFUM, BUTYLPHENYL METHYLPROPIONAL, CITRONELLOL, GERANIOL, HEXYL CINNAMAL, LIMONENE, LINALOOL.', 2, 2),
(333, 'Бальзам для кудрявых и волнистых волос', 'u3', 'AQUA, COCAMIDOPROPYL BETAINE, SODIUM LAUROYL METHYL ISETHIONATE, DECYL GLUCOSIDE, GLYCERIN, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, NIACINAMIDE, PANTHENOL, HYDROLYZED KERATIN, GLUCOSE, SORBITOL, SODIUM GLUTAMATE, UREA, SODIUM PCA, GLYCINE, LACTIC ACID, HYDROLYZED WHEAT PROTEIN, SIMMONDSIA CHINENSIS (JOJOBA) SEED OIL, PERSEA GRATISSIMA (AVOCADO) OIL, POLYQUATERNIUM-10, POLYQUATERNIUM-7, CITRIC ACID, SODIUM HYDROXIDE, TETRASODIUM GLUTAMATE DIACETATE, COCAMIDOPROPYL DIMETHYLAMINE, SODIUM BENZOATE, METHYLCHLOROISOTHIAZOLINONE, METHYLISOTHIAZOLINONE, PARFUM, ALPHA-ISOMETHYL IONONE, LIMONÈNE, BENZYLE SALICYLATE, HYDROXYCITRONELLAL, CITRONNELLOL, HEXYL CINNAMAL, LINALOOL.', 3, 3),
(444, 'Спрей-сыворотка несмываемый для кудрявых и волнистых волос', 'u4', 'AQUA, CETEARYL ALCOHOL, GLYCERIN, DIPALMITOYLETHYL HYDROXYETHYLMONIUM METHOSULFATE, ALOE BARBADENSIS LEAF JUIСE, CETRIMONIUM CHLORIDE, СOCOS NUCIFERA (COCONUT) OIL, VITIS VINIFERA (GRAPE) SEED OIL, PANTHENOL, BUTYROSPERMUM PARKII (SHEA) BUTTER, HYDROLYZED KERATIN, POLYQUATERNIUM-37, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, CETEARETH-20, CITRIC ACID, POTASSIUM SORBATE, SODIUM BENZOATE, PHENOXYETHANOL, ETHYLHEXYLGLYCERIN, PARFUM.', 3, 3)
ON CONFLICT(barcode)
    DO UPDATE SET
        title = excluded.title,
        url = excluded.url,
        components = excluded.components, 
        brand_id = excluded.brand_id, 
        category_id = excluded.category_id

SELECT p.id, p.barcode, p.title product, c.title category, b.title brand FROM product p
    LEFT JOIN category c ON c.id = p.category_id
    LEFT JOIN brand b ON b.id = p.brand_id;
   
SELECT * FROM product p
    WHERE p.id = 1;

===============================================
/lib/systemd/system# 

api.service
bot.service 
cosmo_admin.service

===============================================
https://cosmocode.site/docs

curl -L https://cosmocode.site/apiai/categories > response_categories.json
curl -L https://cosmocode.site/apiai/products > response_products.json
curl -L https://cosmocode.site/apiai/brands > response_brands.json
curl -L https://cosmocode.site/apiai/logs > response_logs.json

curl -L --request GET \
  --url 'https://cosmocode.site/apiai/suggestions?=' \
  --header 'Content-Type: application/json' \
  --data '{
	"category":"shampoo",
	"ingredients":"Aqua, Cetearyl Alcohol, Cetrimonium Chloride"
}'

curl -L --request GET \
  --url 'https://cosmocode.site/apiai/product/111?=' \
  --header 'Content-Type: application/json''

curl -L -F "file=@brand_1.csv" https://cosmocode.site/apiai/upload/brands > response_brands.json
curl -L -F "file=@product_1.csv" https://cosmocode.site/apiai/upload/products > response_products.json

===============================================
