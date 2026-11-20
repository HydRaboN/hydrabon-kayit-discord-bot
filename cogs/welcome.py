import discord
from discord.ext import commands
import random

# Hoş geldin mesajları - İstediğiniz mesajları ekleyebilirsiniz
# {} yerine kullanıcının adı gelecek
WELCOME_MESSAGES = [
    "Hoş geldin {}! Seni aramızda görmek çok güzel, rahatına bak 😊 Bize biraz kendinden bahseder misin?",
    "Selam {}, HydRaboN ailesine hoş geldin! Seni buralara hangi rüzgâr attı?",
    "Hey {}, aramıza hoş geldin! Burada herkes birbirini tanıyor, şimdi sıra seni tanımakta. Nasılsın bakalım?",
    "Hoş geldin {}! Sana nasıl hitap etmemizi istersin?",
    "{} aramıza katıldı, hoş geldin! Hangi konularda sohbet etmeyi seversin?",
    "Hoş geldin {}! Boş zamanlarında neler yapmaktan keyif alırsın?",
    "Selam {}, hoş geldin! Son izlediğin film ya da dizi neydi, tavsiye eder misin? 🎬",
    "Hoş geldin {}! Genelde hangi saatlerde buralarda olursun, denk gelelim 😄",
    "Hey {}, hoş geldin! Bugünlerde uğraştığın, kafa yorduğun bir şey var mı?",
    "Selam {}, aramıza hoş geldin! Topluluk etkinliklerinden en çok hangisi ilgini çeker?",
    "Hoş geldin {}! Sunucuda ilk gözüne çarpan ne oldu?",
    "{} geldi, hoş geldin! İlk olarak nereleri keşfetmeyi düşünüyorsun?",
    "Hoş geldin {}! Sence bir topluluğu güzel yapan şey nedir?",
    "Hey {}, HydRaboN'a hoş geldin! En çok hangi oyunda kendine güveniyorsun? 🎮",
    "Merhaba {}, iyi ki geldin! Kendini bir oyun karakteriyle anlatsan hangisi olurdu?",
    "Hoş geldin {}, aramıza katıldığın için çok mutluyuz! Bu aralar en çok neyi başarmak istiyorsun?",
    "Selam {}, hoş geldin! Bizimle paylaşmak istediğin bir hayalin var mı?",
    "Hoş geldin {}! Burada en çok ne yapmak, ne öğrenmek istersin?",
    "Hey {}, hoş geldin! İlk mesajını merakla bekliyoruz, günün nasıl geçiyor?",
    "Merhaba {}, hoş geldin! Takım oyunu mu, keyifli bir sohbet mi, hangisi daha çok sen?",
    "Hey {}, aramıza katıldığın için çok mutluyuz! Senin gizli yeteneğin ne? ✨",
    "Hoş geldin {}! Seni en çok ne motive eder?",
    "{} geldi, hoş geldin! Sunucuya bir şey eklemek istesen ne olurdu?",
    "Hoş geldin {}! Sunucuda bir etkinlik düzenlesek katılmak isteyeceğin ilk şey ne olurdu?",
    "Selam {}, hoş geldin! En çok hangi oyunda iddialısın, söyle de bir kapışalım 😄",
    "Hoş geldin {}! Burada seni en çok ne mutlu eder?",
    "Selam {}, hoş geldin! Hemen sohbete dalanlardan mısın, yoksa önce biraz ortama mı bakarsın?",
    "Hoş geldin {}! Sence iyi bir ekipte olmazsa olmaz şey nedir?",
    "Hey {}, hoş geldin! Yeni biriyle tanışırken ilk ne sorarsın? Cevabını biz de merak ettik 😄",
    "Selam {}, hoş geldin! Şu anki ruh halini bir emojiyle anlatır mısın?",
    "Hey {}, aramıza hoş geldin! Burada güzel anılar biriktireceğine eminiz 💙",
    "Merhaba {}, hoş geldin! Sevdiğin bir şarkıyı paylaşarak başlamaya ne dersin? 🎵",
    "Selam {}, hoş geldin! Bu aralar aşmaya çalıştığın bir zorluk var mı? Belki birlikte bir yolunu buluruz.",
    "{} geldi ve ortam şenlendi! Hoş geldin, yapmaktan en çok keyif aldığın şey ne?",
    "Selam {}, hoş geldin! Kendini 3 kelimeyle anlatır mısın?",
    "Hoş geldin {}! Bir süper gücün olsaydı ne olmasını isterdin?",
    "{} aramıza katıldı, hoş geldin! Sana en çok ne ilham verir?",
    "{}, hoş geldin! Sence başarı ne demek?",
    "Hey {}, hoş geldin! Seni tanımak için sabırsızlanıyoruz. Şu an istediğin herhangi bir yerde olabilseydin, neresi olurdu?",
    "Hoş geldin {}! Hayat mottonu bizimle paylaşır mısın?",
    "Selam {}, hoş geldin! Bugün kendine bir söz verecek olsan ne olurdu?",
    "Hoş geldin {}! Hayatında örnek aldığın biri var mı?",
    "{} geldi, ailemiz büyüyor! Hoş geldin, kendine koyduğun son hedef neydi?",
    "Selam {}, hoş geldin! Hayat bir oyun olsaydı sen hangi rolde olurdun?",
    "Merhaba {}, hoş geldin! Hangi oyun ya da film karakteriyle aynı takımda olmak isterdin?",
    "Hoş geldin {}! Unutamadığın güzel bir anını paylaşır mısın?",
    "Hey {}, hoş geldin! Bugün seni gülümseten bir şey oldu mu? 😊",
    "Hoş geldin {}! Sence en güçlü yönün ne?",
    "Selam {}, hoş geldin! Kendine bir lakap seçsen ne olurdu?",
    "{} aramıza katıldı, hoş geldin! En büyük hayalini bizimle paylaşmak ister misin?",
    "Selam {}, hoş geldin! Görmeyi en çok istediğin yer neresi? 🌍",
    "Hoş geldin {}! Büyük şeyler küçük adımlarla başlar, buradaki ilk adımın ne olsun?",
    "{}, aramıza hoş geldin! Bu aralar kendini hangi konuda geliştirmek istiyorsun?",
    "Merhaba {}, hoş geldin! Bir kitap yazsan adı ne olurdu? 📖",
    "{} geldi, hoş geldin! Şu anki ruh halin bir renk olsaydı hangisi olurdu? 🎨",
    "Hoş geldin {}! Hafta sonların genelde nasıl geçer?",
    "Selam {}, hoş geldin! Yeni bir şey denemek istesen ne olurdu?",
    "Hoş geldin {}! Birlikte çok güzel anılar biriktireceğiz. Sence hayatın en güzel anları nerede saklı?",
    "{} geldi, hoş geldin! Şimdi sıra sende: Burada ilk ne yaşamak istersin?",
    "Hoş geldin {}, artık sen de bizden birisin! Çay mı kahve mi? ☕",
    "Selam {}, hoş geldin! En sevdiğin yemek ne, merak ettik 🍕",
    "Hey {}, hoş geldin! Burada herkes bir zamanlar yeniydi, kendini yabancı hissetme 😊 Nasılsın?"
]

