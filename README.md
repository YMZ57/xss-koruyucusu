# XSS Koruyucusu

## Proje Hakkinda

Bu proje, web uygulamalarinda sik gorulen **XSS (Cross Site Scripting)** acigini gostermek ve bu aciga karsi temel bir koruma mantigini uygulamak amaciyla hazirlanmistir.

XSS aciklarinda saldirgan, kullanici input alanlarina JavaScript kodu yerlestirerek bu kodun tarayici tarafinda calismasini saglayabilir. Eger uygulama kullanicidan gelen veriyi dogrudan sayfada gosterirse, zararli script kodlari da normal bir veri gibi degil, calisabilir kod gibi yorumlanir.

Bu projede, ayni yorum sistemi iki farkli sekilde ele alinmistir:

- **Guvensiz Surum**
- **Guvenli Surum**

Boylece hem acigin nasil olustugu hem de nasil engellenebilecegi uygulamali olarak gosterilmektedir.

---

## Proje Amaci

Bu projenin amaci:

- kullanici girdisinin dogrudan render edilmesinin riskini gostermek
- XSS payload'larinin nasil calisabildigini gostermek
- backend tarafinda uygulanan `escape()` mantigi ile bu riski azaltmak
- guvensiz ve guvenli yapi arasindaki farki ayni uygulama uzerinde gostermek

---

## Calisma Mantigi

Projede kullanici, yorum formuna bir ad ve yorum girer.

### Guvensiz Sayfa

Bu bolumde kullanici girdisi herhangi bir koruma uygulanmadan ekrana basilir.  
Bu nedenle kullanicinin girdigi zararli bir script kodu tarayici tarafinda calisabilir.

### Guvenli Sayfa

Bu bolumde ise kullanicidan gelen veri backend tarafinda `escape()` fonksiyonu ile donusturulur.  
Boylece `<script>` gibi etiketler HTML veya JavaScript olarak degil, duz metin olarak gorunur.

---

## Ornek XSS Payload

Asagidaki payload, guvensiz sayfada test amaciyla kullanilabilir:

```html
<script>alert('XSS')</script>
```

Bu payload:

- **Guvensiz Sayfa** icinde calisabilir
- **Guvenli Sayfa** icinde ise sadece yazi olarak gorunur

Bu fark, uygulanan korumanin dogrudan sonucudur.

---

## Kullanilan Teknolojiler

Bu projede asagidaki teknolojiler kullanilmistir:

- Python
- Flask
- HTML
- CSS
- MarkupSafe

---

## Dosya Yapisi

```text
xss_project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── vulnerable.html
│   └── safe.html
│
└── static/
    └── style.css
```

---

## Dosyalarin Gorevleri

### app.py
Flask uygulamasinin ana dosyasidir. Route yapilari ve yorum isleme mantigi burada bulunur.

### requirements.txt
Projenin calismasi icin gerekli Python kutuphanelerini icerir.

### templates/index.html
Ana giris sayfasidir.

### templates/vulnerable.html
Guvensiz yorum sayfasidir. XSS aciginin nasil olustugunu gostermek icin kullanilir.

### templates/safe.html
Guvenli yorum sayfasidir. Escape edilmis veri ile koruma uygulanir.

### static/style.css
Sayfalarin gorunumunu duzenleyen CSS dosyasidir.

---

## Kurulum

Projeyi calistirmak icin once gerekli kutuphaneler yuklenmelidir:

```bash
pip install -r requirements.txt
```

Ardindan uygulama baslatilir:

```bash
python app.py
```

Daha sonra tarayicidan asagidaki adres acilir:

```text
http://127.0.0.1:5000
```

---

## Test Adimlari

### 1. Guvensiz Sayfa Testi

1. Ana sayfadan **Guvensiz Sayfa** secilir.
2. Yorum kutusuna asagidaki payload yazilir:

```html
<script>alert('XSS')</script>
```

3. Yorum gonderilir.
4. Eger popup penceresi aciliyorsa, XSS payload'i basarili sekilde calismistir.

### 2. Guvenli Sayfa Testi

1. Ana sayfadan **Guvenli Sayfa** secilir.
2. Ayni payload tekrar girilir.
3. Yorum gonderilir.
4. Popup acilmaz, payload yalnizca duz metin olarak gorunur.

---

## Guvenlik Yaklasimi

Bu projede uygulanan temel savunma yaklasimi, kullanicidan gelen veriyi dogrudan render etmemektir.

Guvenli sayfada su mantik kullanilmistir:

```python
from markupsafe import escape

safe_comment = escape(comment)
```

Bu yaklasim sayesinde:

- `<` ve `>` gibi karakterler dogrudan islenmez
- tarayici bu veriyi kod olarak calistirmaz
- zararli scriptler duz metne donusur

Bu, temel ama etkili bir XSS savunmasidir.

---

## Sonuc

Bu proje ile su fark acik sekilde gosterilmektedir:

- Kullanici girdisi dogrudan islenirse XSS acigi olusabilir.
- Kullanici girdisi guvenli sekilde escape edilirse zararli scriptlerin calisma riski azalir.
- Web uygulamalarinda input guvenligi, sadece frontend degil backend tarafinda da ele alinmalidir.

Bu nedenle kullanici verileri guvenli sekilde filtrelenmeli, escape edilmeli veya uygun sanitize yontemleri ile islenmelidir.

---

## Yapan

YMZ57
