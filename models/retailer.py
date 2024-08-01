from marshmallow import Schema,fields
from init import db, ma 

class Size(db.Model):
    __tablename__ = "sizes"

    # primary key 
    id = db.Column(db.Integer, primary_key=True)

    # attributes 
    name = db.Column(db.String)
    waist_measurement = db.Column(db.String)
    hip_measurement = db.Column(db.String)
    bust_measurement = db.Column(db.String)
    
    # foreign key 
    sizechart_id = db.Column(db.Integer, db.ForeignKey("size_charts.id"))

    # relationships 
    size_chart = db.relationship("SizeChart",back_populates ="sizes")

class SizeSchema(ma.Schema):
    class Meta:
        fields = ("id","name","waist_measurement","hip_measurement","bust_measurement","sizechart_id")

size_schema = SizeSchema()
sizes_schema = SizeSchema(many=True)


class SizeChart(db.Model):
    __tablename__ = "size_charts"

    # primary key 
    id = db.Column(db.Integer, primary_key=True)

    # foreign key 
    retailer_id = db.Column(db.Integer,db.ForeignKey("retailers.id"))

    #relationships 
    sizes = db.relationship("Size",back_populates="size_chart",lazy="dynamic")
    retailers = db.relationship("Retailer",back_populates="size_chart") 


class SizeChartSchema(ma.Schema):
    class Meta:
        fields = ("id","retailer_id")

sizechart_schema = SizeChartSchema()
sizecharts_schema = SizeChartSchema(many=True)

class Retailer(db.Model):
    __tablename__ = "retailers"

    # primary key  
    id = db.Column(db.Integer, primary_key=True)

    # attributes 
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date)
    
    # relationships 
    size_chart = db.relationship("SizeChart",back_populates="retailers")

class RetailerSchema(ma.Schema):
    class Meta:
        fields = ("id","name","date")

retailer_schema = RetailerSchema()
retailers_schema = RetailerSchema(many=True)




