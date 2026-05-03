import os
import django
import requests
import random
from django.utils.text import slugify
from django.utils import timezone
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')
django.setup()

from news_app.models import News, Category

def download_image(url, filename):
    # Qalampir.uz da rasm sifatini oshirish uchun 'thumb_' yoki 'f_' ni 'm_' ga almashtiramiz
    high_res_url = url.replace('/thumb_', '/m_').replace('/f_', '/m_')
    
    try:
        # Avval yuqori sifatli rasmga urinib ko'ramiz
        response = requests.get(high_res_url, timeout=10)
        if response.status_code == 200:
            print(f"Yuqori sifatli rasm yuklandi: {high_res_url}")
            return ContentFile(response.content, name=filename)
        
        # Agar m_ versiyasi bo'lmasa, original URL ni sinaymiz
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return ContentFile(response.content, name=filename)
    except Exception as e:
        print(f"Rasm yuklashda xatolik: {url} -> {e}")
    return None

def populate_with_real_data():
    print("Eski ma'lumotlar o'chirilmoqda...")
    News.objects.all().delete()
    Category.objects.all().delete()

    real_data = [
        {
            "title": "Rossiya Ukrainaga yuzlab dron va raketalar bilan hujum qildi",
            "category": "Olam",
            "description": "Rossiya qurolli kuchlari Ukraina hududiga keng ko‘lamli dron va raketa hujumlarini amalga oshirdi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/oC/m_EtJ98Ms8hyed7HfVxVKs1viMo6vYha.jpg"
        },
        {
            "title": "15 bitli kalitni buzgan xaker bitkoin bilan taqdirlandi",
            "category": "Texnologiya",
            "description": "Murakkab kriptografik kalitni buzishga muvaffaq bo‘lgan mutaxassisga mukofot sifatida bitkoin berildi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/ui/m_ijo3AutrqcjhYSm3ZnrBuFmnWvVjun.jpg"
        },
        {
            "title": "Turkiya temirni qizig‘ida bosdi: Hormuz o‘rniga O‘rta koridor",
            "category": "Siyosat",
            "description": "Turkiya o‘zining geosiyosiy mavqeini mustahkamlash maqsadida yangi transport yo‘laklarini rivojlantirmoqda.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/sI/m_W1E6ylYcKqbZcCb9Yf6ZOs3DkFOl8l.jpg"
        },
        {
            "title": "Dunyoda ochlikdan aziyat chekayotganlarning 2/3 qismi 10 ta davlatda yashaydi",
            "category": "Jamiyat",
            "description": "Global oziq-ovqat xavfsizligi bo‘yicha hisobotda dunyodagi ochlik muammosining asosiy o‘choqlari ma’lum qilindi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/FG/m_lWjcg4z1DbVa2wPTMa4UQDuYHg05Td.jpg"
        },
        {
            "title": "Zelenskiy urush boshlanganidan beri ilk bor Ozarbayjonga bordi",
            "category": "Olam",
            "description": "Ukraina Prezidenti Vladimir Zelenskiy rasmiy tashrif bilan Bokuga yetib keldi.",
            "image_url": "https://cdn.beta.qalampir.uz/uploads/rq/f_kIsILZ3VkiwSGAberxOR9jLiJ3g7g0.jpg"
        },
        {
            "title": "JCH finali chiptalari 2 mln dollardan ortiq narxda e’lon qilindi",
            "category": "Sport",
            "description": "Futbol bo‘yicha jahon chempionati final uchrashuvi uchun chiptalar rekord darajadagi narxlarda sotuvga chiqdi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/7W/thumb_uLRt7tbgRKmBHXsqABShcPwEY8dWMQ.jpg"
        },
        {
            "title": "Eron va AQSH muzokaralarining ikkinchi raundi boshlanadi",
            "category": "Olam",
            "description": "Tomonlar yadroviy kelishuv va mintaqaviy xavfsizlik masalalarini muhokama qilishda davom etmoqda.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/dp/thumb_WsXV1aNfyzeTJbWdPT3eRTDZAwXZY3.jpg"
        },
        {
            "title": "2 gektar yerni 490 ming dollarga sotmoqchi bo‘lganlar ushlandi",
            "category": "Jamiyat",
            "description": "Huquqni muhofaza qiluvchi organlar tomonidan noqonuniy yer savdosi bilan bog‘liq jinoyat fosh etildi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/4Y/thumb_1vlwLeV9twKdrwhHCKqXt8fa4S9oP4.jpg"
        },
        {
            "title": "Endi tilanchilik qilgan xorijliklar quviladi. Qirg‘izistonda!",
            "category": "Olam",
            "description": "Qirg‘iziston hukumati jamoat tartibini saqlash maqsadida yangi qoidalarni joriy etdi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/ow/thumb_UJE3bygPLttXVB2UjY7RRe2AZxtrpn.jpg"
        },
        {
            "title": "Qozog‘istonda Sun’iy intellekt universiteti ochiladi",
            "category": "Olam",
            "description": "Qozog‘istonda sohaga ixtisoslashgan yangi oliy ta’lim muassasasi faoliyat boshlaydi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/X0/thumb_Axji85PaQOJtVgZ9sXakntuNR23UXB.jpg"
        },
        {
            "title": "AQSH otish orqali qatl qilish jazosini qaytarmoqda",
            "category": "Olam",
            "description": "Ayrim shtatlarda o‘lim jazosini ijro etishning eski usullari qayta ko‘rib chiqilmoqda.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/be/thumb_cfS6xtpzvIlSAA3Kgu8vyWBmhlG5GK.jpg"
        },
        {
            "title": "Pashinyan armanlar genotsidining asosiy sababini aytdi",
            "category": "Olam",
            "description": "Armaniston Bosh vaziri tarixiy voqealar bo‘yicha o‘z nuqtai nazarini bayon qildi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/kE/thumb_z00Sz2PFmpxQRROn2yewne5HsZRunN.jpg"
        },
        {
            "title": "“Qonunchilikka zid”. Biznes-ombudsman Toshkentning “Dizayn-kodi” bo‘yicha xulosa berdi",
            "category": "Jamiyat",
            "description": "Poytaxtdagi tashqi reklama va dizayn qoidalariga oid yangiliklar tadbirkorlar manfaatiga zid deb topildi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/5B/thumb_NSS1OJiMbg8ZIlQqzEkE7GCi4eN2Iz.jpg"
        },
        {
            "title": "Saida Mirziyoyeva Samarqanddagi ta’mirtalab ob’ektlarga bordi",
            "category": "Jamiyat",
            "description": "Prezident yordamchisi Samarqand viloyatidagi ijtimoiy va madaniy ob’ektlar holati bilan tanishdi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/mr/thumb_cMLNKlouksDH08KeRGCjapkJmu7R7h.jpg"
        },
        {
            "title": "2 mlrd so‘mlik kriptoaktivlarni aylantirgan shaxs ushlandi",
            "category": "Jamiyat",
            "description": "Noqonuniy kripto-ma’lumotlar almashinuvi bilan shug‘ullangan fuqaro qo‘lga olindi.",
            "image_url": "https://ad-admin.qalampir.uz/uploads/up/thumb_JYILuCe2BzgQEem0WkixPPEU8EiUqM.jpg"
        }
    ]

    print("Kategoriyalar va real yangiliklar yaratilmoqda...")
    category_objs = {}

    for item in real_data:
        cat_name = item["category"]
        if cat_name not in category_objs:
            category_objs[cat_name], _ = Category.objects.get_or_create(name=cat_name)
        
        category = category_objs[cat_name]
        title = item["title"]
        slug = slugify(title)
        
        # Unique slug check
        if News.objects.filter(slug=slug).exists():
            slug = f"{slug}-{random.randint(100, 999)}"

        news = News(
            title=title,
            slug=slug,
            body=(item["description"] + "\n\n") * 10,
            category=category,
            status=News.Status.Published,
            published_time=timezone.now()
        )
        
        # Rasm yuklash
        img_content = download_image(item["image_url"], f"{slug}.jpg")
        if img_content:
            news.image.save(f"{slug}.jpg", img_content, save=False)
        
        news.save()
        print(f"Qo'shildi: {title}")

    print("\nBarcha real ma'lumotlar Qalampir.uz dan muvaffaqiyatli ko'chirildi!")

if __name__ == '__main__':
    populate_with_real_data()