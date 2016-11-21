#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import uniflex_module_gnuradio

'''
    Direct module test; without framework.
    Req.: GnuRadio has to be installed: apt-get install gnuradio
'''
if __name__ == '__main__':

    grm = uniflex_module_gnuradio.GnuRadioModule()

    fid = open(os.path.join(os.path.expanduser("../"), "testdata", "testgrc.grc"))
    grc_xml = fid.read()

    # print(grc_xml)

    grc_radio_program_name = 'test'
    inval = {}
    inval['ID'] = 11
    inval['grc_radio_program_code'] = grc_xml

    grm.activate_radio_program(grc_radio_program_name, **inval)

    time.sleep(2)
    if True:

        gvals = ['samp_rate', 'freq' ]

        for ii in range(5):
            res = grm.get_parameters(gvals)
            print(res)

    tvals = {}
    tvals['do_pause'] = str(True)
    grm.deactivate_radio_program(grc_radio_program_name, **tvals)
