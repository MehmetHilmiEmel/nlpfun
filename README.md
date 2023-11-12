
# Projenin Tanımı
Doğal Dil İşleme (Natural Language Processing - NLP) alanında uygulanan metin özetleme, sohbet botu, duygu durum analizi gibi bazı uygulamaların bulunduğu bir web sitesi.
# Projenin Amacı
Bu projede, kullanıcıların bu uygulamalara kolay ve hızlı bir şekilde ulaşmaları ve kullanmaları amaçlanmıştır.
# Doğal Dil İşleme Nedir?
Doğal dil işleme (natural language processing), bilgisayarlara insan dilini okuma, anlama ve yorumlama yeteneği veren bir yapay zeka uygulamasıdır. Bilgisayarların, insan duygularını ölçmesine ve insan dilinin hangi bölümlerinin önemli olduğunu belirlemesine yardımcı olur.<br />

Bu projede doğal dil işleme alanında geliştirilen modellere kolayca ulaşabilmek için Hugging Face kütüphanesi kullanıldı. 
# Hugging Face Nedir?
![alt text](https://time-to-reinvent.com/wp-content/uploads/2022/02/rectangle_large_type_2_6b3d7a7cdfb3af98774ab76a8aa9ef03.png) <br />
Hugging Face Hub, insanların kolayca işbirliği yapabileceği ve birlikte makine öğrenimi oluşturabileceği çevrimiçi bir platformda, tümü açık kaynaklı ve herkese açık olan 60K'dan fazla model, 6K veri kümesi ve 6K demo uygulaması (Spaces) içeren bir platformdur. Hub, herkesin Makine Öğrenimi ile keşfedebileceği, deneyebileceği, işbirliği yapabileceği ve teknoloji oluşturabileceği merkezi bir yer olarak çalışır.

# Kullanılan Modeller

- Metin özetleme için:<a href="https://huggingface.co/mrm8488/bert2bert_shared-turkish-summarization" target="_blank">"mrm8488/bert2bert_shared-turkish-summarization"</a> <br />
- Duygu analizi için :<a href="https://huggingface.co/savasy/bert-base-turkish-sentiment-cased" target="_blank">"savasy/bert-base-turkish-sentiment-cased"</a> <br />
- Sohbet botu için : <a href="https://huggingface.co/facebook/blenderbot-400M-distill" target="_blank">"facebook/blenderbot-400M-distill"</a>
modelleri kullanıldı.<br />

NOT: Sohbet botunun hali hazırda Türkçe ile eğitilmiş bir modeli olmadığı için projenin içinde python'un "googletrans" kütüphanesi eklendi. Kullanıcı tarafından girilen cümle ilk olarak İngilizce'ye çevrilip sonrasında modelin verdiği cevap İngilizce'den Türkçe'ye çevrildi.

### Prerequisites
- Python
- Pip

### Installation
```bash
pip install virtualenv
```
```bash
virtualenv venv
```

# Activate the virtual environment
```bash
venv\Scripts\activate   # For Windows
source venv/bin/activate # For macOS/Linux
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run the application
```bash
python manage.py runserver
```

Uygulamaya http://127.0.0.1:8000/ adresinden erişilebilecektir.
