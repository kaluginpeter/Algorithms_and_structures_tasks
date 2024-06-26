# Задача «Шифровка ссылок»
# Марсоход ежедневно получает из Центра управления ссылки, по которым он скачивает информацию,
# необходимую в повседневной работе.
# Ссылки могут быть совершенно разными по структуре, например такими:
# https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html
# …такими:
# https://tsup.ru/impunity/01092023/whats_new/
# …или даже такими:
# https://mars-program.ru/all/010923/plan_B.htm
# Злоумышленники и марсиане пытаются получить доступ к информации, предназначенной для марсохода.
# Для защиты данных было решено передавать ссылки в зашифрованном виде, чтобы никто не догадался.

# Напишите программу, которая будет шифровать ссылки.
# Любая переданная в программу ссылка должна быть преобразована в ссылку вида https://ma.rs/<hash>,
# где <hash> — изменяемая часть, которая может включать английские буквы любого регистра и цифры.
# Например, ссылка https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html может быть преобразована
# в ссылку вида https://ma.rs/X7NYIol.
# Количество символов после префикса https://ma.rs/ может быть любым.
# Реализуйте класс MarsURLEncoder, который будет зашифровывать и расшифровывать ссылки.
# В классе должно быть два метода:
# метод encode() должен получать на вход исходные ссылки и возвращать зашифрованные, вида https://ma.rs/<hash>;
# метод decode() должен принимать зашифрованную ссылку и возвращать исходную.
# Пары «зашифрованная ссылка» + «исходная ссылка» должны храниться в словаре.
# В конструкторе класса __init__(...) создайте атрибут — хранилище ссылок. Это должен быть словарь, в котором
# ключ — это сгенерированная зашифрованная ссылка
# значение — исходная ссылка
# Например, если ссылка https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html преобразована в
# https://ma.rs/X7NYIol, то в словарь должен быть добавлен такой элемент:
# {
#     ...,
#     'https://ma.rs/X7NYIol': 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
# }
# Ключом словаря-хранилища может быть не вся зашифрованная ссылка, а только её хеш-фрагмент:
# {
#     ...,
#     'X7NYIol': 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
# }
# Выбор варианта — за вами.
# К изменяющейся части зашифрованной ссылки особых требований нет — там может быть написана
# любая последовательность букв и цифр. Важно, чтобы по зашифрованной ссылке можно было восстановить исходную.
# Solution
class MarsURLEncoder:

    def __init__(self):
        self.storage_encoded: dict[str, str] = dict()
        self.storage_decoded: dict[str, str] = dict()

    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL.
        Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol.
        """
        if long_url in self.storage_encoded:
            return self.storage_encoded.get(long_url)
        decoded_url: str = 'https://ma.rs/' + str(abs(hash(long_url)))
        while decoded_url in self.storage_decoded:
            decoded_url = 'https://ma.rs/' + str(abs(hash(long_url)))
        self.storage_encoded[long_url] = decoded_url
        self.storage_decoded[decoded_url] = long_url
        return decoded_url

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL.
        Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную.
        """
        return self.storage_decoded.get(short_url)