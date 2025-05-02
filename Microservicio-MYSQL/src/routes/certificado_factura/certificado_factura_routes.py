from flask import request,jsonify
class CertificadoFacturaRoutes:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/certificado',methods=['POST'])
        def post_certificado():
            data=request.get_json()
            return self.app_initializer.getControllers().post_certificado(data)
        @self.app.route('/v1/certificados',methods=['GET'])
        def get_certificados():
            return self.app_initializer.getControllers().get_certificados()
        @self.app.route('/v1/certificado/<int:id>',methods=['PUT'])
        def put_ciudad(id):
            data=request.get_json()
            return self.app_initializer.getControllers().put_certificado(id,data)
        @self.app.route('/v1/certificado/<int:id>',methods=['GET'])
        def get_certificado_id(id):
            return self.app_initializer.getControllers().get_certificado_id(id)