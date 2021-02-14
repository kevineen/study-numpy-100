# flake8: noqa
from django.db import models
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError


class Customer(models.Model):
    name = models.CharField(verbose_name="顧客名", default="", max_length=50)

    formal_name = models.CharField(verbose_name="正式名称", default="", max_length=50)

    text = models.TextField(verbose_name="備考", default="", blank=True, null=True,)

    logo = models.TextField(verbose_name="ロゴ", default="", blank=True, null=True,)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class LogoImage(models.Model):
    company = models.ForeignKey(
        "Customer",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="会社",
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title


class CustomerPlace(models.Model):

    company = models.ForeignKey(
        "Customer",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="会社",
    )

    name = models.CharField(verbose_name="工場・事業場所名", default="", max_length=50)

    postal = models.CharField(verbose_name="郵便番号", default="", max_length=7,)

    address = models.TextField(verbose_name="住所", default="", blank=True, null=True,)

    tel_number_regex = RegexValidator(
        regex=r"^[0-9]+$",
        message=(
            "Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."
        ),
    )

    tell = models.CharField(
        validators=[tel_number_regex],
        max_length=15,
        verbose_name="電話番号1",
        blank=True,
        null=True,
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    name = models.CharField(verbose_name="職名", default="", max_length=50,)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class GuestJobTitle(models.Model):

    company = models.ForeignKey(
        "Customer",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="会社",
    )

    name = models.CharField(verbose_name="部署名・職名", default="", max_length=50,)

    isTop = models.BooleanField(default=False, verbose_name="トップ部署",)

    parent = models.ForeignKey(
        "self",
        to_field="id",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="上位組織",
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Guest(models.Model):

    company = models.ForeignKey(
        "Customer",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="会社",
    )

    department = models.ForeignKey(
        "GuestJobTitle",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="所属部署",
    )

    firstName = models.CharField(verbose_name="名前", max_length=12,)

    callFirstName = models.CharField(verbose_name="名ヨミ", max_length=12,)

    lastName = models.CharField(verbose_name="苗字", max_length=12,)

    callLastName = models.CharField(verbose_name="苗ヨミ", max_length=12,)

    tel_number_regex = RegexValidator(
        regex=r"^[0-9]+$",
        message=(
            "Tel Number must be \
             entered in the format: '09012345678' Up to 15 digits allowed."
        ),
    )

    tell_1 = models.CharField(
        validators=[tel_number_regex],
        max_length=15,
        verbose_name="電話番号1",
        blank=True,
        null=True,
    )

    tell_2 = models.CharField(
        validators=[tel_number_regex],
        max_length=15,
        verbose_name="電話番号2",
        blank=True,
        null=True,
    )

    mail = models.EmailField(verbose_name="PCメールアドレス", blank=True, null=True,)

    phoneMail = models.EmailField(verbose_name="携帯メールアドレス", blank=True, null=True,)

    text = models.TextField(blank=True, null=True,)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstName


class Employee(models.Model):

    jobTitle = models.ForeignKey(
        "JobTitle",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="職種",
    )

    firstName = models.CharField(verbose_name="名前", max_length=12,)

    callFirstName = models.CharField(verbose_name="名ヨミ", max_length=12,)

    lastName = models.CharField(verbose_name="苗字", max_length=12,)

    callLastName = models.CharField(verbose_name="苗ヨミ", max_length=12,)

    tel_number_regex = RegexValidator(
        regex=r"^[0-9]+$",
        message=(
            "Tel Number must be \
            entered in the format: '09012345678'. Up to 15 digits allowed."
        ),
    )

    tell_1 = models.CharField(
        validators=[tel_number_regex],
        max_length=15,
        verbose_name="電話番号1",
        blank=True,
        null=True,
    )

    tell_2 = models.CharField(
        validators=[tel_number_regex],
        max_length=15,
        verbose_name="電話番号2",
        blank=True,
        null=True,
    )

    mail = models.EmailField(verbose_name="PCメールアドレス", blank=True, null=True,)

    phoneMail = models.EmailField(verbose_name="携帯メールアドレス", blank=True, null=True,)

    text = models.TextField(blank=True, null=True,)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstName


class Order(models.Model):
    orderNumber = models.IntegerField(
        verbose_name="オーダーNo.",
        default=200000,
        validators=[MinValueValidator(0), MaxValueValidator(999999)],
        unique=True,
    )

    subject = models.TextField(blank=True, null=True, verbose_name="件名")

    frontUser = models.ForeignKey(
        "Customer",
        related_name="fCustomer_id",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="フロントユーザー",
    )

    middleUser = models.ForeignKey(
        "Customer",
        related_name="mCustomer_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="ミドルユーザー",
    )

    endUser = models.ForeignKey(
        "Customer",
        related_name="eCustomer_id",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="エンドユーザー",
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.orderNumber)


class Product(models.Model):
    orderNumber = models.ForeignKey(
        "Order",
        to_field="id",
        verbose_name="オーダーNo.",
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.TextField(verbose_name="品名", blank=True, null=True,)

    to_user = models.ForeignKey(
        "CustomerPlace",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="送り先",
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.orderNumber)


class Specification(models.Model):
    productNumber = models.ForeignKey(
        "Product",
        to_field="id",
        verbose_name="製品",
        null=True,
        on_delete=models.SET_NULL,
    )

    needCustomer = models.ForeignKey(
        "Customer",
        to_field="id",
        verbose_name="需要先",
        related_name="nCustomer_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    orderCustomer = models.ForeignKey(
        "Customer",
        to_field="id",
        verbose_name="注文先",
        related_name="oCustomer_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    isContact = models.BooleanField(verbose_name="有接点", default=False,)

    isNotContact = models.BooleanField(verbose_name="無接点", default=False,)

    quantity = models.CharField(default=1, max_length=100, verbose_name="数量")

    isNotContact = models.BooleanField(verbose_name="無接点", default=False,)

    isCustomerSpecification = models.BooleanField(default=False, verbose_name="客先仕様有無",)

    isCustomerSpecificationNo = models.TextField(
        blank=True, null=True, verbose_name="客先仕様文書番号"
    )

    mainVoltType = models.CharField(verbose_name="主電源電圧種類", max_length=2, default="AC",)

    mainVoltagePhase = models.CharField(
        verbose_name="主要電圧相", blank=True, null=True, default=3, max_length=4,
    )

    mainLineCount = models.CharField(
        verbose_name="主電源線数", blank=True, null=True, default=3, max_length=1,
    )

    mainHz = models.CharField(verbose_name="主電源周波数", max_length=2, default=50,)

    controlVoltType = models.TextField(
        verbose_name="制御源電圧種類", blank=True, null=True, default="DC",
    )

    controlVoltagePhase = models.CharField(
        verbose_name="制御電圧相", default=3, max_length=4
    )

    controlLineCount = models.CharField(verbose_name="制御電源線数", default=3, max_length=1)

    controlHz = models.CharField(
        verbose_name="制御電源周波数", blank=True, null=True, max_length=2, default=50,
    )

    isOutdoor = models.BooleanField(verbose_name="屋外", default=False,)

    isIndoor = models.BooleanField(verbose_name="屋内", default=False,)

    isSelfRelianace = models.BooleanField(verbose_name="自立", default=False,)

    isWallHanging = models.BooleanField(verbose_name="壁掛", default=False,)

    isPortable = models.BooleanField(verbose_name="可搬", default=False,)

    ambientCondition = models.TextField(
        verbose_name="周囲条件", blank=True, null=True, default="",
    )

    isOpen = models.BooleanField(verbose_name="開放", default=False,)

    isClose = models.BooleanField(verbose_name="閉鎖", default=False,)

    isDustproof = models.BooleanField(verbose_name="防塵", default=False,)

    isSplashpoof = models.BooleanField(verbose_name="防滴", default=False,)

    isWaterproof = models.BooleanField(verbose_name="防水", default=False,)

    isPanel = models.BooleanField(verbose_name="パネル", default=False,)

    isAntiVibration = models.BooleanField(verbose_name="防振", default=False,)

    isAirPurge = models.BooleanField(verbose_name="そのた(エアパージ)", default=False,)

    isBothDoor = models.BooleanField(verbose_name="両扉", default=False,)

    is90Open = models.BooleanField(verbose_name="90度開", default=False,)

    is180Open = models.BooleanField(verbose_name="180度開", default=False,)

    isRemovalDoor = models.BooleanField(verbose_name="取り外し扉", default=False,)

    isMiddlePlateMovable = models.BooleanField(verbose_name="中板可動", default=False,)

    isExposedHandle = models.BooleanField(verbose_name="取手露出", default=True,)

    isPushingHandle = models.BooleanField(verbose_name="取手押込", default=False,)

    isWithKey = models.BooleanField(verbose_name="鍵付", default=True,)

    isHingeIn = models.BooleanField(verbose_name="蝶番内", default=True,)

    isHingeOut = models.BooleanField(verbose_name="蝶番外", default=False,)

    isNamePlateAcrylic = models.BooleanField(verbose_name="銘板：アクリル", default=True,)

    isNamePlateMetaric = models.BooleanField(verbose_name="銘板：金属", default=False,)

    isNamePlateBackLight = models.BooleanField(verbose_name="銘板：背照", default=False,)

    isWithdrawalTop = models.BooleanField(verbose_name="外部引出：上面", default=True,)

    isWithdrawalBottm = models.BooleanField(verbose_name="外部引出：下面", default=True,)

    isWithdrawalLeft = models.BooleanField(verbose_name="外部引出：左側面", default=False,)

    isWithdrawalRight = models.BooleanField(verbose_name="外部引出：右側面", default=False,)

    isWithdrawalFront = models.BooleanField(verbose_name="外部引出：前面", default=False,)

    isWithdrawalBack = models.BooleanField(verbose_name="外部引出：背面", default=False,)

    isHowWithdrawalPlate = models.BooleanField(verbose_name="盲板", default=False,)

    isHowWithdrawalPlateTop = models.BooleanField(verbose_name="上部", default=False,)

    isHowWithdrawalPlateBottom = models.BooleanField(verbose_name="下部", default=False,)

    isHowWithdrawalKnockOut = models.BooleanField(
        verbose_name="ノックアウト穴", default=False,
    )

    isHowWithdrawalMetalConsent = models.BooleanField(
        verbose_name="メタルコンセント", default=False,
    )

    isHowWithdrawalCupring = models.BooleanField(verbose_name="カップリング", default=False,)

    isHowWithdrawalOther = models.BooleanField(verbose_name="その他(無し)", default=False,)

    HowWithdrawalOther = models.TextField(
        verbose_name="その他(無し)：詳細", blank=True, null=True, default="",
    )

    isHowLineTFront = models.BooleanField(verbose_name="配線方法：表面", default=True,)

    isHowLineTBack = models.BooleanField(verbose_name="配線方法：裏面", default=True,)

    isHowLineBundle = models.BooleanField(verbose_name="束", default=False,)

    isHowLineDuct = models.BooleanField(verbose_name="ダクト", default=True,)

    isHowLineCleat = models.BooleanField(verbose_name="クリート", default=False,)

    isHowLineCurl = models.BooleanField(verbose_name="カール", default=False,)

    isHowLineOhter = models.BooleanField(verbose_name="配線方法：その他", default=False,)

    HowLineOhter = models.TextField(
        verbose_name="配線方法：その他：詳細", blank=True, null=True, default="",
    )

    isOutColorSample = models.BooleanField(verbose_name="外装色見本", default=False,)

    isInColorSample = models.BooleanField(verbose_name="内装色見本", default=False,)

    isInstrumentBlack = models.BooleanField(verbose_name="計器枠：黒", default=True,)

    isInstrumentColor = models.BooleanField(verbose_name="計器枠：色見本", default=False,)

    isSwitchBlack = models.BooleanField(verbose_name="開閉器、ハンドル：黒", default=True,)

    isSwitchColor = models.BooleanField(verbose_name="開閉器、ハンドル：色見本", default=False,)

    isSolder = models.BooleanField(verbose_name="ハンダ付", default=True,)

    isCrimpTerminal = models.BooleanField(verbose_name="圧着端子", default=True,)

    isCrimpHawk = models.BooleanField(verbose_name="圧着端子：ホーク型", default=True,)

    isCrimpCircle = models.BooleanField(verbose_name="圧着端子：丸型", default=False,)

    isCrimpPin = models.BooleanField(verbose_name="圧着端子：ピン型", default=False,)

    isCrimpConnectionMethod = models.BooleanField(
        verbose_name="接続方法：その他", default=False,
    )

    crimpConnectionMethod = models.TextField(
        verbose_name="接続方法：その他：詳細", blank=True, null=True, default="",
    )

    isMarkSeal = models.BooleanField(verbose_name="端子：押印", default=True,)

    isMarkSculpture = models.BooleanField(verbose_name="端子：彫刻", default=False,)

    isMarkPrinting = models.BooleanField(verbose_name="端子：焼付", default=False,)

    isMarkOther = models.BooleanField(verbose_name="端子：その他", default=False,)

    markOther = models.TextField(
        verbose_name="端子：その他：詳細", blank=True, null=True, default="",
    )

    mainAcLineColorR = models.CharField(
        verbose_name="R相色", default="赤", blank=True, null=True, max_length=1,
    )

    mainAcLineColorS = models.CharField(
        verbose_name="S相色", default="白", blank=True, null=True, max_length=1,
    )

    mainAcLineColorT = models.CharField(
        verbose_name="T相色", default="青", blank=True, null=True, max_length=1,
    )

    mainDcLineColorP = models.CharField(
        verbose_name="P", default="青", max_length=1, blank=True, null=True,
    )

    mainDcLineColorN = models.CharField(
        verbose_name="N", default="青", max_length=1, blank=True, null=True,
    )

    controlAcLineColorX = models.CharField(
        verbose_name="制御：X", default="黄", blank=True, null=True, max_length=1,
    )

    controlAcLineColorY = models.CharField(
        verbose_name="制御：Y", default="黄", blank=True, null=True, max_length=1,
    )

    controlAcLineColorNonNutral = models.CharField(
        verbose_name="非中性点", default="黒", blank=True, null=True, max_length=1,
    )

    controlDcLineColorP = models.CharField(
        verbose_name="P", default="黒", max_length=1, blank=True, null=True,
    )

    controlDcLineColorN = models.CharField(
        verbose_name="N", default="白", max_length=1, blank=True, null=True,
    )

    groundLineColor = models.CharField(
        verbose_name="接地回路：色", default="緑", blank=True, null=True, max_length=1,
    )

    isGroundEarthDoor = models.BooleanField(verbose_name="扉のアース有無", default=False,)

    mainAcLineCapColorR = models.CharField(
        verbose_name="R相キャップ", default="赤", max_length=1, blank=True, null=True,
    )

    mainAcLineCapColorS = models.CharField(
        verbose_name="S相キャップ", default="白", max_length=1, blank=True, null=True,
    )

    mainAcLineCapColorT = models.CharField(
        verbose_name="T相キャップ", default="青", max_length=1, blank=True, null=True,
    )

    sheldColorR = models.CharField(
        verbose_name="R相シールド", default="赤", max_length=1, blank=True, null=True,
    )

    sheldColorS = models.CharField(
        verbose_name="S相シールド", default="白", max_length=1, blank=True, null=True,
    )

    sheldColorT = models.CharField(
        verbose_name="T相シールド", default="青", max_length=1, blank=True, null=True,
    )

    isInsulationResistance = models.BooleanField(verbose_name="絶縁抵抗", default=False,)

    InsulationResistance = models.IntegerField(
        verbose_name="絶縁抵抗：試験値", default=5, blank=True, null=True,
    )

    remarks = models.TextField(verbose_name="特記事項", default="", blank=True, null=True,)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.productNumber)


class Inspection(models.Model):
    orderNumber = models.ForeignKey(
        "Order",
        to_field="id",
        verbose_name="オーダーNo.",
        null=True,
        on_delete=models.SET_NULL,
    )

    subject = models.ForeignKey(
        "Order",
        related_name="Ins_subject",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="件名",
    )

    name = models.ForeignKey(
        "Product",
        to_field="id",
        verbose_name="製品名",
        null=True,
        on_delete=models.SET_NULL,
    )

    serialNumber = models.CharField(
        blank=True,
        null=True,
        verbose_name="製品番号",
        default="0000S-00000",
        max_length=11,
    )

    testDate = models.DateTimeField(blank=True, null=True,)
    chechDate = models.DateTimeField(blank=True, null=True,)

    wintnessed = models.TextField(blank=True, null=True, verbose_name="立合者")

    approver = models.ForeignKey(
        "Employee",
        to_field="id",
        related_name="aEmployee_id",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="承認",
    )

    reviewer = models.ForeignKey(
        "Employee",
        to_field="id",
        related_name="rEmployee_id",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="照査",
    )

    practitioner = models.ForeignKey(
        "Employee",
        to_field="id",
        related_name="pEmployee_id",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="実施",
    )

    isParts = models.BooleanField(verbose_name="納入数量検査", default=False,)

    isOuter = models.BooleanField(verbose_name="外観検査", default=False,)

    isConstruction = models.BooleanField(verbose_name="構造検査", default=False,)

    isSize = models.BooleanField(verbose_name="寸法検査", default=False,)

    isPainting = models.BooleanField(verbose_name="塗装検査", default=False,)

    isThickness = models.BooleanField(verbose_name="膜厚検査", default=False,)

    isNamePlate = models.BooleanField(verbose_name="名板検査", default=False,)

    isTag = models.BooleanField(verbose_name="計器検査", default=False,)

    isTerminal = models.BooleanField(verbose_name="端子配列検査", default=False,)

    isWiring = models.BooleanField(verbose_name="配線検査", default=False,)

    isSequence = models.BooleanField(verbose_name="シーケンス検査", default=False,)

    isMegger = models.BooleanField(verbose_name="絶縁抵抗検査", default=False,)

    isPressure = models.BooleanField(verbose_name="絶縁体圧検査", default=False,)

    isLoop = models.BooleanField(verbose_name="ループ検査", default=False,)

    isAir = models.BooleanField(verbose_name="配管検査", default=False,)

    isPurge = models.BooleanField(verbose_name="エアーパージ検査", default=False,)

    drawingNo1 = models.TextField(blank=True, null=True)
    drawingNo2 = models.TextField(blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.orderNumber


class MainCorrectHistory(models.Model):
    orderNumber = models.ForeignKey(
        "Order",
        to_field="id",
        verbose_name="オーダーNo.",
        null=True,
        on_delete=models.SET_NULL,
    )

    corrector = models.ForeignKey(
        "Employee",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="訂正者",
    )

    correct_date = models.DateTimeField(default=timezone.now)

    comment = models.TextField(blank=True, null=True, verbose_name="タイトルコメント")

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.orderNumber)


class SubCorrectHistory(models.Model):
    mainhistory = models.ForeignKey(
        "MainCorrectHistory",
        to_field="id",
        verbose_name="メイン履歴",
        null=True,
        on_delete=models.SET_NULL,
    )

    corrector = models.ForeignKey(
        "Employee",
        to_field="id",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="訂正者",
    )

    revision = models.CharField(default=0, max_length=10, verbose_name="revision")

    comment = models.TextField(blank=True, null=True, verbose_name="コメント")

    do_date = models.DateTimeField(default=timezone.now)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.mainhistory)


class Drawing(models.Model):
    orderNumber = models.ForeignKey(
        "Order",
        to_field="id",
        verbose_name="オーダーNo.",
        null=True,
        on_delete=models.SET_NULL,
    )

    drawingNumber = models.TextField(verbose_name="ページ番号", default="",)

    pages = models.CharField(default=0, max_length=100, verbose_name="ページ番号")

    drawType = models.ForeignKey(
        "DrawingType",
        to_field="id",
        verbose_name="図面種類.",
        null=True,
        on_delete=models.SET_NULL,
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.orderNumber


class DrawingType(models.Model):
    type = models.TextField(verbose_name="図面種類")

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type

