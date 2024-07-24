from init import db, ma 
from marshmallow import fields

class Size(db.Model):
    __tablename__ = "sizes"

    # primary key 
    id = db.Column(db.Integer, primary_key=True)

    # foreign key 
    #sizechart_id = db.Column(db.Integer, db.ForeignKey("size_charts.id"))

    # attributes 
    name = db.Column(db.String)
    bust_measurement = db.Column(db.String)
    waist_measurement = db.Column(db.String)
    hip_measurement = db.Column(db.String)

    # relationships 
    #size_charts = db.relationship("SizeChart",back_populates ="sizes")

class SizeSchema(ma.Schema):
    class Meta:
        fields = ("id","name","bust_measurement","waist_measurement","hip_measurement")

size_schema = SizeSchema()
sizes_schema = SizeSchema(many=True)


#class SizeChart(db.Model):
    #__tablename__ = "size_charts"

    # primary key 
    #id = db.Column(db.Integer, primary_key=True)

    # foreign key 
    #size_id = db.Column(db.Integer,db.ForeignKey("sizes.id"))

    #relationships 
    #sizes = db.relationship("Size",back_populates="size_chart",lazy="dynamic")


#class SizeChartSchema(ma.Schema):
    #class Meta:
        #fields = ("id","size_id")

#sizechart_schema = SizeChartSchema()
#sizecharts_schema = SizeChartSchema(many=True)

#class Retailer(db.Model):
    #__tablename__ = "retailers"

    # primary key  
    #id = db.Column(db.Integer, primary_key=True)

    # foreign key 
    #sizechart_id = db.Column(db.Integer,db.ForeignKey("size_charts.id"))

    # attributes 
    #name = db.Column(db.String(80), unique=True, nullable=False)
    #date = db.Column(db.Date)
    

    # relationships 
    #sizechart = db.relationship("SizeChart",back_populates="retailer",lazy="dynamic")

#class RetailerSchema(ma.Schema):
    #class Meta:
        #fields = ("id","name","date","sizechart_id")

#retailer_schema = RetailerSchema()
#retailers_schema = RetailerSchema(many=True)




