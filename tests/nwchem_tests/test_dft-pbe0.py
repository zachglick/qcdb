#! pbe/sto-3g H2O DFT energy
import os
import sys
from ..utils import *
from ..addons import *
import qcdb

h2o = qcdb.set_molecule('''
        O     0.000000000000    0.000000000000   -0.068516219310
        H     0.000000000000   -0.790689573744    0.543701060724
        H     0.000000000000    0.790689573744    0.543701060724
        ''')
print(h2o)


def check_dft(return_value, is_df):
    if is_df:
        ref = -75.251809079677
        assert compare_values(ref, qcdb.get_variable('DFT TOTAL ENERGY'), 5, 'DFT total')  #TEST
    else:
        ref = -74.964662543238
        assert compare_values(ref, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'HF total')  #TEST


@using_nwchem
def test_1_dft():
    qcdb.set_options({
        'basis': 'sto-3g',
        'memory': '3000 mb',
        #'e_convergence': 1.0e-7,
        #'scf__d_convergence': 1.0e-7,
        'nwchem_charge': 0,
        'nwchem_dft__direct': True,
        'nwchem_dft__xc': 'pbe0',
        #'nwchem_dft__convergence__energy': 1.0e-7,
        #'nwchem_dft__convergence__density': 1.0e-7,
    })
    print('Testing DFT total energy...')
    val = qcdb.energy('nwc-pbe0')
    check_dft(val, is_df=True)


@using_nwchem
def test_2_hf():
    qcdb.set_options({
        'basis': 'sto-3g',
        'memory': '3000 mb',
        'e_convergence': 1.0e-7,
        #'nwchem_charge': 0,
    })
    print('Testing HF energy...')
    value = qcdb.energy('nwc-hf')
    check_dft(value, is_df=False)