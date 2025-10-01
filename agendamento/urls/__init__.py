from .clientes_url import urlpatterns as cliente_urls
from .agendamentos_url import urlpatterns as agendamento_urls


urlpatterns = cliente_urls + agendamento_urls