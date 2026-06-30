# CEO — Rules & Policies

## CEO rules

Client will provide this information.

## Escalation rules

Client will provide this information.

## Risk policy

Client will provide this information.

## Decision policy

Client will provide this information.

## Reporting policy

Client will provide this information.

## Updates log

<!-- Append dated policy updates below -->

## Imported Company Knowledge


## Hujjatlashtirish boshqaruvi

**Source:** `HBA-06_Hujjatlashtirish_arxitekturasi_v1.0.docx`

HARIDLAR.UZ BUSINESS ARCHITECTURE
VI-QATLAM
HUJJATLASHTIRISH ARXITEKTURASI
(Document Management Architecture)
Hujjat kodi: HBA-06
Versiya: 1.0
Sana: 26.06.2026
Mualliflar: NEXT ONE
Shohruhmirzo
Asomiddin
1. Qatlam maqsadi
Savdo va ta'minot jarayonlaridagi barcha hujjatlarni qonunchilik talablariga muvofiq, to'g'ri, o'z vaqtida va izchil rasmiylashtirish hamda hujjatlar aylanishini boshqarish.
2. Ta'rif
Hujjatlashtirish arxitekturasi — shartnoma, ishonchnoma, hisob-faktura, elektron hujjatlar (DIDOX) va arxivni boshqarishga oid funksiyalar majmuasi.
3. Haridlar.uz uchun ahamiyati
Hujjatlar biznesning huquqiy asosidir.
Noto'g'ri hujjat mijoz ishonchi va to'lovni xavf ostiga qo'yadi.
Qonuniylik va auditga tayyorgarlik aynan shu qatlam orqali ta'minlanadi.
LPR uchun xavfsizlik hissini yaratadigan asosiy qatlamlardan biridir.
4. Qatlam arxitekturasi
Shartnomani tayyorlash
Shartnomani tekshirish
Ishonchnomani qabul qilish
Hisob-faktura yaratish
DIDOX orqali yuborish
Elektron tasdiqlarni nazorat qilish
Hujjatlarni arxivlash
Hujjatlar monitoringi
5. Yig'ilgan ma'lumotlar
Shakllangan shartnoma buxgalteriyaga topshiriladi.
Ishonchnoma asosida hisob-faktura yaratiladi.
Hisob-faktura DIDOX orqali mijozga yuboriladi.
Sotuv bo'limi hujjatlar qabul qilinishini nazorat qiladi.
Hujjatdagi xatolar asosiy operatsion risklardan biri sifatida qayd etilgan.
6. Funksiyalar daraxti
Hujjatlashtirish
├─ Shartnoma
├─ Ishonchnoma
├─ Hisob-faktura
├─ DIDOX
├─ Elektron tasdiq
├─ Arxiv
└─ Monitoring
7. Input
Ta'minotdan topshirish ma'lumotlari
Savdo shartlari
Ishonchnoma
Mijoz rekvizitlari
8. Output
Rasmiy shartnoma
Hisob-faktura
DIDOX hujjati
Arxivlangan hujjatlar
To'lov uchun asos
9. Asosiy natijalar
Hujjatlar xatosiz rasmiylashtiriladi
To'lov jarayoni tezlashadi
Auditga tayyor hujjatlar bazasi yaratiladi
10. KPI
Hujjatlar xatolik darajasi
Hisob-faktura tayyorlash vaqti
DIDOX orqali qabul qilish foizi
Arxivlangan hujjatlar ulushi
11. Asosiy risklar
Shartnomadagi xatolar
Hisob-faktura xatolari
DIDOX kechikishi
Hujjat yo'qolishi
Qonunchilik talablariga mos kelmaslik
12. Atamalar izohi
Shartnoma: Tomonlarning huquq va majburiyatlarini belgilovchi rasmiy hujjat.
Hisob-faktura: Tovar yoki xizmat uchun to'lov asosini tasdiqlovchi hujjat.
Ishonchnoma: Mahsulotni qabul qilish vakolatini beruvchi hujjat.
DIDOX: Elektron hujjat almashish tizimi.
Arxiv: Hujjatlarni tizimli saqlash va qidirish muhiti.
13. Business Rules
Har bir savdo rasmiy shartnoma bilan tasdiqlanadi.
Hisob-faktura faqat tasdiqlangan ma'lumotlar asosida yaratiladi.
DIDOX orqali yuborish majburiy.
Barcha hujjatlar arxivlanadi.
14. Qatlamlar bilan bog'liqlik
Input: 5-qatlam (Ta'minot va logistika).
Output: 7-qatlam (Moliya) hamda 8-qatlam (Mijozlarga xizmat).
15. NEXT ONE izohi
Hujjatlashtirish kompaniyaning ishonchliligini huquqiy jihatdan mustahkamlaydi. Jarayon standartlashganda inson omili va operatsion risklar kamayadi.
16. Xulosa
Hujjatlar sifati kompaniya obro'sining bir qismidir.
Har bir hujjat standart asosida yaratilishi kerak.
Elektron hujjatlar aylanishi nazorat qilinishi zarur.
Hujjatlar bazasi korporativ aktiv hisoblanadi.
Ushbu qatlam moliyaviy oqimning huquqiy asosini yaratadi.


## Boshqaruv va qaror qabul qilish

**Source:** `HBA-09_Boshqaruv_arxitekturasi_v1.0.docx`

HARIDLAR.UZ BUSINESS ARCHITECTURE
IX-QATLAM
BOSHQARUV ARXITEKTURASI
(Management Architecture)
Hujjat kodi: HBA-09
Versiya: 1.0
Sana: 26.06.2026
Mualliflar: NEXT ONE
Shohruhmirzo
Asomiddin
1. Qatlam maqsadi
Haridlar.uz biznesining barcha funksional qatlamlarini yagona tizim sifatida boshqarish, resurslarni muvofiqlashtirish, qarorlar qabul qilish, nazorat qilish va doimiy takomillashtirishni ta'minlash.
2. Ta'rif
Boshqaruv arxitekturasi — strategik, taktik va operatsion boshqaruvni, hisobotlarni, KPI tizimini, monitoringni, tahlilni va uzluksiz rivojlanishni boshqaruvchi markaziy qatlam.
3. Haridlar.uz uchun ahamiyati
Murad akaga operatsion bog'liqlikni kamaytiruvchi asosiy qatlam.
8 ta funksional qatlamni yagona tizimga birlashtiradi.
Resurslar, manfaatlar va risklar muvozanatini boshqaradi.
Biznesni masshtablash va delegatsiya qilish uchun asos yaratadi.
4. Qatlam arxitekturasi
Strategik boshqaruv
Operatsion boshqaruv
KPI boshqaruvi
Hisobotlar
Monitoring
Qaror qabul qilish
Risklarni boshqarish
Resurslarni taqsimlash
Takomillashtirish
Delegatsiya
Ichki audit
5. Yig'ilgan ma'lumotlar
Asosiy KPI: sof foyda, aylanma, yangi buyurtmalar, aktiv mijozlar, yutilgan tenderlar, pul oqimi.
Murad aka 200 mln so'mdan yuqori buyurtmalar va strategik qarorlarni nazorat qiladi.
Dilshod operatsion va taktik boshqaruvni olib boradi.
Asosiy know-how — ishonchga asoslangan insoniy munosabatlar.
Biznes qiymati resurslarni tez va to'g'ri muvofiqlashtirish orqali yaratiladi.
6. Funksiyalar daraxti
Boshqaruv
├─ Strategik boshqaruv
├─ Operatsion boshqaruv
├─ KPI
├─ Hisobotlar
├─ Monitoring
├─ Qarorlar
├─ Risklar
├─ Resurslar
├─ Delegatsiya
├─ Audit
└─ Takomillashtirish
7. Input
1–8 qatlamlardan hisobotlar
KPI natijalari
Pul oqimi
Mijoz feedbacklari
Risklar to'g'risidagi ma'lumotlar
8. Output
Strategik qarorlar
Operatsion topshiriqlar
Resurs taqsimoti
Yaxshilash rejalari
Delegatsiya qarorlari
9. Asosiy natijalar
Barqaror boshqaruv tizimi
Murad akaga bog'liqlik kamayadi
Qarorlar sifati oshadi
Biznes masshtablashga tayyor bo'ladi
10. KPI
Sof foyda
Aylanma
Pul oqimi
Yangi buyurtmalar
Faol mijozlar
Yutilgan tenderlar
Delegatsiya darajasi
Qaror bajarilish foizi
11. Asosiy risklar
Qarorlarning markazlashib qolishi
Nazoratning sustligi
Hisobotlarning ishonchsizligi
Resurslar noto'g'ri taqsimlanishi
Asosiy xodimlarga haddan tashqari bog'liqlik
12. Atamalar izohi
KPI: Asosiy samaradorlik ko'rsatkichi.
Monitoring: Jarayonlarni muntazam kuzatish va baholash.
Delegatsiya: Vakolat va mas'uliyatni topshirish.
Audit: Jarayonlarni mustaqil tekshirish va baholash.
Operatsion boshqaruv: Kundalik faoliyatni boshqarish.
13. Business Rules
Har bir qaror ma'lumotlarga asoslanishi kerak.
KPI va hisobotlar muntazam ko'rib chiqiladi.
Strategik va operatsion qarorlar ajratiladi.
Takomillashtirish sikli doimiy ishlaydi.
14. Qatlamlar bilan bog'liqlik
Input: 1–8 qatlamlarning barchasi.
Output: Barcha qatlamlarga boshqaruv qarorlari va takomillashtirish topshiriqlari.
15. NEXT ONE izohi
Boshqaruv qatlami Haridlar.uzning 'miyasi' hisoblanadi. U alohida bo'limni emas, balki barcha oqimlarni boshqaradi. Asosiy vazifasi sakkizta asosiy oqimni muvofiqlashtirishdir: manfaatlar, odamlar, vaqt, axborot, pul oqimi, tovar harakati, hujjatlar va risklar.
16. Xulosa
Boshqaruv barcha qatlamlarni yagona tizimga birlashtiradi.
Qarorlar standartlashtirilsa biznes masshtablanadi.
Murad akaning bilimlari tizimga ko'chirilishi kerak.
Delegatsiya boshqaruvning ajralmas qismi.
Ushbu qatlam Haridlar.uzning operatsion mustaqilligini ta'minlaydi.


## CEO boshqaruv jarayonlari

**Source:** `П9 Фақат Мурод ака учун! V3.docx`

ХАРИДЛАР.УЗ БИЗНЕС АРХИТЕКТУРАСИ
9-БИЗНЕС ЖАРАЁНИ
КОРПОРАТИВ БОШҚАРУВ, СТРАТЕГИК РИВОЖЛАНТИРИШ ВА БИЗНЕС ТРАНСФОРМАЦИЯСИ
Ҳужжат тури: Бизнес жараёни (Business Process)
Жараён рақами: BP-09
Версия: 3.0 (BP-06, BP-07 ва BP-08 таҳрирларидан кейин қайта ишланган)
1. Жараённинг мақсади
Харидлар.уз компаниясининг миссияси, стратегик мақсадлари ва бизнес моделига мувофиқ барча бизнес жараёнларини мувофиқлаштириш, стратегик қарорларни қабул қилиш, ривожланиш дастурларини бошқариш, инновацияларни жорий этиш ва компаниянинг узоқ муддатли рақобатбардошлигини таъминлаш.
Ушбу жараённинг асосий вазифаси:
Компаниянинг келажагини бошқариш.
BP-09 барча бошқа бизнес жараёнларининг ривожланиш йўналишини белгилайди.
2. Жараённинг бизнесдаги ўрни
BP-09 Харидлар.уз компаниясининг энг юқори даражадаги бошқарув жараёни ҳисобланади.
Барча жараёнлар:
BP-01 → BP-08
ушбу жараён учун маълумот ишлаб чиқаради.
BP-09 эса ушбу маълумотлар асосида:
стратегияни янгилайди;
бизнес моделини ўзгартиради;
инвестиция қарорларини қабул қилади;
янги хизматларни ишлаб чиқади;
компания архитектурасини ривожлантиради.
Бу жараён компаниянинг "Бош мияси" вазифасини бажаради.
3. Жараённинг асосий натижаси (Output)
Жараён якунида:
✓ Стратегия янгиланган.
✓ Бизнес модели қайта кўриб чиқилган.
✓ Янги стратегик ташаббуслар тасдиқланган.
✓ Лойиҳалар портфели шакллантирилган.
✓ KPI тизими қайта кўриб чиқилган.
✓ Барча бизнес жараёнлари учун яхшилаш топшириқлари берилган.
✓ Кейинги чорак учун ривожланиш режаси тасдиқланган.
4. Жараённинг кириш маълумотлари (Input)
BP-08 дан қабул қилинади
Савдо
Лидлар
Конверсия
Даромад
Электрон савдо
Ғолиблик коэффициенти
Йўқотилган тендерлар
Таъминот
OTIF
Таъминловчилар рейтинги
Таъминловчиларга тўлов интизоми
Молия
Cash Flow
Дебитор қарздорлик
Кредитор қарздорлик
DSO
EBITDA
Рентабеллик
Customer Success
CSAT
NPS
Customer Lifetime Value
Repeat Purchase
Retention Rate
Рефераллар
Компания
Барча KPI
Dashboard
Аналитик ҳисоботлар
Ташқи маълумотлар
Бозор таҳлили
Қонунчилик ўзгаришлари
Давлат харидлари сиёсати
Рақобатчилар
Янги технологиялар
AI имкониятлари
5. Жараён иштирокчилари
Асосий иштирокчилар
Таъсисчи
Бош директор
Стратегик кенгаш
Бизнес аналитикаси раҳбари
Молия директори
Савдо директори
Барча бўлим раҳбарлари
6. Жараён эгаси (Process Owner)
Лавозим:
Компания таъсисчиси.
У қуйидагилар учун шахсан жавоб беради:
миссия;
стратегия;
бизнес модели;
инвестициялар;
корпоратив бошқарув;
трансформация.
7. Жараённинг кетма-кетлиги
1-босқич. Стратегик маълумотларни қабул қилиш
BP-08 дан келган барча ҳисоботлар қабул қилинади.
Текширилади:
KPI
Dashboard
Cash Flow
Customer Success
Supplier Performance
2-босқич. Strategic Review (Стратегик таҳлил)
Қуйидаги 10 та йўналиш таҳлил қилинади.
1.
Business Model Review
Бизнес модели ҳали ҳам бозорга мосми?
2.
Market Review
Янги бозорлар.
Янги имкониятлар.
3.
Customer Review
Қайси мижозлар ўсмоқда?
Қайси сегментдан чиқиш керак?
4.
Supplier Review
Қайси таъминловчилар қолади?
Қайсилари алмаштирилади?
5.
Financial Review
Cash Flow
Фойда
Маржа
Инвестиция
6.
Process Review
BP-01 дан BP-08 гача
қайси процессларда ўзгариш керак?
7.
Organization Review
Ташкилий структура.
Раҳбарлар.
KPI.
8.
Technology Review
CRM
ERP
AI
Автоматлаштириш.
9.
Risk Review
Стратегик хавфлар.
Молиявий хавфлар.
Юридик хавфлар.
Операцион хавфлар.
10.
Innovation Review
Қайси янги хизматлар ишлаб чиқилади?
Қайси янги бизнес моделлар синовдан ўтади?
3-босқич. Илдиз сабабларни таҳлил қилиш
Муаммолар
5 Why
Fishbone
Pareto
каби таҳлил усуллари билан ўрганилади.
4-босқич. Стратегик қарорлар қабул қилиш
Қарорлар қабул қилинади.
Масалан:
янги бозорга чиқиш;
янги маҳсулот;
янги хизмат;
янги ҳамкор;
янги таъминловчи;
инвестиция;
автоматлаштириш.
5-босқич. Лойиҳалар портфелини шакллантириш
Барча стратегик ташаббуслар
устуворлик бўйича
сараланади.
Ҳар бири учун:
бюджет;
масъул;
KPI;
муддат.
6-босқич. Бизнес архитектурасини янгилаш
Зарур ҳолларда
қайта кўриб чиқилади:
Бизнес модели
BP-01 ... BP-08
KPI
Ташкилий структура
SOP
Автоматлаштириш
7-босқич. Стратегик лойиҳаларни ишга тушириш
Ҳар бир лойиҳа учун:
раҳбар;
бюджет;
ресурс;
календар;
бириктирилади.
8-босқич. Ижрони мониторинг қилиш
Ҳар ой
лойиҳалар ҳолати
кўриб чиқилади.
9-босқич. Чораклик стратегик йиғилиш
Қайта баҳоланади:
KPI
Cash Flow
Customer Success
Supplier Performance
Strategy
10-босқич. Янги қарорларни BP-01 — BP-08 жараёнларига узатиш
Шу орқали
бутун компания
бир вақтда
янгиланади.
8. Қарор қабул қилиш нуқталари (Decision Points)
DP-01
Бизнес модели ҳали ҳам рақобатбардошми?
Ҳа →
Давом этилади.
Йўқ →
Қайта қурилади.
DP-02
Cash Flow барқарорми?
Ҳа →
Инвестиция мумкин.
Йўқ →
Пул оқимига устуворлик берилади.
DP-03
Стратегик таъминловчилар сақланадими?
Ҳа →
Ҳамкорлик давом этади.
Йўқ →
Янги таъминловчилар қидирилади.
DP-04
Customer Lifetime Value ўсмоқдами?
Ҳа →
Мавжуд стратегия давом этади.
Йўқ →
Customer Success қайта қурилади.
DP-05
Янги лойиҳа инвестиция қилишга арзийдими?
Ҳа →
Лойиҳа очилади.
Йўқ →
Бекор қилинади.
9. Стратегик KPI
Бизнес ўсиши
Даромад
Соф фойда
EBITDA
Молия
Cash Flow
Дебитор қарздорлик
Кредитор қарздорлик
Мижоз
Retention
CLV
NPS
Таъминот
Supplier Rating
Supplier Payment Performance
Жараёнлар
BP самарадорлиги
Автоматлаштириш даражаси
Инновация
Янги хизматлар
Янги маҳсулотлар
Янги бизнес моделлар
10. Management Policies (Бошқарув сиёсатлари)
Компанияда қуйидаги бошқарув принциплари амал қилади:
Барча стратегик қарорлар маълумотлар асосида қабул қилинади.
Cash Flow барқарорлиги фойдадан устун бошқарув кўрсаткичи ҳисобланади.
Таъминловчилар билан ҳисоб-китоб интизоми компания репутациясининг бир қисми ҳисобланади.
Мижозни сақлаб қолиш янги мижоз жалб қилишдан устувор вазифа ҳисобланади.
Ҳар бир бизнес жараёни ҳар чоракда қайта кўриб чиқилади.
Автоматлаштириш инсон меҳнатини алмаштириш учун эмас, қарор қабул қилиш сифатини ошириш учун жорий қилинади.
11. Рисклар реестри (Risk Register)
Асосий стратегик хавфлар:
Давлат харидлари қонунчилигидаги ўзгаришлар.
Йирик таъминловчининг йўқолиши.
Cash Flow инқирози.
Стратегик мижозларни йўқотиш.
Технологик орқада қолиш.
Бизнес моделининг эскириши.
Бозор рақобатининг кучайиши.
Ҳар бир хавф учун:
эҳтимол даражаси;
таъсир даражаси;
масъул шахс;
қарши чоралар режаси;
алоҳида юритилади.
12. Автоматлаштириш талаблари
BP-09 қуйидаги тизимлар билан интеграция қилиниши керак:
CRM
ERP
BI Dashboard
Молиявий ҳисоб тизими
Лойиҳаларни бошқариш тизими
KPI Monitoring System
AI Analytics
13. NEXT ONE эксперт хулосаси
Бу таҳрирдан кейин BP-09 энди оддий "ривожлантириш жараёни" эмас.
У Харидлар.уз компаниясининг ҳақиқий **Корпоратив Бошқарув Тизими (Corporate Governance System)**га айланди.
Бу жараённинг энг муҳим вазифаси — компаниянинг бугунги фаолиятини эмас, балки эртанги рақобатбардошлигини таъминлашдир.
NEXT ONEнинг якуний стратегик тавсияси
Ҳозир BP-01 дан BP-09 гача бўлган жараёнлар тайёр. Энди уларни бошқариш учун "Корпоратив бошқарув тақвими" (Corporate Governance Calendar) ишлаб чиқишни тавсия қиламан.
Масалан:
Ҳар куни — CEO Dashboard кўриб чиқилади.
Ҳар ҳафта — Операцион йиғилиш (BP-01–BP-07 натижалари).
Ҳар ой — KPI ва Cash Flow йиғилиши (BP-08).
Ҳар чорак — Strategic Review (BP-09).
Ҳар ярим йилда — Бизнес модели ва ташкилий архитектура қайта баҳоланади.
Ҳар йили — Миссия, стратегия ва 3–5 йиллик ривожланиш режаси қайта кўриб чиқилади.
Бу тақвим BP-09 ни "ҳужжат"дан "амалда ишлайдиган корпоратив бошқарув тизими"га айлантиради.
NEXT ONEнинг умумий хулосаси
BP-01 дан BP-09 гача бўлган ҳужжатлар энди фақат бизнес жараёнлари эмас. Улар Харидлар.узнинг операцион тизими, бошқарув тизими ва ривожланиш тизимининг яхлит архитектурасини ташкил қилади.
Менинг фикримча, энди кейинги босқич сифатида жараёнлардан келиб чиққан ҳолда:
Ташкилий тузилма (Organizational Structure);
RACI матрицаси (ваколатлар тақсимоти);
Лавозим йўриқномалари;
SOP (Стандарт иш тартиблари);
CRM/ERP техник топшириқлари
ишлаб чиқилса, Харидлар.уз учун тўлиқ институционал бошқарув тизими шаклланади.
