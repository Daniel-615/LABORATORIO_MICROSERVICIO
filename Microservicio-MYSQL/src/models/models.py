class Models:
    def __init__(self,db):
        self.db=db
        class CERTIFICADO_FACTURA(db.Model):
            __tablename__='CERTIFICADO_FACTURA'
            __table_args__={'extend_existing':True}
            id=db.Column(db.Integer,primary_key=True,autoincrement=True)
            cae=db.Column(db.String(255))
            certificado=db.Column(db.Text)
            factura=db.Column(db.Text)
            def to_dict(self):
                return {
                    'id': self.id,
                    'cae': self.cae
                }
        self.CERTIFICADO_FACTURA=CERTIFICADO_FACTURA