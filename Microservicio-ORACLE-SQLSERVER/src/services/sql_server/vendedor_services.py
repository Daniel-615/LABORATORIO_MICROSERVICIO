class VendedorServices:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def getDb(self):
        return self.db

    def post_vendedor(self, nombre):
        db = self.getDb()
        models = self.models
        try:
            # Crear nueva instancia de VENDEDOR
            nuevo_vendedor = models.VENDEDOR(nombre=nombre)
            db.session.add(nuevo_vendedor)
            db.session.commit()
            return {"message": "Vendedor creado correctamente.", "id": nuevo_vendedor.id}, 201
        except Exception as e:
            db.session.rollback()
            print("Error en post_vendedor:", e)
            return {"error": "Ocurrió un error al insertar en vendedor"}, 500

    def get_vendedores(self):
        db = self.getDb()
        models = self.models
        try:
            vendedores = db.session.query(models.VENDEDOR).all()
            return [vendedor.to_dict() for vendedor in vendedores], 200
        except Exception as e:
            print("Error en get_vendedores:", e)
            return {"error": "Ocurrió un error al obtener los vendedores"}, 500

    def get_vendedor(self, id):
        db = self.getDb()
        models = self.models
        try:
            vendedor = db.session.query(models.VENDEDOR).filter_by(id=id).first()
            if not vendedor:
                return {"error": f"Vendedor con id {id} no encontrado."}, 404
            return vendedor.to_dict(), 200
        except Exception as e:
            print("Error en get_vendedor:", e)
            return {"error": "Ocurrió un error al obtener el vendedor"}, 500

    def put_vendedor(self, id, nombre):
        db = self.getDb()
        models = self.models
        try:
            vendedor = db.session.query(models.VENDEDOR).filter_by(id=id).first()
            if not vendedor:
                return {"error": f"Vendedor con id {id} no encontrado."}, 404
            vendedor.nombre = nombre
            db.session.commit()
            return {"message": "Vendedor actualizado correctamente."}, 200
        except Exception as e:
            db.session.rollback()
            print("Error en put_vendedor:", e)
            return {"error": "Ocurrió un error al actualizar el vendedor"}, 500
