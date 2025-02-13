class Database:
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Database, cls).__new__(cls)
    return cls.instance

singleton = Database()
new_singleton = Database()

print(singleton is new_singleton)