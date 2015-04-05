# Create your views here.
from collections import OrderedDict

from django.templatetags.static import static
from django.views.generic.base import TemplateView

from jeslee_web.fashion_show.views import UpcomingFashionShowMixin
from jeslee_web.utils import string_utils
from jeslee_web.utils.views import JSONResponseMixin


class HomeView(UpcomingFashionShowMixin, TemplateView):
    pass


class HowToTakeMeasuresView(TemplateView):

    ENCODE_KEY = 'pelikaan'
    ID_SEPARATOR = ','

    MEASURE_WAIST = 'W'
    MEASURE_CHESTSIZE = 'CS'
    MEASURE_FRONT_WAIST_LENGTH = 'FWL'
    MEASURE_SHOULDER_WIDTH = 'SW'
    MEASURE_LONG_SKIRT_LENGTH = 'LSL'
    MEASURE_TOTAL_LENGTH_FRONT = 'TLF'
    MEASURE_BACK_LENGTH = 'BL'
    MEASURE_SLEEVE_LENGTH = 'SL'
    MEASURE_UPPER_ARM_WIDTH = 'UAW'
    MEASURE_WRIST_WIDTH = 'WW'
    MEASURE_NECK_SET = 'NS'
    MEASURE_BETWEEN_LEG_LENGTH = 'BLL'

    MEASURES = OrderedDict([
        (MEASURE_WAIST, {
            'title': 'Taillewijdte',
            'image': static('gfx/photos/maten_nemen/taillewijdte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/taillewijdte_300x400.jpg'),
            'explanation_text': 'meet deze rondom de taille'
        }),
        (MEASURE_CHESTSIZE, {
            'title': 'Bovenwijdte',
            'image': static('gfx/photos/maten_nemen/bovenwijdte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/bovenwijdte_300x400.jpg'),
            'explanation_text': 'meet deze rondom het lijfje onder de oksels',
        }),
        (MEASURE_FRONT_WAIST_LENGTH, {
            'title': 'Voortaillelengte',
            'image': static('gfx/photos/maten_nemen/voortaillelengte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/voortaillelengte_300x400.jpg'),
            'explanation_text': 'meet deze vanaf de halsaanzet tot de taille',
        }),
        (MEASURE_SHOULDER_WIDTH, {
            'title': 'Schouderbreedte',
            'image': static('gfx/photos/maten_nemen/schouderbreedte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/schouderbreedte_300x400.jpg'),
            'explanation_text': 'meet deze van schouder tot schouder',
        }),
        (MEASURE_LONG_SKIRT_LENGTH, {
            'title': 'Lange Rok lengte',
            'image': static('gfx/photos/maten_nemen/lange_rok_lengte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/lange_rok_lengte_300x400.jpg'),
            'explanation_text': 'meet deze vanaf de taille tot aan de grond',
        }),
        (MEASURE_TOTAL_LENGTH_FRONT, {
            'title': 'Totale voorlengte',
            'image': static('gfx/photos/maten_nemen/totale_voorlengte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/totale_voorlengte_300x400.jpg'),
            'explanation_text': 'meet deze vanaf de halsaanzet tot aan de grond',
        }),
        (MEASURE_NECK_SET, {
            'title': 'Halsaanzet',
            'image': static('gfx/photos/maten_nemen/halsaanzet.jpg'),
            'thumb': static('gfx/photos/maten_nemen/halsaanzet_300x400.jpg'),
            'explanation_text': 'is het punt tussen de hals en de schouder'
        }),
        (MEASURE_BACK_LENGTH, {
            'title': 'Ruglengte',
            'image': static('gfx/photos/maten_nemen/ruglengte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/ruglengte_300x400.jpg'),
            'explanation_text': 'meet deze vanaf de halsknobbel tot aan de taillelijn',
        }),
        (MEASURE_SLEEVE_LENGTH, {
            'title': 'Mouwlengte',
            'image': static('gfx/photos/maten_nemen/mouwlengte_2.jpg'),
            'thumb': static('gfx/photos/maten_nemen/mouwlengte_2_300x400.jpg'),
            'explanation_text': 'meet deze vanaf het schouderpunt tot aan het polsgewricht'
        }),
        (MEASURE_UPPER_ARM_WIDTH, {
            'title': 'Bovenarmwijdte',
            'image': static('gfx/photos/maten_nemen/bovenarmwijdte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/bovenarmwijdte_300x400.jpg'),
            'explanation_text': 'meet deze rondom de bovenarm'
        }),
        (MEASURE_WRIST_WIDTH, {
            'title': 'Polswijdte',
            'image': static('gfx/photos/maten_nemen/polswijdte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/polswijdte_300x400.jpg'),
            'explanation_text': 'meet deze rondom het polsgewricht'
        }),
        (MEASURE_BETWEEN_LEG_LENGTH, {
            'title': 'Tussenbeenlengte',
            'image': static('gfx/photos/maten_nemen/tussenbeenlengte.jpg'),
            'thumb': static('gfx/photos/maten_nemen/tussenbeenlengte_300x400.jpg'),
            'explanation_text': 'meet deze van het kruis tot de grond',
        }),
        ]
    )

    def get_context_data(self, **kwargs):
        context_data = super(HowToTakeMeasuresView, self).get_context_data(**kwargs)
        encoded_measures = kwargs.get('encoded_measures', None)
        if encoded_measures:
            # find the measure in the hash and return them
            measures_ids = string_utils.decode(self.ENCODE_KEY, str(encoded_measures))
            measures_to_show = OrderedDict()
            for m_id in measures_ids.split(self.ID_SEPARATOR):
                measures_to_show.update({m_id: self.MEASURES[m_id]})
        else:
            # no encoded_measures found return all
            measures_to_show = self.MEASURES

        context_data['measures'] = measures_to_show
        return context_data


class GetMeasureUrl(JSONResponseMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context_data = {}
        # check request for measure id's to be encoded
        measure_ids = self.request.GET.getlist('m')
        if measure_ids:
            # found some measure ids, encode them in a string and place it in the context
            measure_ids_str = HowToTakeMeasuresView.ID_SEPARATOR.join(measure_ids)
            context_data['url'] = string_utils.encode(HowToTakeMeasuresView.ENCODE_KEY, measure_ids_str)
        return context_data
