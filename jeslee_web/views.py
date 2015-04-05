# Create your views here.
from collections import OrderedDict

from django.templatetags.static import static
from django.views.generic.base import TemplateView

from jeslee_web.fashion_show.views import UpcomingFashionShowMixin


class HomeView(UpcomingFashionShowMixin, TemplateView):
    pass


class HowToTakeMeasuresView(TemplateView):

    MEASURE_WAIST = 'WAIST'
    MEASURE_CHESTSIZE = 'CHESTSIZE'
    MEASURE_FRONT_WAIST_LENGTH = 'FRONT_WAIST_LENGTH'
    MEASURE_SHOULDER_WIDTH = 'SHOULDER_WIDTH'
    MEASURE_LONG_SKIRT_LENGTH = 'LONG_SKIRT_LENGTH'
    MEASURE_TOTAL_LENGTH_FRONT = 'TOTAL_LENGTH_FRONT'
    MEASURE_BACK_LENGTH = 'BACK_LENGTH'
    MEASURE_SLEEVE_LENGTH = 'SLEEVE_LENGTH'
    MEASURE_UPPER_ARM_WIDTH = 'UPPER_ARM_WIDTH'
    MEASURE_WRIST_WIDTH = 'WRIST_WIDTH'
    MEASURE_NECK_SET = 'NECK_SET'
    MEASURE_BETWEEN_LEG_LENGTH = 'BETWEEN_LEG_LENGTH'

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
        context_data['measures'] = self.MEASURES
        return context_data




