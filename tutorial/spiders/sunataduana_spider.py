import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class SunataduanaSpider(scrapy.Spider):
    name = "sunataduana"
    consultaAgenteAduana = 'http://www.aduanet.gob.pe/cl-ad-consdepa/ConsImpoIAServlet?accion=cargarConsulta&tipoConsulta=2'
    formConsultaUrl = 'http://www.aduanet.gob.pe/cl-ad-consdepa/ConsImpoIAServlet'
    start_urls = [consultaAgenteAduana]


    def parse(self, response):
        #open_in_browser(response)
        self.log('response1 headers: ' + str(response.request.headers))
        filename = 'consultaForm.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        data = {
            'accion' : 'consultarImportador',
            'detalle' : '',
            'description' : '',
            'vig001278' : 'F',
            'tipoDocum' : '',
            'tipoConsulta' : '2',
            'fec_inicio' : '06/11/2018',
            'fec_fin' : '16/11/2018',
            'criterio' : '5681',
            'grupo' : '4',
            'codgrupo' : '118',
            'orden' : 'fob',
            'donacion' : '1',
        }

        yield scrapy.FormRequest(url=self.formConsultaUrl, formdata=data, callback=self.parse_postForm)

    def parse_postForm(self, response):
        self.log('response2 headers: ' + str(response.request.headers))
        #open_in_browser(response)
        filename = 'postForm.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)