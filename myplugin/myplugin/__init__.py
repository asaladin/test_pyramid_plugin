from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route("wiki", "/wiki")
    config.scan()
    return config.make_wsgi_app()

    
def includeme(config):
    settings = config.get_settings()
    import Config
    Config.glob_wikipath = settings['basewikitemplate']
    print "in includeme:", id(Config.glob_wikipath), Config.glob_wikipath
    
    config.add_route("wiki", "/wiki")
    config.scan()