# Quantum Computing Band Structure Calculation for Solid-State Materials

This repository contains code for quantum computing calculations of band structures for solid-state materials. The code is based on the JARVIS (Joint Automated Repository for Various Integrated Simulations) framework and utilizes quantum algorithms for electronic structure calculations.

## Citation

If you find this code useful in your research, please consider also citing the following paper:

Choudhary, K. (2021). "Quantum Computation for Predicting Solid-State Electron and Phonon Properties." *J. Phys.: Condens. Matter*, 33(38), 385501. DOI: [10.1088/1361-648X/ac1154](https://doi.org/10.1088/1361-648X/ac1154)

## Overview

The code uses the Qiskit library for quantum computing and the JARVIS database for obtaining material information. It demonstrates the calculation of the band structure for solid-state materials using quantum algorithms such as Variational Quantum Eigensolver (VQE) and Variational Quantum Deflation (VQD).

## Getting Started

### Prerequisites

- [Qiskit](https://qiskit.org/)
- [JARVIS](https://jarvis.nist.gov/)
- [matplotlib](https://matplotlib.org/)

### Installation

```bash
pip install qiskit
pip install jarvis-tools
pip install matplotlib
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/adiazcarral/quantum-band-structure.git
    cd quantum-band-structure
    ```

2. Run the code:

    ```bash
    python quantum_band_structure.py
    ```

3. View the generated band structure plot in the `bands.png` file.

## Code Structure

- `quantum_band_structure.py`: Main script containing the quantum computing code for band structure calculations.
- `jarvis.db.figshare`: Module for accessing the JARVIS database.
- `jarvis.io.qiskit.inputs`: Module for input preparation for Qiskit.
- `jarvis.core.kpoints`: Module for generating k-points for band structure calculations.
- `jarvis.core.circuits`: Module containing Quantum Circuit Library for VQE.

## Quantum Algorithms Used

1. **Variational Quantum Eigensolver (VQE):** Used for electronic structure calculations.
2. **Variational Quantum Deflation (VQD):** Employed for quantum deflation of the obtained eigenstates.

## Examples

The provided code includes examples for various materials, such as graphene, aluminum, silicon, and lead sulfide. You can modify the `jid` parameter in the code to choose a different material.

```python
# Example for Silicon (JVASP-1002)
wtbh, Ef, atoms = get_wann_electron(jid="JVASP-1002")
```

## Acknowledgments

- [JARVIS](https://jarvis.nist.gov/) - Joint Automated Repository for Various Integrated Simulations
- [Qiskit](https://qiskit.org/) - An open-source quantum computing software development framework

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
