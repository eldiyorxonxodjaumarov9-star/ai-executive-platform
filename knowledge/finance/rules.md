# Finance — Rules & Policies

## Approval limits

Client will provide this information.

## Payment policy

Client will provide this information.

## Expense policy

Client will provide this information.

## Reporting policy

Client will provide this information.

## Compliance rules

Client will provide this information.

## Updates log

<!-- Append dated policy updates below -->

## Imported Company Knowledge


## Hujjatlashtirish arxitekturasi

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


## Moliya direksiyasi qoidalari

**Source:** `DP-03_Moliya_Direksiyasi_Pasporti.docx`

DP-03
MOLIYA DIREKSIYASI PASPORTI
Kompaniya: Xaridlar.uz
Versiya: 1.0
Hujjat kodi: DP-03
1. Hujjat maqsadi
Moliya direksiyasining vazifalari, javobgarligi, KPIlari, moliyaviy nazorat va hisobot standartlarini belgilash.
2. Missiya
Kompaniyaning moliyaviy barqarorligini ta'minlash, pul oqimini boshqarish, hisob-kitoblarni o'z vaqtida yuritish va moliyaviy intizomni saqlash.
3. Process Owner javobgarligi
Buxgalteriya bo'limi
Majburiyatlar
Buxgalteriya hisobini yuritish
Soliq hisobotlarini tayyorlash
Moliyaviy hisobotlarni shakllantirish
Asosiy vositalar hisobini yuritish
KPI
Hisobotlar
Buxgalteriya balansi
Foyda va zarar hisoboti
Soliq hisobotlari
Debitor to'lovlar nazorati
Majburiyatlar
Debitor qarzlarni monitoring qilish
To'lov muddatlarini nazorat qilish
Qarzdorlar bilan ishlash
KPI
Hisobotlar
Debitor reestri
Qarzdorlik tahlili
G'aznachilik bo'limi
Majburiyatlar
Pul oqimini rejalashtirish
Bank operatsiyalari
Likvidlikni boshqarish
To'lov kalendarini yuritish
KPI
Hisobotlar
Cash Flow hisoboti
To'lov kalendari
Kreditor to'lovlar bo'limi
Majburiyatlar
Yetkazib beruvchilarga to'lovlar
To'lov rejasini bajarish
Kreditor qarzdorlikni nazorat qilish
KPI
Hisobotlar
Kreditor reestri
To'lovlar hisoboti
Direksiya KPI
Cash Flow
EBITDA
DSO
Kreditor qarzdorlik
Likvidlik
Budjet ijrosi
Moliyaviy hisobotlarning o'z vaqtida topshirilishi
BP | Jarayon | Owner
BP-06 | Moliyaviy hisob-kitoblar va to'lovlar | Moliya direktori
KPI | Reja/Fakt
Hisobotlar o'z vaqtida topshirilishi
Xatolar soni
Soliq intizomi
KPI | Reja/Fakt
Debitor qarzdorlik
DSO
Undirilgan qarzlar %
KPI | Reja/Fakt
Cash Flow
Likvidlik koeffitsienti
To'lovlar o'z vaqtida %
KPI | Reja/Fakt
Kreditor qarzdorlik
To'lov intizomi %
Kechikkan to'lovlar


## Moliya direktori operatsion qoidalari

**Source:** `AQ-03_1-qism_Moliya_Direktori_Amaliy_Qollanma.docx`

