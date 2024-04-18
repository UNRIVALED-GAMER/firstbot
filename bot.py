import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Türkiye'deki 10 şehrin kültürel özelliklerini içeren bir sözlük oluşturalım
turkiye_sehirleri = {
    "İstanbul": "İstanbul, tarihi ve kültürel mirasıyla ünlü bir şehirdir. Ayasofya, Topkapı Sarayı ve Kapalıçarşı gibi önemli turistik yerlere ev sahipliği yapar.",
    "Ankara": "Ankara, Türkiye'nin başkenti ve politik merkezidir. Anıtkabir, Kocatepe Camii ve Etnografya Müzesi gibi önemli yerlere ev sahipliği yapar.",
    "İzmir": "İzmir, Ege'nin incisi olarak bilinir. Saat Kulesi, Konak Meydanı ve Kemeraltı Çarşısı gibi turistik mekanlarıyla dikkat çeker.",
    "Antalya": "Antalya, doğal güzellikleri ve tarihi zenginlikleriyle ünlü bir tatil beldesidir. Kaleiçi, Düden Şelalesi ve Konyaaltı Plajı gibi yerleri barındırır.",
    "Bursa": "Bursa, tarihi ve kültürel mirasıyla dikkat çeken bir şehirdir. Uludağ, Yeşil Türbe ve Bursa Kalesi gibi önemli yerleri bulunur.",
    "Adana": "Adana, Türkiye'nin güneyinde yer alan bir şehirdir. Taş Köprü, Merkez Park ve Adana Arkeoloji Müzesi gibi yerleri barındırır.",
    "Konya": "Konya, tarihi ve dini öneme sahip bir şehirdir. Mevlana Müzesi, Alaeddin Tepesi ve Karatay Medresesi gibi yerleri bulunur.",
    "Trabzon": "Trabzon, Karadeniz'in incisi olarak bilinir. Sumela Manastırı, Atatürk Köşkü ve Uzungöl gibi yerleri barındırır.",
    "Gaziantep": "Gaziantep, tarihi ve kültürel zenginlikleriyle dikkat çeken bir şehirdir. Gaziantep Kalesi, Zeugma Mozaik Müzesi ve Bakırcılar Çarşısı gibi yerleri bulunur.",
    "Mersin": "Mersin, Akdeniz'in önemli şehirlerinden biridir. Tarihi Silifke Kalesi, Kızkalesi ve Anamur Müzesi gibi yerleri barındırır."
}

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    
    elif message.content.startswith('$bye'):
        await message.channel.send("Görüşürüz!")
    
    elif message.content.startswith('$senkimsin'):
        await message.channel.send("Ben bir Discord botuyum. Kullanıcılara çeşitli komutlarla yardımcı olmak için buradayım.")
    
    elif message.content.startswith('$kulturel_ozellik'):
        sehir = message.content.split(' ', 1)[1]
        if sehir in turkiye_sehirleri:
            await message.channel.send(turkiye_sehirleri[sehir])
        else:
            await message.channel.send("Üzgünüm, bu şehir hakkında bilgi bulunamadı.")
    
    else:
        await message.channel.send("Üzgünüm, anlamadım. Yardımcı olabileceğim başka bir şey var mı?")

client.run("token")
