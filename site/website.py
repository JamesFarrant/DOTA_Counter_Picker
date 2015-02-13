import cherrypy
import team_picker 
import json

class HelloWorld(object):
    def get_counters(self,enemies,form):
        counters = json.loads(enemies,form)
        return json.dumps(team_picker.counter_team(counters,form))
    get_counters.exposed = True


cherrypy.quickstart(HelloWorld(),config='cherrypy.config')
#cherrypy.config.update('cherrypy.config')

