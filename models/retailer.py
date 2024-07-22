from init import db, ma 
from marshmallow import fields

class Retailer(db.Model):
    __tablename__ = "retailers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)

    #sizechart_id = db.Column(db.Integer,db.ForeignKey("sizechart.id")) #foreign key

    #sizecharts = db.relationship('Card',back_populates="retailers") 

class RetailerSchema(ma.Schema):
    #sizechart = fields.Nested('SizeChartSchema')
    class Meta:
        fields = ("id","name","date","sizechart")

retailer_schema= RetailerSchema()
retailers_schema = RetailerSchema(many=True)

#class Size Chart(db.Model):
# __tablename__ = 'size charts'
# id = db.Column(db.Integer, primary_key=True)
# sizes ...    
