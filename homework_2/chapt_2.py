class DataCache:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        if len(self.storage) < 5:
            self.storage.append(value)
        else:
            print("Кэш переполнен. Очистка...")
            self.storage = []

    def fetch(self):
        if not self.storage:
            print("Кэш пуст. Нет данных для вывода.")
        else:
            print("Содержимое кэша:", self.storage)


cache = DataCache()

cache.insert("test1")
cache.insert("example")
cache.insert(42)
cache.insert("sample")
cache.insert(True)
cache.insert([1, 2, 3])  
cache.insert(99)
cache.fetch()  
