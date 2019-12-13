class Image:
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print(f'loading {self._filename}')

    def display_image(self):
        print(f'display {self._filename}')


class Proxy:
    def __init__(self, subject: Image):
        self._subject = subject
        self._proxystate = None


class ProxyImage(Proxy):
    def display_image(self):
        if self._proxystate is None:
            self._subject.load_image_from_disk()
            self._proxystate = 1
        print(f'display {self._subject._filename}')


if __name__ == '__main__':
   proxy_image1 = ProxyImage(Image('Hires_10Mb_Photo1'))
   proxy_image2 = ProxyImage(Image('Hires_10Mb_Photo2'))

   proxy_image1.display_image()
   proxy_image1.display_image()
   proxy_image2.display_image()
   proxy_image2.display_image()
   proxy_image1.display_image()
