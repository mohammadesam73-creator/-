# الكلاس الأساسي GenericDevice
class GenericDevice:

    def __init__(self, name="Device"):
        self.name = name


# 1. إنشاء كلاس Camera يرث من GenericDevice
class Camera(GenericDevice):

    def __init__(self, name, ip_address):
        super().__init__(name)
        # 2. إضافة خاصية محمية (private) باستخدام شرطتين سفليتين (__)
        self.__ip_address = ip_address

    # 3. إنشاء دالة ()get_ip لطباعة الـ IP بطريقة آمنة
    def get_ip(self):
        print(f"Secure IP Address: {self.__ip_address}")
        return self.__ip_address


# --- تجربة وتشغيل الكود ---
if __name__ == "__main__":
    # إنشاء كائن من الكلاس Camera
    my_camera = Camera("Front-Door-Cam", "192.168.1.101")

    # استدعاء الدالة لطباعة الـ IP بأمان
    my_camera.get_ip()