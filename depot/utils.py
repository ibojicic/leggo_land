import os
import uuid

from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from django.http import HttpResponseRedirect
from django.urls import reverse

from depot.models import FFUpload, FF, FFHeader
from leggo_builder_settings import paths as leggo_paths_settings
from leggo_fits.parsers import get_all_header_items, create_footprint, set_slice_header, get_cube_slice, \
    write_fits_image


def proccess_upload(request, *args, **kwargs):
    uploaded_object = FFUpload.objects.get(pk=kwargs.get('pk'))
    file_name = os.path.basename(str(uploaded_object.file_upload))

    # Header parsr
    parsed_header, original_header = get_all_header_items(file_name)

    slice_header = set_slice_header(original_header)

    if 'NAXIS4' in parsed_header:
        naxis4_range = range(int(parsed_header['NAXIS4']))
    else:
        naxis4_range = [None]

    if 'NAXIS3' in parsed_header:
        naxis3_range = range(int(parsed_header['NAXIS3']))
    else:
        naxis3_range = [None]

    for naxis3 in naxis3_range:
        for naxis4 in naxis4_range:
            new_file_image = "{}.fits".format(uuid.uuid1().hex)
            new_file_path = os.path.join(leggo_paths_settings.FILE_WORKING, new_file_image)
            cube_slice = get_cube_slice(file_name, naxis3=naxis3, naxis4=naxis4)

            write_fits_image(data=cube_slice, header=slice_header, out_image=new_file_path)

            footprint = create_footprint(in_image=new_file_path)

            parsed_slice_header, original_slice_header = get_all_header_items(file_name)

            # naxis_center_x = int(parsed_header['NAXIS1']/2)
            # naxis_center_2 = int(parsed_header['NAXIS2']/2)

            new_wcs = WCS(slice_header)

            origin = SkyCoord.from_pixel(
                slice_header['NAXIS1'] / 2,
                slice_header['NAXIS2'] / 2,
                wcs=new_wcs,
                origin=1)

            corner_distances = []
            for corner in footprint:
                corner_coord = SkyCoord(ra=corner[0] * u.degree, dec=corner[1] * u.degree)
                sep = corner_coord.separation(origin)
                corner_distances.append(sep.deg)

            ff = FF.objects.create(
                file_upload=uploaded_object,
                fits=new_file_image,
                naxis3=naxis3,
                naxis4=naxis4,
                footprint=footprint.tolist(),
                center_x=origin.ra.deg,
                center_y=origin.dec.deg,
                radius=max(corner_distances)

            )

            FFHeader.objects.create(
                fits=ff,
                parsed_header=parsed_slice_header,
                full_header = slice_header
            )

            # footprint = create_footprint(in_image=new_file_path).flatten()
            # FFFootprint.objects.create(
            #     fits=ff,
            #     x0=footprint[0],
            #     y0=footprint[1],
            #     x1=footprint[2],
            #     y1=footprint[3],
            #     x2=footprint[4],
            #     y2=footprint[5],
            #     x3=footprint[6],
            #     y3=footprint[7],
            # )

    first_fits = FF.objects.filter(file_upload=uploaded_object).first()
    return HttpResponseRedirect(reverse('fits_details_form_view',
                                        kwargs={'upfitspk': kwargs.get('pk'),
                                                'pk'      : first_fits.id}
                                        )
                                )
