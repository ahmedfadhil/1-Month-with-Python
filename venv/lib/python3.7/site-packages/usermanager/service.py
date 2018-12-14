import logging

from bn import AttributeDict
from pipestack.ensure import ensure_function_bag

log = logging.getLogger(__name__)

class ProxyingAttributeDict(AttributeDict):
    def __init__(self, flow, module, oself, *k, **p):
        self['module'] = module
        self['flow'] = flow
        self['oself'] = oself
        #AttributeDict.__init__(self, *k, **p)

    def __getattr__(self, name):
        if hasattr(self['module'], name):
            def func(*k, **p):
                if not self['flow'].has_key(self['oself'].connection_name):
                    raise Exception(
                        'The %rservice has not been started'%(
                            self['oself'].connection_name
                        )
                    )
                return getattr(self['module'], name)(self['flow'], *k, **p)
            return func
        elif hasattr(self['oself'], name):
            return self['oself'].__dict__[name]
        else:
            raise AttributeError('No such attribute %r'%name)

class Self(object):
    pass

def userService(module, connection_name='database', encrypt=None):
    def userService_constructor(service, name, aliases=None, *k, **p):
        @ensure_function_bag(connection_name)
        def enter(flow):
            oself = Self()
            oself.connection_name = connection_name
            flow[name] = ProxyingAttributeDict(flow, module, oself)
        return AttributeDict(start=enter, enter=enter)
    return userService_constructor
    
def postgresqlUserService(*k, **p):
    import usermanager.driver.postgresql
    return userService(usermanager.driver.postgresql, *k, **p)