AQ-03
MOLIYA DIREKTORI UCHUN AMALIY QO'LLANMA
1-QISM
Kompaniya: Xaridlar.uz
Hujjat kodi: AQ-03
Versiya: 1.0
Maqomi: Ichki foydalanish uchun
1. Qo'llanmaning maqsadi
Mazkur qo'llanma Moliya direktorining kundalik boshqaruv faoliyatini yagona korporativ standart asosida tashkil etish uchun ishlab chiqilgan. Hujjat moliyaviy rejalashtirish, pul oqimini boshqarish, topshiriqlarni delegatsiya qilish, nazorat qilish, hisobotlarni qabul qilish va CEOga boshqaruv hisobotini taqdim etish tartibini belgilaydi.
2. Moliya direktorining missiyasi
Kompaniyaning moliyaviy barqarorligini ta'minlash, pul oqimini samarali boshqarish va rahbariyatni ishonchli moliyaviy ma'lumotlar bilan ta'minlash.
BP-06 jarayoniga egalik qilish.
Cash Flow boshqaruvi.
Budjet ijrosini nazorat qilish.
Debitor va kreditor qarzdorlikni boshqarish.
Moliyaviy hisobotlar sifatini ta'minlash.
CEO va aksiyadorlar uchun moliyaviy tahlillarni tayyorlash.
3. Boshqaruv tamoyillari
4. Kundalik boshqaruv sikli
5. SMART+ topshiriq standarti
Maqsad
Kutilayotgan natija
KPI
Mas'ul
Muddat
Resurs
Risk
Nazorat sanasi
Hisobot shakli
6. Moliyaviy topshiriq kartasi
Topshiriq:
Jarayon:
Mas'ul:
Boshlanish sanasi:
Tugash sanasi:
KPI:
Budjet:
Nazorat sanasi:
Hisobot shakli:
7. Direktorning kundalik chek-listi
□ Cash Flow tekshirildi
□ To'lov kalendari tasdiqlandi
□ Budjet og'ishlari tahlil qilindi
□ Debitor/Kreditor holati ko'rildi
□ Hisobotlar qabul qilindi
□ CEO hisoboti tayyorlandi
1-qism yakuni
2-qismda topshiriqlarni delegatsiya qilish, moliyaviy nazorat, to'lovlarni tasdiqlash va eskalatsiya tartibi bayon qilinadi.
Tamoyil | Mazmuni
1 | Likvidlik doimo nazorat ostida
2 | Har bir xarajat budjet bilan asoslanadi
3 | Pul oqimi foydadan ustuvor nazorat qilinadi
4 | Moliyaviy ma'lumotlar yagona manbadan olinadi
5 | Hisobotlar o'z vaqtida tayyorlanadi
6 | Har bir qaror moliyaviy ta'siri bilan baholanadi
Vaqt | Amal
08:30 | Cash Flow va bank qoldiqlarini tekshirish
09:00 | Moliya bo'limi yig'ilishi
10:00 | To'lov kalendarini tasdiqlash
14:00 | Budjet va xarajatlarni monitoring qilish
16:30 | Debitor/Kreditor tahlili
17:30 | Hisobotlarni qabul qilish
18:00 | CEO uchun moliyaviy xulosa


## Moliya direktori operatsion qoidalari

**Source:** `AQ-03_2-qism_Moliya_Direktori_Amaliy_Qollanma.docx`

AQ-03
MOLIYA DIREKTORI UCHUN AMALIY QO'LLANMA
2-QISM
Mavzu: Topshiriqlarni delegatsiya qilish, moliyaviy nazorat va to'lovlarni boshqarish
1. Delegatsiya siyosati
Moliya direktori strategik moliyaviy qarorlarni o'zida saqlaydi, operatsion vazifalarni esa bo'lim rahbarlariga va mas'ul mutaxassislarga delegatsiya qiladi.
2. To'lovlarni boshqarish algoritmi
1. To'lov talabnomasini qabul qilish
2. Hujjatlarni tekshirish
3. Budjet mavjudligini tekshirish
4. To'lov ustuvorligini aniqlash
5. Direktor tasdig'ini olish
6. Bank orqali amalga oshirish
7. 1C tizimida aks ettirish
8. To'lovni tasdiqlash
9. Hisobotga kiritish
10. Jarayonni yopish
3. Moliyaviy nazorat nuqtalari
4. Cash Flow nazorati
Kunlik pul oqimini monitoring qilish
To'lov kalendarini yuritish
Likvidlikni nazorat qilish
Reja/Fakt tahlili
Pul oqimi xavflarini baholash
5. Debitor va kreditor qarzdorlikni boshqarish
Debitor qarzdorlik muddatlarini kuzatish
Kreditor to'lovlarini rejalashtirish
DSO va DPO ko'rsatkichlarini nazorat qilish
Muddati o'tgan qarzdorlikni kamaytirish
Qayta undirish choralarini belgilash
6. Eskalatsiya tartibi
Cash Flow manfiy holatga tushsa
Budjet limiti oshib ketsa
Yirik qarzdorlik yuzaga kelsa
Soliq xavfi aniqlansa
Moliyaviy yo'qotish xavfi paydo bo'lsa
7. Direktorning nazorat chek-listi
□ Cash Flow tekshirildi
□ To'lovlar tasdiqlandi
□ Budjet og'ishlari ko'rib chiqildi
□ Debitor/Kreditor nazorat qilindi
□ Hisobotlar qabul qilindi
□ Moliyaviy risklar baholandi
2-qism yakuni
3-qismda KPI boshqaruvi, moliyaviy Dashboard, budjet ijrosi va moliyaviy ko'rsatkichlarni tahlil qilish standartlari bayon qilinadi.
Delegatsiya qilinadi | Delegatsiya qilinmaydi
To'lov hujjatlarini tayyorlash | Yillik budjetni tasdiqlash
Debitor monitoringi | Yirik to'lovlarni tasdiqlash
Kreditor reyestrini yuritish | Moliyaviy siyosatni tasdiqlash
Hisobotlarni tayyorlash | CEO uchun yakuniy moliyaviy hisobot
Bank hujjatlarini rasmiylashtirish | Likvidlik bo'yicha strategik qarorlar
Bosqich | Tekshiriladi | Mas'ul | Natija
Budjet | Limit mavjudligi | Direktor | Tasdiq
25% | To'lov hujjatlari | Buxgalter | Davom
50% | Cash Flow | Direktor | Qaror
75% | Bank ijrosi | G'aznachi | Nazorat
100% | Hisobot | Direktor | Yopish


