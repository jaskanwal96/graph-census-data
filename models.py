import mongoengine

class adults(mongoengine.Document):
    # Table to add Adults from the census
    
    _id = mongoengine.IntField()
    age = mongoengine.IntField()
    workclass = mongoengine.StringField()
    fnlgwt = mongoengine.IntField()
    
    education = mongoengine.StringField()
    education_num = mongoengine.IntField()
    martial_status = mongoengine.StringField()
    
    occupation = mongoengine.StringField()
    relationship = mongoengine.StringField()
    race = mongoengine.StringField()
    sex = mongoengine.StringField()
    capital_gain = mongoengine.IntField()
    
    capital_loss = mongoengine.IntField()
    hours_per_week = mongoengine.IntField()
    native_country = mongoengine.StringField()
    salary = mongoengine.StringField()



