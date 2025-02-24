# VectorStore

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak vector store ile bir proje geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

Projede, Gemini AI ile birlikte Langchain framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır. Doküman okuma, yükleme, embedding işlemleri ve vektör database işlemleri için langchain framework'ünden faydalanılmıştır. LangChain, LLM'ler ile entegrasyon sağlayarak özelleştirilmiş sorgu yönetimi sunmaktadır.

<h3> Vector Store </h3>

<br>
Elimizde birçok veri / bilgi olduğunda en alakalı / mantıklı cevabı vermeyi sağlamaktadır. Vektörleştirme işlemi için ayrı embedding modelleri kullanılmaktadır.  Bu vektörler vector store'da kayıt edilmektedir.

Bu çalışmada embedding fonksiyonu olarak __HuggingFaceEmbeddings__ kullanılmıştır.
<br>
Çalışmada vektör veri tabanı olarak Chroma kullanılmıştır. Chroma open source bir vektör veri tabanıdır.
<br>
Kullanılan dökümanlar kod içerisinde de tanımlanabilmektedir. Bir dosyadan da yüklenebilmektedir. Her iki örnek kod dosyasında mevcuttur.

<br>

Çalışmada langchain kullanılarak temel bir RAG mantığı kodlanmıştır. LLM'ler vector store kullanarak özelleştirilmiştir. Böylece kendi dökümanımızdaki veriler okunarak LLM'in istenilen cevapları vermesi sağlanmaktadır. Vector store'lar __similarity search__ ile dökümandaki benzer veriyi çıktı olarak sunmaktadır.

Çalışmanın örnek çıktıları Şekil 1 ve Şekil 2'de görülmektedir.

<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/c5256344-4110-45ec-bc35-b37c2d3e7310" alt="image">
</div>
Şekil 1. Örnek çıktı

<br>
<br>


<div align="center">
<img src="https://github.com/user-attachments/assets/a316d309-76ab-4f7c-b7d1-319eef947d08" alt="image">
</div>

Şekil 2. Örnek çıktı
