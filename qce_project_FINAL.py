#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:07:17 2022

@author: angel
"""
# http://lampx.tugraz.at/~hadley/ss1/bzones/fcc.php
# https://aiida-tutorials.readthedocs.io/en/tutorial-2020-intro-week/source/sections/bands.html


from jarvis.db.figshare import get_wann_electron, get_wann_phonon, get_hk_tb
from jarvis.io.qiskit.inputs import HermitianSolver, get_bandstruct, get_dos
from jarvis.core.kpoints import generate_kgrid
import numpy as np
import qiskit
from qiskit import Aer
from jarvis.core.circuits import QuantumCircuitLibrary
import matplotlib.pyplot as plt
# JVASP-667 graphene
# JVASP-816 Al
# JVASP-1002 Si
# JVASP-35680 PbS
#########################
##### Download WTBH #####
wtbh, Ef, atoms = get_wann_electron(jid="JVASP-1002")
# wtbh, atoms = get_wann_phonon(jid="JVASP-1002",  factor=34.3)
#########################

################################################
##### Transform WTBH into Hermitian matrix #####

# kpt = [0.5, 0., 0.5] #X-point jarvis
kpt = [0., 0., 0.] #gamma-point
##########
hk = get_hk_tb(w=wtbh, k=kpt)
HS = HermitianSolver(hk)
n_qubits = HS.n_qubits()
reps = 6
circ = QuantumCircuitLibrary(n_qubits=n_qubits, reps=reps).circuit6()
backend = Aer.get_backend("statevector_simulator")
################################################

###########
### VQE ### 
en, vqe_result, vqe = HS.run_vqe(mode='min_val',var_form=circ,backend=backend)
vals, vecs = HS.run_numpy()
params = vqe.optimal_params
circuit = vqe.construct_circuit(params)
print('Classical, VQE (eV)', (vals[0] - Ef),(en - Ef))
print('Classical, VQE (eV)', (vals[0]),(en))
print(Ef)
###########

#### VQD ####
eigenvalues, eigenstates = HS.run_vqd(backend=backend, reps=reps)
vals, vecs = HS.run_numpy()
print('Classical, VQD (eV)', (vals[0] - Ef),(eigenvalues[0] - Ef))
#############

### BANDSTRUCTURE ###
bands = get_bandstruct(
    w=wtbh,
    atoms=atoms,
    # ef=Ef,
    line_density=5,
    ylabel="Energy (Ev)",
    font=12,
    var_form=None,
    filename="bands.png",
    savefig=True,
    neigs=None,
    max_nk=None,
    tol=None,
)
######################