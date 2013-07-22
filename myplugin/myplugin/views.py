from pyramid.view import view_config


from pyramid.renderers import render_to_response

import Config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    
    return {'project': 'myplugin'}

#@view_config(route_name="wiki")    
#def wiki(request):
    ##return render_to_response( "basepyramid:templates/wiki.mako",
    #return render_to_response( request.registry.settings['basewikitemplate'],
                              #{'wikicontent':"this is a basic wiki content", 'bar':2},
                              #request=request)
                              
@view_config(route_name="wiki", renderer=Config.glob_wikipath)    
def wiki(request):
    #return render_to_response( "basepyramid:templates/wiki.mako",
    print "in wiki: ", id(Config.glob_wikipath), Config.glob_wikipath
    return  {'wikicontent':"this is a basic wiki content", 'bar':2}

                              
