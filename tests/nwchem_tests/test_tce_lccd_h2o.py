#LCCD

import os
import sys
import qcdb
from ..addons import *
from ..utils import *

h2o = qcdb.set_molecule('''
    H    0.000000000000000   1.079252144093028   1.474611055780858
    O    0.000000000000000   0.000000000000000   0.000000000000000
    H    0.000000000000000   1.079252144093028  -1.47461105578085
        ''')

print(h2o)

def check_lccd(return_value):
    hf      =   -74.506112017705
    lccd_tot=   -75.012682861990669
    lccd_corl=   -0.049777455819604

    assert compare_values(hf, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'hf ref')
    assert compare_values(lccd_tot, qcdb.get_variable('LCCD TOTAL ENERGY'), 5, 'lccd tot')
    assert compare_values(lccd_corl, qcdb.get_variable('LCCD CORRELATION ENERGY'), 5, 'lccd corl')

@using_nwchem
def test_1_lccd():
    qcdb.set_options({
        'basis' : 'sto-3g',
        'memory': '1500 mb',
        #'scf__e_convergence':   1.0e-10,
        'nwchem_scf__thresh':   1.0e-10,
        'nwchem_scf__tol2e' :   1.0e-10,
        'nwchem_scf__singlet':  True,
        'nwchem_scf__rhf'   :   True,
        'qc_module'         :   'TCE',
        'nwchem_tce__lccd'  :   True
        })
    val = qcdb.energy('nwc-lccd')
    check_lccd(val)

def check_lccsd(return_value):
    hf      =   -74.506112017705  
    lccsd_tot   = -75.013554624840296
    lccsd_corl  =   -0.050891562718781

    assert compare_values(hf, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'hf ref')
    assert compare_values(lccsd_tot, qcdb.get_variable('LCCSD TOTAL ENERGY'), 5, 'lccd tot')
    assert compare_values(lccsd_corl, qcdb.get_variable('LCCSD CORRELATION ENERGY'), 5, 'lccd corl')

@using_nwchem
def test_2_lccsd():
    qcdb.set_options({
        'basis' : 'sto-3g',
        'memory': '1500 mb',
        #'scf__e_convergence':   1.0e-10,
        'nwchem_scf__thresh':   1.0e-10,
        'nwchem_scf__tol2e' :   1.0e-10,
        'nwchem_scf__singlet':  True,
        'nwchem_scf__rhf'   :   True,
        'qc_module'         :   'TCE',
        'nwchem_tce__lccsd'  :   True
        })
    val = qcdb.energy('nwc-lccsd')
    check_lccsd(val)

