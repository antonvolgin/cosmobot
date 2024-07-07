INSERT INTO brand
(title, description, url, logo)
VALUES 
('PROКУДРИ', 'Описание PROКУДРИ', 'url PROКУДРИ', 'logo PROКУДРИ'),
('BEAUTIFIC', 'Описание BEAUTIFIC', 'url BEAUTIFIC', 'logo BEAUTIFIC'),
('KERAPROOF', 'Описание KERAPROOF', 'url KERAPROOF', 'logo KERAPROOF')
;

INSERT INTO category
(title, title_en, description)
VALUES
('стайлинг', 'stayling', 'Описание Стайлинг'),
('шампунь', 'shampoo', 'Описание Шампунь'),
('бальзам', 'balzam', 'Описание Бальзам'),
('укладка', 'piling', 'Описание Укладка')
;

INSERT INTO product
(barcode, TITLE, URL, components, description, brand_id, category_id)
VALUES
(111, 'CURL ME ON Гель-кастард для кудрявых и волнистых волос', 'u1', 'AQUA, COCO-CAPRYLATE CAPRATE, CETEARYL ALCOHOL, GLYCERIN, BEHENTRIMONIUM METHOSULFATE, GLYCINE SOJA (SOYBEAN) OIL, PERSEA GRATISSIMA (AVOCADO) OIL, CAPRYLIC/CAPRIC TRIGLYCERIDE, ARGANIA SPINOSA (ARGAN) KERNEL OIL, PANHTENOL, HYDROLYZED SILK, LINUM USITATISSIMUM SEED EXTRACT, HYDROLYZED KERATIN, TOCOPHEROL, HELIANTHUS ANNUSS (SUNFLOWER) SEED OIL, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, ARGININE,  PHENOXYETHANOl, TETRASODIUM GLUTAMATE DIACETATE, ETHYLHEXYLGLYCERIN, SODIUM BENZOATE, POTASSIUM SORBATE, SODIUM HYDROXIDE, PARFUM, BUTYLPHENYL METHYLPROPIONAL, HEXYL CINNAMAL, LINALOOL, CITRONELLOL, GERANIOL, LIMONENE.', 'Мягкий шампунь, основанный на бетаине. Подходит для частого применения. За счет отсутствия сульфатов, шампунь не сушит длину волос. Шампунь обладает приятным освежающим ароматом грейпфрута и зеленого чая. Наша рекомендация- комбинированное мытье. Чередовать шампунь PROКудри с сульфатным шампунем, это обеспечит лучшее очищение кожи головы.', 1, 1),
(222, 'Шампунь для кудрявых и волнистых волос', 'u2', 'AQUA (WATER), VP/VA COPOLYMER, XANTHAN GUM, GLYCERIN, ALOE BARBADENSIS (ALOE VERA) LEAF JUICE, QUERCUS ALBA BARK EXTRACT, POLYSORBATE-20, PEG-40 HYDROGENATED CASTOR OIL, HUMULUS LUPULUS (HOPS) EXTRACT, HYDROLYZED SILK, LINUM USITATISSIMUM (LINSEED) SEED EXTRACT, COCO-CAPRYLATE/ CAPRATE, PECTIN, ZEA MAYS (CORN) STARCH, MALTODEXTRIN, PANTHENOL, CITRIC ACID, TETRASODIUM GLUTAMATE DIACETATE, SODIUM HYDROXIDE, PHENOXYETHANOL, ETHYLHEXYLGLYCERIN, POTASSIUM SORBATE, SODIUM BENZOATE, PARFUM, BUTYLPHENYL METHYLPROPIONAL, CITRONELLOL, GERANIOL, HEXYL CINNAMAL, LIMONENE, LINALOOL.', 'Шампунь очищающий с маслом чайного дерева и ментолом подходит для всех типов волос. Благодаря мягкому sodium coco-sulfate, не пересушивая, тщательно вымывает загрязнения с кожи головы и волос. В свою очередь, масло чайного дерева регулирует выработку кожного сала. Обладает антисептическим и противогрибковым свойством, что позволяет нормализовать баланс жирности кожи головы. Добавленный в шампунь экстракт алоэ имеет увлажняющее действие, сохраняет влагу в волосах, а аромат мяты продлевает чувство свежести на весь день.', 2, 2),
(333, 'Бальзам для кудрявых и волнистых волос', 'u3', 'AQUA, COCAMIDOPROPYL BETAINE, SODIUM LAUROYL METHYL ISETHIONATE, DECYL GLUCOSIDE, GLYCERIN, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, NIACINAMIDE, PANTHENOL, HYDROLYZED KERATIN, GLUCOSE, SORBITOL, SODIUM GLUTAMATE, UREA, SODIUM PCA, GLYCINE, LACTIC ACID, HYDROLYZED WHEAT PROTEIN, SIMMONDSIA CHINENSIS (JOJOBA) SEED OIL, PERSEA GRATISSIMA (AVOCADO) OIL, POLYQUATERNIUM-10, POLYQUATERNIUM-7, CITRIC ACID, SODIUM HYDROXIDE, TETRASODIUM GLUTAMATE DIACETATE, COCAMIDOPROPYL DIMETHYLAMINE, SODIUM BENZOATE, METHYLCHLOROISOTHIAZOLINONE, METHYLISOTHIAZOLINONE, PARFUM, ALPHA-ISOMETHYL IONONE, LIMONÈNE, BENZYLE SALICYLATE, HYDROXYCITRONELLAL, CITRONNELLOL, HEXYL CINNAMAL, LINALOOL.', 'Натуральный кондиционер, в котором не последнюю роль играют: кокосовое масло, масло ши, масло грейпфрута, протеины, алоэ, пантенол, аскорбиновая кислота, экстракты женьшеня и ламинарии. Благодаря этим компонентам кондиционер прекрасно увлажняет волосы, запечатывает кутикулу, придает упругость завиткам. Обладает освежающим ароматом грейпфрута и зеленого чая.', 3, 3),
(444, 'Спрей-сыворотка несмываемый для кудрявых и волнистых волос', 'u4', 'AQUA, CETEARYL ALCOHOL, GLYCERIN, DIPALMITOYLETHYL HYDROXYETHYLMONIUM METHOSULFATE, ALOE BARBADENSIS LEAF JUIСE, CETRIMONIUM CHLORIDE, СOCOS NUCIFERA (COCONUT) OIL, VITIS VINIFERA (GRAPE) SEED OIL, PANTHENOL, BUTYROSPERMUM PARKII (SHEA) BUTTER, HYDROLYZED KERATIN, POLYQUATERNIUM-37, GUAR HYDROXYPROPYLTRIMONIUM CHLORIDE, CETEARETH-20, CITRIC ACID, POTASSIUM SORBATE, SODIUM BENZOATE, PHENOXYETHANOL, ETHYLHEXYLGLYCERIN, PARFUM.', 'Натуральная маска, в которой не последнюю роль играют: кокосовое масло, масло ши, масло грейпфрута, протеины, алоэ, пантенол, аскорбиновая кислота, масло жожоба. А также гидролизированный кератин, способствующий удержанию влаги в волосах, и восстановлению их структуры.Способ применения: Нанести на чистые влажные волосы, оставить на 5-10 минут, смыть. Для усиления эффекта увлажнения и реконструкции волоса, его уплотнения, нанести маску на 30 минут и подержать волосы в тепле. Затем тщательно смыть. Так как в маске большое количество натуральных компонентов, сделайте предварительный тест на аллергию на сгибе локтя.', 3, 3)
ON CONFLICT(barcode)
    DO UPDATE SET
        title = excluded.title,
        url = excluded.url,
        components = excluded.components,
        description = excluded.description,
        brand_id = excluded.brand_id, 
        category_id = excluded.category_id
