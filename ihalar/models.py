from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class Iha(models.Model):
    state_choice=(
        ('01', 'Adana'), ('02', 'Adıyaman'), ('03', 'Afyonkarahisar'), ('04', 'Ağrı'), ('68', 'Aksaray'),
        ('05', 'Amasya'), ('06', 'Ankara'), ('07', 'Antalya'), ('75', 'Ardahan'), ('08', 'Artvin'), ('09', 'Aydın'),
        ('10', 'Balıkesir'), ('74', 'Bartın'), ('72', 'Batman'), ('69', 'Bayburt'), ('11', 'Bilecik'), ('12', 'Bingöl'),
        ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'), ('17', 'Çanakkale'), ('18', 'Çankırı'),
        ('19', 'Çorum'), ('20', 'Denizli'), ('21', 'Diyarbakır'), ('81', 'Düzce'), ('22', 'Edirne'), ('23', 'Elazığ'),
        ('24', 'Erzincan'), ('25', 'Erzurum'), ('26', 'Eskişehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),
        ('29', 'Gümüşhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('76', 'Iğdır'), ('32', 'Isparta'), ('33', 'Mersin'),
        ('34', 'İstanbul'), ('35', 'İzmir'), ('78', 'Karabük'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),
        ('39', 'Kırklareli'), ('40', 'Kırşehir'), ('41', 'Kocaeli'), ('42', 'Konya'), ('43', 'Kütahya'),
        ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmaraş'), ('70', 'Karaman'), ('71', 'Kırıkkale'),
        ('79', 'Kilis'), ('47', 'Mardin'), ('48', 'Muğla'), ('49', 'Muş'), ('50', 'Nevşehir'), ('51', 'Niğde'),
        ('52', 'Ordu'), ('80', 'Osmaniye'), ('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'),
        ('57', 'Sinop'), ('58', 'Sivas'), ('73', 'Şırnak'), ('59', 'Tekirdağ'), ('60', 'Tokat'), ('61', 'Trabzon'),
        ('62', 'Tunceli'), ('63', 'Şanlıurfa'), ('64', 'Uşak'), ('65', 'Van'), ('77', 'Yalova'), ('66', 'Yozgat'),
        ('67', 'Zonguldak'),
    )
    features_choices = (
        ('Lojistik', 'Lojistik'),
        ('ARGE', 'ARGE'),
        ('Sivil ve Ticari', 'Sivil ve Ticari'),
        ('Taktiksel', 'Taktiksel'),
        ('Hedef İnsansız', 'Hedef İnsansız'),
        ('Askeri', 'Askeri'),
    )
    year_choice= []
    for r in range(2000,(datetime.now().year+1)):
        year_choice.append((r,r))

    state = models.CharField(choices=state_choice,max_length=100)
    city = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    color = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = RichTextField(max_length=2000)
    iha_foto = models.ImageField(upload_to='photos/%Y/%m/%d/')
    iha_foto_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    iha_foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    iha_foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    features = MultiSelectField(choices=features_choices, max_length=20)
    engine = models.CharField(max_length=100)
    vin_no = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    iha_title = models.CharField(max_length=255)

    def __str__(self):
        return self.iha_title