#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Quantum Computing Band Structure Calculation for Solid-State Materials
This script utilizes Qiskit and JARVIS for quantum computing calculations of band structures
for solid-state materials. It demonstrates the use of advanced quantum algorithms, such as
Variational Quantum Eigensolver (VQE) and Variational Quantum Deflation (VQD).
Author: Angel Diaz Carral
'''

from jarvis.db.figshare import get_wann_electron, get_hk_tb
from jarvis.io.qiskit.inputs import HermitianSolver, get_bandstruct
from jarvis.core.circuits import QuantumCircuitLibrary
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def download_wtbh(jid):
    """Download Wannier Hamiltonian."""
    wtbh, Ef, atoms = get_wann_electron(jid=jid)
    return wtbh, Ef, atoms

def transform_to_hermitian(wtbh, kpt):
    """Transform Wannier Hamiltonian to Hermitian matrix."""
    hk = get_hk_tb(w=wtbh, k=kpt)
    HS = HermitianSolver(hk)
    n_qubits = HS.n_qubits()
    reps = 6
    circ = QuantumCircuitLibrary(n_qubits=n_qubits, reps=reps).circuit6()
    return HS, circ

def run_vqe_and_vqd(HS, circ, backend, Ef):
    """Run VQE and VQD algorithms."""
    en, _, vqe = HS.run_vqe(mode='min_val', var_form=circ, backend=backend)
    vals, _ = HS.run_numpy()
    
    # VQE
    params = vqe.optimal_params
    circuit = vqe.construct_circuit(params)
    print('Classical, VQE (eV)', (vals[0] - Ef), (en - Ef))
    print('Classical, VQE (eV)', vals[0], en)
    print(Ef)

    # VQD
    eigenvalues, _ = HS.run_vqd(backend=backend, reps=reps)
    print('Classical, VQD (eV)', (vals[0] - Ef), (eigenvalues[0] - Ef))

def generate_band_structure(wtbh, atoms):
    """Generate band structure."""
    bands = get_bandstruct(
        w=wtbh,
        atoms=atoms,
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

def main():
    # JVASP-1002 Si
    jid = "JVASP-1002"
    
    # Download WTBH
    wtbh, Ef, atoms = download_wtbh(jid)
    
    # Transform WTBH into Hermitian matrix
    kpt = [0., 0., 0.]  # gamma-point
    HS, circ = transform_to_hermitian(wtbh, kpt)
    
    # Use AerSimulator for state vector simulation
    backend = AerSimulator()
    
    # Run VQE and VQD
    run_vqe_and_vqd(HS, circ, backend, Ef)
    
    # Generate Band Structure
    generate_band_structure(wtbh, atoms)

if __name__ == "__main__":
    main()
