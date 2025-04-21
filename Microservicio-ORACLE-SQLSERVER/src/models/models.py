class Models:
    def __init__(self,db):
        self.db=db
        
        """ SQL Server Tables
        """
        class FACTURACION(db.Model):
            __tablename__='FACTURACION'
            __table_args__={'extend_existing':True}
            
            cae=db.Column(db.String(255),nullable=False,primary_key=True)
            nit_clte=db.Column(db.Integer,nullable=False)
            fecha_hora_certificado=db.Column(db.DateTime,nullable=False)
            fecha_hora_validacion=db.Column(db.DateTime,nullable=False)
            id_vendedor=db.Column(db.ForeignKey('VENDEDOR.id'),nullable=False)
            def to_dict(self):
                return {
                    'nit_clte': self.nit_clte,
                    'cae': self.cae,
                    "fecha_hora_certificado": self.fecha_hora_certificado,
                    "fecha_hora_validacion": self.fecha_hora_validacion,
                    'id_vendedor': self.id_vendedor
                }
        self.FACTURACION=FACTURACION    
        class VENDEDOR(db.Model):
            __tablename__='VENDEDOR'
            __table_args__={'extend_existing':True}
            id=db.Column(db.Integer,primary_key=True,autoincrement=True)
            nombre=db.Column(db.String(255),nullable=False)
            def to_dict(self):
                return {
                    'id': self.id,
                    'nombre': self.nombre
                }
        self.VENDEDOR=VENDEDOR

        """ Oracle Tables
        """
        
     
        class FACTURA_DETALLE(db.Model):
            __bind_key__='oracle'
            __tablename__='FACTURA_DETALLE'
            __table_args__={'extend_existing':True}
            id=db.Column(db.Integer,primary_key=True)
            cae = db.Column(db.String(255), nullable=False) 
            id_producto=db.Column(db.Integer,db.ForeignKey('PRODUCTO.id'),nullable=False)
            cantidad=db.Column(db.Integer,nullable=False)
            precio=db.Column(db.Float,nullable=False)
            descuento=db.Column(db.Float,nullable=False)
            def to_dict(self):
                return {
                    'id': self.id
                }
        self.FACTURA_DETALLE=FACTURA_DETALLE
        class PRODUCTO(db.Model):
            __bind_key__='oracle'
            __tablename__='PRODUCTO'
            __table_args__={'extend_existing':True}
            id=db.Column(db.Integer,primary_key=True)
            nombre=db.Column(db.String(255),nullable=False)
            stock=db.Column(db.Integer,nullable=False)
            def to_dict(self):
                return {
                    'id': self.id,
                    'nombre': self.nombre
                }
        self.PRODUCTO=PRODUCTO