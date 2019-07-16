from peewee import *

db = SqliteDatabase('./weather.db')

class BaseModel(Model):
	class Meta:
		database = db
	

class Weather(BaseModel):
	city = CharField()
	date = DateField()
	temp = CharField()
	desc = CharField()
	humdity = CharField()
	sunrise = DateTimeField()
	sunset = DateTimeField()

	class Meta:
		db_table = 'weather'


try:
	db.connect()
	Weather.create_table()
except InternalError as px:
	print(str(px))