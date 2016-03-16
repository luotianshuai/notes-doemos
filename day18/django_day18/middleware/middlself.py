
class Mmm(object):
    def process_request(self,request):
        print 'Mmm - process_request'

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print 'Mmm - process_view'


    def process_response(self, request, response):
        print 'Mmm - process_response'
        return response


    def process_exception(self, request, exception):
        #print 'Mmm - process_exception'
        pass



class Xxx(object):
    def process_request(self,request):
        print 'Xxx - process_request'

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print 'Xxx - process_view'


    def process_response(self, request, response):
        print 'Xxx - process_response'
        return response


    def process_exception(self, request, exception):
        #print 'Mmm - process_exception'
        pass

