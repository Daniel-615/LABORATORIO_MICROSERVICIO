class ProductoServices:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def getDb(self):
        return self.db

    def post_producto(self, nombre,  stock):
        db = self.getDb()
        models = self.models
        try:
            # Crear nueva instancia de PRODUCTO
            nuevo_producto = models.PRODUCTO(
                nombre=nombre,
                stock=stock
            )
            db.session.add(nuevo_producto)
            db.session.commit()
            return {"message": "Producto creado correctamente.", "id": nuevo_producto.id}, 201
        except Exception as e:
            db.session.rollback()
            print("Error en post_producto:", e)
            return {"error": "Ocurrió un error al insertar el producto"}, 500

    def get_productos(self):
        db = self.getDb()
        models = self.models
        try:
            productos = db.session.query(models.PRODUCTO).all()
            return [producto.to_dict() for producto in productos], 200
        except Exception as e:
            print("Error en get_productos:", e)
            return {"error": "Ocurrió un error al obtener los productos"}, 500

    def get_producto(self, id):
        db = self.getDb()
        models = self.models
        try:
            producto = db.session.query(models.PRODUCTO).filter_by(id=id).first()
            if not producto:
                return {"error": f"Producto con id {id} no encontrado."}, 404
            return producto.to_dict(), 200
        except Exception as e:
            print("Error en get_producto:", e)
            return {"error": "Ocurrió un error al obtener el producto"}, 500

    def put_producto(self, id, stock):
        db = self.getDb()
        models = self.models
        try:
            producto = db.session.query(models.PRODUCTO).filter_by(id=id).first()
            if not producto:
                return {"error": f"Producto con id {id} no encontrado."}, 404

            producto.stock = stock
            db.session.commit()
            return {"message": "Producto actualizado correctamente."}, 200
        except Exception as e:
            db.session.rollback()
            print("Error en put_producto:", e)
            return {"error": "Ocurrió un error al actualizar el producto"}, 500
