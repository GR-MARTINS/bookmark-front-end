from app.controllers.site import site as bp_site


def init_app(app):
    app.register_blueprint(bp_site)
