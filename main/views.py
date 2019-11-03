# Create your views here.
import logging
from django.http.response import HttpResponse

logger = logging.getLogger(__name__)
def top(request):
    logger.info('test')
    return HttpResponse('hello world')