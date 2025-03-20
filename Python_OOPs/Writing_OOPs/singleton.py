class Database:
  '''Single instance to be created by database class to maintain integrity'''
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Database, cls).__new__(cls)
    return cls.instance

db1 = Database()
db2 = Database()

print(db1)
print(db2)