## Moliya direktori operatsion qoidalari

**Source:** `AQ-03_3-qism_Moliya_Direktori_Amaliy_Qollanma.docx`

AQ-03
MOLIYA DIREKTORI UCHUN AMALIY QO'LLANMA
3-QISM
Mavzu: KPI boshqaruvi va moliyaviy Dashboard
1. KPI boshqaruvining maqsadi
Moliyaviy KPIlar kompaniyaning moliyaviy holatini real vaqt rejimida baholash, og'ishlarni aniqlash va boshqaruv qarorlarini qabul qilish uchun qo'llaniladi.
2. Asosiy moliyaviy KPIlar
3. Dashboard bo'yicha kunlik tekshiruv
Bank qoldiqlari
Cash Flow
Bugungi to'lovlar
Muddati o'tgan debitorlar
Kreditor majburiyatlari
Budjet og'ishlari
Qizil KPIlar
4. KPI monitoring algoritmi
1. Dashboardni ochish
2. Reja/Faktni solishtirish
3. Og'ishlarni aniqlash
4. Sabablarni tahlil qilish
5. Mas'ullar bilan muhokama
6. Tuzatish choralarini tasdiqlash
7. Qayta monitoring
5. KPI baholash mezonlari
6. Budget vs Actual tahlili
Daromad og'ishi
Xarajat og'ishi
Marja og'ishi
Pul oqimi og'ishi
Sabab va tuzatish rejasi
7. Direktor KPI chek-listi
□ Cash Flow tekshirildi
□ Budget vs Actual tahlil qilindi
□ DSO/DPO ko'rib chiqildi
□ EBITDA va foyda baholandi
□ Risklar qayd etildi
□ CEO uchun moliyaviy xulosa tayyorlandi
3-qism yakuni
4-qismda moliyaviy hisobotlarni qabul qilish, tahlil qilish, tahrirlash va CEO uchun Executive Report tayyorlash standartlari bayon qilinadi.
KPI | Manba | Davriylik | Mas'ul
Cash Flow | 1C/Bank | Kunlik | G'aznachilik
Budget vs Actual | 1C | Haftalik | Moliya
EBITDA | 1C | Oylik | Moliya direktori
Gross Profit | 1C | Haftalik | Moliya
Net Profit | 1C | Oylik | Moliya
DSO | CRM/1C | Haftalik | Debitor
DPO | 1C | Haftalik | Kreditor
Current Ratio | 1C | Oylik | Moliya
Holat | Mezon | Harakat
Yashil | 100%+ | Monitoring
Sariq | 90-99% | Tuzatish rejasi
Qizil | 89% va past | Favqulodda choralar


## Moliya direktori operatsion qoidalari

**Source:** `AQ-03_4-qism_Moliya_Direktori_Amaliy_Qollanma.docx`