class Welcome(commands.Cog):
    """Yeni üye karşılama sistemi"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.welcome_channel_id = 1406431661872124026  # Sohbet-muhabbet kanalı
        self.new_member_role_id = 1428496119213588521  # Yeni üyelere verilecek rol (KAYITSIZ UYE)
        self.unregistered_chat_channel_id = 1477433179857223892  # Kayıtsız-sohbet kanalı
        self.registration_channel_id = 1428811701708394558  # Kayıt (hoş geldin) kanalı

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Yeni üye sunucuya katıldığında çalışır"""
        
        if member.bot:
            return
        
        guild = member.guild

        # Rol verme
        try:
            role = guild.get_role(self.new_member_role_id)
            if role:
                await member.add_roles(role, reason="Yeni üye otomatik rol")
            else:
                print(f"[HATA] Yeni üye rolü bulunamadı! Rol ID: {self.new_member_role_id}")
        except discord.Forbidden:
            print(f"[HATA] Yeni üyeye rol verme yetkisi yok! Üye: {member}")
        except Exception as e:
            print(f"[HATA] Yeni üyeye rol verilirken hata: {type(e).__name__}: {e}")

        # Kayıtsız-sohbet kanalında kayıt yönlendirmesi
        try:
            channel = guild.get_channel(self.unregistered_chat_channel_id)
            if channel:
                await channel.send(
                    f"Hoş geldin {member.mention}! 👋 <#{self.registration_channel_id}> kanalından kayıt olabilirsin, "
                    f"istersen yaşını gizleyebilirsin. Bir sorun yaşarsan **Yetkili Çağır** butonunu kullanman yeterli."
                )
            else:
                print(f"[HATA] Kayıtsız-sohbet kanalı bulunamadı! Kanal ID: {self.unregistered_chat_channel_id}")
        except discord.Forbidden:
            print(f"[HATA] Kayıtsız-sohbet kanalına mesaj gönderme yetkisi yok!")
        except Exception as e:
            print(f"[HATA] Kayıt yönlendirme mesajı gönderilirken hata: {type(e).__name__}: {e}")

        # NOT: Sohbet kanalındaki hoş geldin mesajı kayıt işlemi tamamlandıktan sonra gönderiliyor
    
    def get_welcome_message(self, member: discord.Member) -> str:
        """Rastgele hoş geldin mesajı döndürür"""
        return random.choice(WELCOME_MESSAGES).format(member.mention)
    
    async def send_welcome_message(self, member: discord.Member):
        """Kayıt başarılı olduğunda hoş geldin mesajı gönderir"""
        try:
            guild = member.guild
            channel = guild.get_channel(self.welcome_channel_id)
            if channel:
                # Rastgele mesaj seç
                message = self.get_welcome_message(member)
                await channel.send(message)
            else:
                print(f"[HATA] Hoş geldin kanalı bulunamadı! Kanal ID: {self.welcome_channel_id}")
        except discord.Forbidden:
            print(f"[HATA] Hoş geldin kanalına mesaj gönderme yetkisi yok!")
        except Exception as e:
            print(f"[HATA] Hoş geldin mesajı gönderilirken hata: {type(e).__name__}: {e}")


async def setup(bot: commands.Bot):
    """Cog'u yükler"""
    await bot.add_cog(Welcome(bot))

