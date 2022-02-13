import django_filters
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io.fits import Header
from depot.models import FF, FFHeader
from astropy.wcs import WCS


class PositionFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(method='position_filter', )

    class Meta:
        model = FF
        fields = ['position', ]

    # noinspection PyMethodMayBeStatic
    def position_filter(self, queryset, name, value):
        c = SkyCoord(value, frame='icrs', unit=(u.deg, u.deg))
        # TODO first run filter
        found_ff = []
        for ff in FFHeader.objects.all():
            wcs = WCS(Header.fromstring(ff.full_header))
            if wcs.footprint_contains(c):
                found_ff.append(ff.id)

        return FF.objects.filter(id__in=found_ff)