AQ-03
MOLIYA DIREKTORI UCHUN AMALIY QO'LLANMA
4-QISM
Mavzu: Moliyaviy hisobotlarni qabul qilish, tahlil qilish va CEO uchun Executive Report
1. Hisobotlarni qabul qilish standarti
Har bir moliyaviy hisobot tasdiqlangan shakl, muddat va ma'lumotlar manbasi asosida qabul qilinadi.
Reja/Fakt majburiy taqqoslanadi
KPI natijalari ilova qilinadi
1C va bank ma'lumotlari mos bo'lishi kerak
Og'ish sabablari yoziladi
Tuzatish choralari ko'rsatiladi
2. Hisobotni tekshirish algoritmi
3. Haftalik moliyaviy hisobot
4. Oylik direktor hisoboti tarkibi
Daromad va xarajatlar
Cash Flow tahlili
Budget vs Actual
EBITDA va sof foyda
DSO/DPO ko'rsatkichlari
Moliyaviy risklar
Kelgusi oy rejasi
5. CEO uchun Executive Report
CEO hisoboti 1–2 sahifadan iborat bo'lib, faqat boshqaruv qarorlari uchun muhim ma'lumotlarni o'z ichiga oladi.
Asosiy KPIlar
Top 5 ijobiy natija
Top 5 muammo
Qaror talab qiladigan masalalar
Pul oqimi prognozi
Keyingi davr rejasi
6. Hisobotni rad etish mezonlari
KPI ko'rsatilmagan
Reja/Fakt mavjud emas
1C bilan tafovut mavjud
Dalillar ilova qilinmagan
Muddat buzilgan
7. Direktor chek-listi
□ Hisobotlar qabul qilindi
□ Cash Flow tekshirildi
□ KPIlar tasdiqlandi
□ Risklar baholandi
□ CEO Executive Report yuborildi
4-qism yakuni
5-qismda yig'ilishlar reglamenti, qarorlar reyestri, 30/60/90 kunlik reja, amaliy keyslar va yakuniy boshqaruv standartlari bayon qilinadi.
Bosqich | Tekshiruv
1 | Hisobot to'liqligi
2 | Reja/Fakt tekshiruvi
3 | KPIlarni tekshirish
4 | 1C va bank ma'lumotlarini solishtirish
5 | Og'ish sabablarini tahlil qilish
6 | Direktor xulosasi
7 | Tasdiqlash yoki qayta ishlash
Yo'nalish | Reja | Fakt | Og'ish | Qaror
Cash Flow
Budjet
Debitor
Kreditor
Foyda


## Moliya direktori operatsion qoidalari

**Source:** `AQ-03_5-qism_Moliya_Direktori_Amaliy_Qollanma.docx`

AQ-03
MOLIYA DIREKTORI UCHUN AMALIY QO'LLANMA
5-QISM
Mavzu: Yig'ilishlar reglamenti, qarorlar, amaliy keyslar va yakuniy boshqaruv standartlari
1. Direktor yig'ilishlari reglamenti
2. Finance Review kun tartibi
Cash Flow holati
Budget vs Actual
Debitor va kreditor qarzdorlik
Likvidlik ko'rsatkichlari
Moliyaviy risklar
Keyingi hafta rejasi
3. Qarorlar reyestri
4. Direktorning 30/60/90 kunlik rejasi
5. Amaliy keyslar
Keys 1. Cash Flow tanqisligi
To'lovlar ustuvorligini qayta ko'rib chiqish, tushumlarni tezlashtirish va qisqa muddatli likvidlik choralarini ko'rish.
Keys 2. Debitor qarzdorlik keskin oshdi
Qarzdorlar reytingi, undirish rejasi va kredit siyosatini qayta ko'rib chiqish.
Keys 3. Budjetdan oshiqcha xarajat
Og'ish sababini aniqlash, tasdiqlash tartibini kuchaytirish va tuzatish rejasini ishlab chiqish.
6. Ilovalar
To'lov talabnomasi
Cash Flow hisoboti
Budget vs Actual hisoboti
Haftalik moliyaviy hisobot
Oylik direktor hisoboti
CEO Executive Report
Yig'ilish bayonnomasi
Qarorlar reyestri
7. Direktorning yakuniy chek-listi
□ Cash Flow nazorat ostida
□ Budjet ijrosi tasdiqlandi
□ Debitor va kreditor nazorat qilindi
□ Risklar baholandi
□ Hisobotlar tasdiqlandi
□ CEO Executive Report yuborildi
AQ-03 yakuni
Mazkur qo'llanma Moliya direktorining kundalik, haftalik, oylik va strategik boshqaruv faoliyatini yagona korporativ standart asosida tashkil etish uchun ishlab chiqilgan hamda DP-03 Direksiya pasporti bilan birgalikda qo'llaniladi.
Yig'ilish turi | Davriyligi | Davomiyligi | Ishtirokchilar
Kunlik moliyaviy yig'ilish | Har kuni | 15 daqiqa | Moliya bo'limi rahbarlari
Finance Review | Haftada 1 marta | 60 daqiqa | Moliya direksiyasi
Budget Committee | Oyda 1 marta | 2 soat | CEO va direktorlar
Strategik sessiya | Chorakda 1 marta | 4 soat | Rahbariyat
Qaror | Mas'ul | Muddat | Holat | Izoh
Davr | Asosiy vazifalar
30 kun | Moliyaviy audit, KPI va Cash Flow tahlili
60 kun | Budjet intizomini kuchaytirish va DSO/DPOni yaxshilash
90 kun | Barqaror moliyaviy boshqaruv, avtomatlashtirish va prognozlash
